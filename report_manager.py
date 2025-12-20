import json
import os
from datetime import datetime

REPORT_FILE = "reports.json"

def _load_reports():
    if not os.path.exists(REPORT_FILE):
        return []
    try:
        with open(REPORT_FILE, "r", encoding="utf-8") as f:
            return json.load(f) if isinstance(json.load(f), list) else []
    except:
        return []

def _save_reports(reports):
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(reports, f, indent=4)

def add_report(summary: str):
    reports = _load_reports()
    reports.append({"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "summary": summary.strip()})
    _save_reports(reports)
    print(f"\nRapport sparad! ({len(reports)} totalt)")

def list_reports() -> bool:
    reports = _load_reports()
    if not reports:
        print("Inga rapporter ännu.")
        return False
    print("\n=== GAMLA RAPPORTER ===")
    for i, r in enumerate(reports, 1):
        print(f"{i}. {r['date']}")
    print("==========================\n")
    return True

def show_report(index: int):
    reports = _load_reports()
    try:
        r = reports[index]
        print(f"\nRapport från {r['date']}\n")
        print(r['summary'])
    except:
        print("Fel nummer!")