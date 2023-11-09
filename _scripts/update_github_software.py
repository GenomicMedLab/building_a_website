"""Update software description files with metadata acquired from remote sources like GitHub."""
import os
import re
from typing import Dict, List, Tuple, Optional
from pathlib import Path
import yaml

import requests


# API key required - otherwise the request rate limit is pretty low
token = os.environ.get("GITHUB_API_KEY")
if not token:
    raise ValueError("Must supply GitHub API key under env var GITHUB_API_KEY")
request_headers = {
    "Authorization": f"Bearer {token}"
}


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
        commit_data.append({
            "commit": commit["commit"]["message"].split("\n")[0],
            "author": commit["author"]["login"]
        })

    return commit_data


def get_languages(org: str, repo: str) -> List:
    # filter out stuff like "makefile"
    # update as needed
    permitted_languages = [
        "Python", "Shell", "Ruby", "TypeScript",
    ]
    url = f"https://api.github.com/repos/{org}/{repo}/languages"
    language_data = requests.get(url, headers=request_headers).json()
    languages = []
    for d in list(language_data)[:5]:
        if d in permitted_languages:
            languages.append(d)
    return languages


def get_latest_version(org: str, repo: str) -> Optional[str]:
    url = f"https://api.github.com/repos/{org}/{repo}/releases"
    repo_data = requests.get(url, headers=request_headers).json()
    try:
        return repo_data[0]["tag_name"]
    except IndexError:
        return None


def get_contributors(org: str, repo: str) -> List:
    url = f"https://api.github.com/repos/{org}/{repo}/contributors"
    contributor_data = requests.get(url, headers=request_headers).json()
    # get all contributors -- filter out external users in template
    return [c["login"] for c in contributor_data]


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
    data["latest_version"] = get_latest_version(org, repo)
    data["contributors"] = get_contributors(org, repo)
    write_updated_file(file, data, content)


def update_software_files() -> None:
    for file in Path("_software").glob("**/*"):
        try:
            update_file(file)
        except Exception as e:
            print(file)
            print(e)


# if __name__ == "__main__":
#     update_software_files()
