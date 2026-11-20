#!/usr/bin/env python3
"""Refresh data/starred.json from the GitHub API and regenerate the
'Starred by d123d' section of README.md in place.

Public data only: uses the unauthenticated /users/d123d/starred endpoint
(set GITHUB_TOKEN in the environment to raise the rate limit).
No credentials are stored in this repo."""
import json, os, re, urllib.request
from collections import OrderedDict

API = "https://api.github.com/users/d123d/starred"
CATS = OrderedDict([
    ("Agents, Harnesses, Skills & MCP", ["agent", "mcp", "claude", "codex", "opencode", "openclaw", "harness", "skill", "prompt", "cursor", "copilot", "aider", "cline", "crewai", "autogen", "langgraph", "orchestrat"]),
    ("3D, Animation & World Generation", ["3d", "blender", "three.js", "threejs", "gaussian", "splat", "mesh", "rig", "animation", "animate", "motion", "avatar", "terrain", "cesium", "maplibre", "trellis", "hunyuan3d", "voxel", "godot", "sculpt"]),
    ("Audio, Voice & Music", ["audio", "voice", "tts", "speech", "music", "song", "vocal", "lip-sync", "lip sync", "dubbing"]),
    ("Video, Image & ComfyUI", ["comfy", "video", "image", "diffusion", "flux", "wan2", "sora", "veo", "kling", "runway", "higgsfield", "photo", "upscale", "cinematic", "film", "shorts", "lora", "inpaint", "editor", "camera", "shot", "previz", "render", "world"]),
    ("LLMs, Models, Training & Inference", ["llm", "ollama", "llama", "qwen", "gemma", "mistral", "gpt", "transformer", "finetune", "fine-tune", "unsloth", "inference", "embedding", "neural"]),
    ("Games, D&D & Reverse Engineering", ["dnd", "d&d", "dungeon", "rpg", "game", "reverse-engineer", "decomp", "gemrb", "openmw", "devilution", "daggerfall", "bg3", "baldur", "tabletop", "dice"]),
    ("Data, RAG, Memory & Search", ["rag", "memory", "database", "dataset", "search", "vector", "knowledge", "scrape"]),
    ("Automation, Web & Apps", ["telegram", "bot", "browser", "automation", "api", "dashboard", "react", "next.js", "app"]),
])
PRIORITY = ["Audio, Voice & Music", "3D, Animation & World Generation", "Agents, Harnesses, Skills & MCP",
            "Video, Image & ComfyUI", "Games, D&D & Reverse Engineering", "LLMs, Models, Training & Inference",
            "Data, RAG, Memory & Search", "Automation, Web & Apps"]

def fetch():
    token = os.environ.get("GITHUB_TOKEN")
    repos, page = [], 1
    while True:
        req = urllib.request.Request(f"{API}?per_page=100&page={page}")
        req.add_header("Accept", "application/vnd.github+json")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=60) as resp:
            batch = json.load(resp)
        if not batch:
            break
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    return [{"full_name": x["full_name"], "url": x["html_url"], "description": x.get("description"),
             "stars": x["stargazers_count"], "language": x.get("language"),
             "topics": x.get("topics", []), "archived": x["archived"]} for x in repos]

def categorize(r):
    name = r["full_name"].lower()
    text = (r["full_name"] + " " + (r["description"] or "") + " " + " ".join(r["topics"])).lower()
    best, best_score = None, 0
    for cat in PRIORITY:
        kws = CATS[cat]
        score = sum(3 for k in kws if k in name) + sum(1 for k in kws if k in text)
        if score > best_score:
            best, best_score = cat, score
    return best or "Everything Else"

def section(repos):
    grouped = {k: [] for k in list(CATS.keys()) + ["Everything Else"]}
    for r in repos:
        grouped[categorize(r)].append(r)
    out = ["## Starred by d123d — the complete list\n",
           f"All **{len(repos)} GitHub repos starred by [d123d](https://github.com/d123d)**, pulled from the GitHub API and sorted into sections automatically by name, description, and topics (star counts as of the last refresh). Every public star, no cherry-picking (1 private star omitted). Machine-readable copy: [data/starred.json](data/starred.json). Regenerate with `python3 build_list.py`.\n"]
    for cat, items in grouped.items():
        if not items:
            continue
        items.sort(key=lambda x: -x["stars"])
        out.append(f"### {cat} ({len(items)})\n")
        for r in items:
            desc = (r["description"] or "").replace("\n", " ").strip()
            if not desc:
                desc = "No description on GitHub"
                if r["topics"]:
                    desc += " — topics: " + ", ".join(r["topics"][:5])
            elif desc[-1] not in ".!?":
                desc += "."
            lang = f" *{r['language']}.*" if r["language"] else ""
            arch = " *(archived)*" if r["archived"] else ""
            out.append(f"- [{r['full_name']}]({r['url']}) — ★{r['stars']:,} — {desc}{lang}{arch}")
        out.append("")
    return "\n".join(out), {k: len(v) for k, v in grouped.items() if v}

def update_readme(readme, repos):
    """Return the README text with the starred section regenerated, and the per-section counts."""
    sec, counts = section(repos)
    # The replacement is a function, so a backslash in a repo description is not read as a regex escape.
    new, n = re.subn(r"## Starred by d123d — the complete list\n.*?(?=\n## License)", lambda m: sec.rstrip() + "\n", readme, flags=re.S)
    assert n == 1, "README.md: the 'Starred by d123d' section (up to '## License') was not found"
    return new, counts

if __name__ == "__main__":
    repos = fetch()
    readme = open("README.md", encoding="utf-8").read()
    new, counts = update_readme(readme, repos)
    json.dump(repos, open("data/starred.json", "w", encoding="utf-8"), indent=1)
    open("README.md", "w", encoding="utf-8", newline="\n").write(new)
    print(len(repos), counts)
