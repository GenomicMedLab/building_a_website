"""Update paper descriptions with metadata acquired from crossref.org."""
from pathlib import Path
import re
import traceback
from typing import Tuple, Dict, List

import requests
import yaml


def normalize_string(input: str) -> str:
    return re.sub(r"\s+", " ", input).strip()


def get_file_yaml(file: Path) -> Tuple[Dict, List]:
    with open(file, "r") as f:
        next_line = f.readline()
        while next_line.strip() != "---":
            next_line = f.readline()
        yaml_lines = []
        next_line = f.readline()
        while next_line.strip() != "---":
            yaml_lines.append(next_line)
            next_line = f.readline()
        remaining_lines = []
        next_line = f.readline()
        while next_line:
            remaining_lines.append(next_line)
            next_line = f.readline()

    fmt_lines = "".join(yaml_lines)
    yaml_dict = yaml.safe_load(fmt_lines)
    return yaml_dict, remaining_lines


def write_updated_file(file: Path, data: Dict, content: List) -> None:
    yaml_str = yaml.dump(data, allow_unicode=True, width=float("inf"))
    content_str = "\n".join([line for line in content if line != "\n"])
    with open(file, "w") as f:
        f.write("---\n")
        f.write(yaml_str)
        f.write("---\n")
        f.write(content_str + "\n")


def set_title(data: Dict, msg_data: Dict) -> None:
    titles = msg_data["title"]
    if len(titles) != 1:
        raise ValueError(f"Unexpected # of title options: {titles}")
    data["name"] = normalize_string(titles[0])


def set_date(data: Dict, msg_data: Dict) -> None:
    if data.get("date"):
        return None
    # TODO figure out date hierarchy
    # want to replace preprint/published online first date with final print date


def _fmt_author(author: Dict) -> str:
    try:
        if author.get("given"):
            name = f"{author['given']} {author['family']}"
        else:
            name = author["family"]
        if author.get("suffix"):
            name = f"{name} {author['suffix']}"
    except KeyError:
        name = author["name"]
    return name


def set_authors(data: Dict, msg_data: Dict) -> None:
    authors = msg_data["author"]
    author_string = ", ".join([_fmt_author(a) for a in authors])
    author_string.replace("\xa0", " ")
    if author_string:
        data["authors"] = normalize_string(author_string)


def set_journal(data: Dict, msg_data: Dict) -> None:
    journal = msg_data["container-title"]
    if len(journal) > 1:
        raise ValueError(f"Unexpected # of journal titles: {journal}")
    elif len(journal) == 0:
        return None
    data["journal"] = normalize_string(journal[0])


def update_file(file: Path) -> None:
    data, content = get_file_yaml(file)
    doi = data.get("doi")
    if not doi:
        return
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    response.raise_for_status()
    response_content = response.json()
    if response_content["status"] != "ok" or not response_content["message-version"].startswith("1."):
        raise ValueError
    msg_data = response_content["message"]

    set_title(data, msg_data)
    set_date(data, msg_data)
    set_authors(data, msg_data)
    set_journal(data, msg_data)
    # TODO
    # set_publisher_url(data, msg_data)
    # set_abstract(data, msg_data)

    write_updated_file(file, data, content)


def update_paper_files() -> None:
    for file in Path("_papers").glob("**/*"):
        print(f"Processing {file}...", end=" ")
        try:
            update_file(file)
            print("ok.")
        except Exception as e:
            print(e)
            traceback.print_exc()


if __name__ == "__main__":
    update_paper_files()
