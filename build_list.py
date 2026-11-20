#!/usr/bin/env python3
"""Refresh the 'Starred by d123d' section from the GitHub API.
Uses GITHUB_TOKEN from the environment if set (not required for public data).
Writes data/starred.json (slim)."""
import json, os, urllib.request
token = os.environ.get("GITHUB_TOKEN")
repos, page = [], 1
while True:
    req = urllib.request.Request(f"https://api.github.com/users/d123d/starred?per_page=100&page={page}")
    req.add_header("Accept", "application/vnd.github+json")
    if token: req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        batch = json.load(resp)
    if not batch: break
    repos += batch
    if len(batch) < 100: break
    page += 1
slim = [{"full_name": x["full_name"], "url": x["html_url"], "description": x.get("description"),
         "stars": x["stargazers_count"], "language": x.get("language"),
         "topics": x.get("topics", []), "archived": x["archived"]} for x in repos]
json.dump(slim, open("data/starred.json", "w"), indent=1)
print(f"{len(repos)} starred repos -> data/starred.json")
