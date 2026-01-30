# azure-ai-security-briefing-agent

Daily, executive-ready Azure security briefing generated from Microsoft Defender + Azure/Entra logs — focused on **risk, detections, and meaningful change**.

## What it produces (the briefing)
A single Markdown report you can paste into email/Teams:

- **Top Risks (Today)** — 3–5 bullets with impact + why it matters
- **Detections / Incidents** — what fired, severity, affected assets, next action
- **Identity & Privilege Changes** — new admins, risky sign-ins, role assignments
- **Azure Control-Plane Changes** — NSGs, Key Vault access, policies, resource changes
- **Recommended Actions** — owner + ETA (clear, operational)

> Goal: compress “what happened + what changed + what to do next” into a 60-second read.

---

## Inputs (planned)
This project is designed to work in two modes:

### Mode A — Export-first (no tenant admin needed)
Start with JSON/CSV exports (from Log Analytics, Defender portals, etc.) and generate a briefing locally.

### Mode B — Live queries (Azure integration)
Pull data directly via:
- **Azure Log Analytics / Microsoft Sentinel** (KQL)
- **Microsoft Defender** (incidents/alerts where available)
- **Entra ID** sign-in & audit logs (where available)

---

## Architecture (MVP)
1. **Collect** signals (exported files now → live APIs later)
2. **Normalize** into a common schema (detections, changes, identity events)
3. **Score & prioritize** (severity + blast radius + novelty)
4. **Summarize** into an executive-ready briefing
5. **Deliver** (Markdown now → email/Teams later)

---

## Quickstart (MVP, export-first)
This repo will ship an MVP that generates `outputs/daily_briefing.md` from sample exports.

**Planned command:**

```bash
python briefing_agent.py \
  --input ./sample_data \
  --out ./outputs/daily_briefing.md
### Quickstart (MVP)
This generates a sample briefing file.

```bash
python briefing_agent.py \
  --input ./sample_data \
  --out ./outputs/daily_briefing.md
