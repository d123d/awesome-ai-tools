"""Offline checks for build_list.py (no network). Run from the repo root:
python3 -m pytest test_build_list.py   or   python3 test_build_list.py"""
import copy
import json

import build_list as B


def _load():
    return open("README.md", encoding="utf-8").read(), json.load(open("data/starred.json", encoding="utf-8"))


def test_committed_readme_matches_data():
    readme, repos = _load()
    new, counts = B.update_readme(readme, repos)
    assert new == readme
    assert sum(counts.values()) == len(repos)


def test_backslash_in_description_is_kept_literally():
    readme, repos = _load()
    repos = copy.deepcopy(repos)
    repos[0]["description"] = r"Runs from C:\tools\x with \d+ patterns"
    new, _ = B.update_readme(readme, repos)
    assert r"C:\tools\x with \d+ patterns" in new


if __name__ == "__main__":
    test_committed_readme_matches_data()
    test_backslash_in_description_is_kept_literally()
    print("ok")
