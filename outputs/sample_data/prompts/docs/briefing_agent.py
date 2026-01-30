#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import datetime

DEFAULT_BRIEFING = """# Daily Azure Security Briefing

## Top Risks (Today)
- No data provided (MVP stub). Add exports to ./sample_data to populate this report.

## Detections / Incidents
- No data provided.

## Identity & Privilege Changes
- No data provided.

## Azure Control-Plane Changes
- No data provided.

## Recommended Actions (Owner + ETA)
- Assign an owner to connect exports (Mode A) or KQL/API queries (Mode B).
"""

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="./sample_data", help="Folder with exported files (future)")
    p.add_argument("--out", default="./outputs/daily_briefing.md", help="Output report file")
    args = p.parse_args()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    header = f"<!-- generated: {datetime.utcnow().isoformat()}Z -->\n"
    out_path.write_text(header + DEFAULT_BRIEFING, encoding="utf-8")
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()

