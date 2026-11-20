# TOOLS.md — Our AI Tools Handout

The inventory behind [Awesome AI Tools](README.md). Everything we actually run, grouped by where it lives. No credentials, tokens, or private URLs — names and jobs only. Snapshot: Nov 19, 2026.

## Recent additions

- **Nov 19, 2026:** dnd-agent-stack tools — stage.py, rigs.py, film.py / film_session.py, srd.py, dmctl.py / state_engine.py, dm_mcp_server.py, lore.py, permissions.py; dnd-library build_lore_index.py.
- **Nov 14, 2026:** 29-skill batch from skills.sh (world generation ×10, Blender/3D ×11, MiniMax ×2, writing/D&D ×5) plus openrouter-typescript-sdk, ponytail, caveman — all in the custom skills list below.
- **Nov 13, 2026:** Telegram bridge to the local coding agent on the PC.

## Cloud agent (Muse, this VM)

- **Agent:** Muse (Muse Spark, Meta) — memory, goals, scheduled jobs, subagents, browser.
- **GitHub helpers:** small API wrappers for creating repos, pushing files, opening PRs, and downloading tarballs — all GitHub writes go through the REST API.
- **Repo creation:** via the GitHub REST API (`POST /user/repos`), verified for awesome-dnd, awesome-forgotten-realms, dnd-library, and this repo.

## Custom skills (34)

- `blender-animation`
- `blender-cameras`
- `blender-export`
- `blender-materials`
- `blender-mcp`
- `blender-modeling`
- `blender-rendering`
- `camera-cinematography`
- `caveman`
- `cesiumjs-terrain-environment`
- `dnd`
- `dnd5e-srd`
- `fantasy-fiction-writer`
- `fantasy-writer`
- `find-skills`
- `game-3d-assets`
- `h3-prompt-writing`
- `layer-3d`
- `maplibre-terrain-rendering`
- `meshy-3d-generation`
- `mmx-cli`
- `oblique-worldbuilding`
- `openrouter-typescript-sdk`
- `ponytail`
- `procedural-gen`
- `recovered-skill-notes`
- `scenario-3d-worlds`
- `story-planning`
- `systemic-worldbuilding`
- `threejs-animation`
- `threejs-world-generation`
- `worldbuilding`
- `worldbuilding-jwynia`
- `worldlabs`

## Muse system skills (58, selection)

`advertising-campaigns`, `app-creation`, `avatar-dance-videos`, `business-finance`, `custom-connector-setup`, `customer-outreach`, `device-data`, `documents`, `email-management`, `event-tickets`, `file-hosting`, `financial-planning`, `fitness-tracking`, `flight-booking`, `flight-tracking`, `forget`, `form-design`, `generate_podcast`, `goals`, `groceries`, `health-review`, `home-control`, `home-search`, `hotel-booking`, `image-search`, `knowledge-organization`, `live-page-checks`, `marketplaces`, `media-library`, `meeting-follow-up`, `messaging`, `mortgage-comparison`, `muse-early-access`, `muse-feedback`, `muse_db`, `music-discovery`, `place-discovery`, `remember-products`, `restaurant-reservations`, `scheduling`, `self-awareness`, `share-ideas`, `shopping`, `smb-product-shots`, `social-content-performance`, `social-publishing`, `spoken-audio`, `store-operations`, `style-tryon`, `subscription-status`, `task-management`, `transcribe-recordings`, `translation`, `trip-planning`, `trip-transport`, `wearables-comms`, `wide-research`, `workout-planning`

## Connectors in use

GitHub, Gmail, Google Calendar / Docs / Sheets / Slides / Drive, Telegram Bot, Duffel, Expedia, FlightAware, Facebook, Instagram, Threads, Messenger, Meta Ads, Spotify, Stripe, Shopify, Instacart, Places, Plaid, 1Password, Tailscale, Ticketmaster, Uber Courier, Shop Pay, UCP catalog search, Muse Mail, Apple Health, Health Connect.

## PC stack (mirrored notes)

- **Coding agents:** Claude Code (local, Telegram-bridged), Codex, Gemini, OpenCode, Crush, OpenClaw gateway.
- **Local inference:** llama.cpp router, Qwen family, IBM Granite 8B, Ollama.
- **Media engine:** ComfyUI + custom nodes, watchdog / idle releaser / process guard, MiniMax H3 via mmx CLI, Edge TTS shim, Whisper.
- **3D / film:** Blender + MPFB 2.0.18, Mesh2Motion, Kimodo, AnyMove, TRELLIS.2 / Pixal3D / Hunyuan3D 2.1 image-to-mesh route, 14,858-clip BVH motion library (CMU, Mixamo, 100STYLE, Bandai, LAFAN1, ZEGGS, KayKit, Rocketbox).
- **Registry:** a canonical PC tool registry (`tools.md`), refreshed weekly by an inventory script (safe stable updates only; no Windows/driver/CUDA-major/paid/multi-GB updates unattended).
- **Automation:** ai-scripts — agent inbox/outbox, cross-agent sync, spend ledger, budget/quota checks, session digests, Telegram senders, ComfyUI guards, backup to Drive.

## Animation tools (from `world-cast/docs/TOOLS.md`, Nov 14, 2026)

- Bodies/rigs: MPFB (Mixamo standard), Rocketbox avatars (MIT), Mesh2Motion (CC0), AnyMove, AssetFurnace / image-to-3dlab.
- Retarget/QA: fe_rig.py retargeter, retarget_check.py (foot slide, joint flips), motion_strip.py, qa_movie.py, motion_judge.py, creature_qa.py, pose_check.py.
- Not usable: TailorRig (unreleased), UniMate (crashes on Windows).

## Rules that keep this stack safe

- Public repos get links and open-license content only; private book texts stay in private repos.
- Read a skill's SKILL.md before installing it; never run third-party install scripts uninspected.
- Secrets never enter a repo, a list, or this handout.
