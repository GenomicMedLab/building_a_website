"""Update software description files with metadata acquired from remote sources like GitHub."""
import traceback
import os
import re
from typing import Dict, List, Tuple, Optional
from pathlib import Path
import yaml

import markdown
import requests


# API key required - otherwise the request rate limit is pretty low
token = os.environ.get("GITHUB_API_KEY")
if not token:
    raise ValueError("Must supply GitHub API key under env var GITHUB_API_KEY")
request_headers = {"Authorization": f"Bearer {token}"}


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


def get_latest_commits(org: str, repo: str) -> List:
    url = f"https://api.github.com/repos/{org}/{repo}/commits?sha=main"
    commits = requests.get(url, headers=request_headers).json()
    commit_data = []
    for commit in commits[:5]:
        commit_data.append(
            {
                "commit": commit["commit"]["message"].split("\n")[0],
                "author": commit["author"]["login"],
                "url": commit["html_url"],
            }
        )

    return commit_data


def get_languages(org: str, repo: str) -> List:
    # filter out stuff like "makefile"
    # update as needed
    permitted_languages = [
        "Python",
        "Shell",
        "Ruby",
        "TypeScript",
        "Rust",
    ]
    url = f"https://api.github.com/repos/{org}/{repo}/languages"
    language_data = requests.get(url, headers=request_headers).json()
    languages = []
    for d in list(language_data)[:5]:
        if d in permitted_languages:
            languages.append(d)
    return languages


def get_latest_release(org: str, repo: str) -> Optional[Dict]:
    url = f"https://api.github.com/repos/{org}/{repo}/releases"
    repo_data = requests.get(url, headers=request_headers).json()
    try:
        return {
            "version": repo_data[0]["tag_name"],
            "url": repo_data[0]["html_url"],
        }
    except IndexError:
        return None


def get_contributors(org: str, repo: str) -> List:
    url = f"https://api.github.com/repos/{org}/{repo}/contributors"
    contributor_data = requests.get(url, headers=request_headers).json()
    # get all contributors -- filter out external users in template
    return [c["login"] for c in contributor_data]


def get_docs(org: str, repo: str) -> Optional[str]:
    url = f"https://api.github.com/repos/{org}/{repo}"
    repo_data = requests.get(url, headers=request_headers).json()
    homepage = repo_data.get("homepage")
    if not homepage or "readthedocs" not in homepage:
        return None
    return homepage


def get_description(org: str, repo: str) -> Optional[str]:
    url = f"https://raw.githubusercontent.com/{org}/{repo}/main/README.md"
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.HTTPError:
        return None
    pattern = "<!-- description -->([\\S\\s]*)<!-- /description -->"
    description_matches = re.findall(pattern, response.text)
    if not description_matches:
        return None
    description = description_matches[0]
    html = markdown.markdown(description, extensions=["sane_lists"])
    processed = re.sub("\\n", "", html)
    return processed


def write_updated_file(file: Path, data: Dict, content: List) -> None:
    yaml_str = yaml.dump(data)
    content_str = "\n".join([line for line in content if line != "\n"])
    with open(file, "w") as f:
        f.write("---\n")
        f.write(yaml_str)
        f.write("---\n")
        f.write(content_str + "\n")


def update_file(file: Path) -> None:
    data, content = get_file_yaml(file)
    org, repo = re.findall("[https:]?github.com/(.+)/(.+)/?", data["source"])[0]
    repo = repo.strip("/")
    data["latest_commits"] = get_latest_commits(org, repo)
    data["languages"] = get_languages(org, repo)
    data["latest_release"] = get_latest_release(org, repo)
    data["contributors"] = get_contributors(org, repo)
    # only overwrite if available
    docs = get_docs(org, repo)
    if docs:
        data["docs"] = docs
    description = get_description(org, repo)
    if description:
        data["description"] = description
    write_updated_file(file, data, content)


def update_software_files() -> None:
    for file in Path("_software").glob("**/*"):
        print(f"Processing {file}...", end=" ")
        try:
            update_file(file)
            print("ok.")
        except Exception as e:
            print(e)
            traceback.print_exc()


if __name__ == "__main__":
    update_software_files()
