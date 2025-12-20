import json
import os
from datetime import datetime

#Filen där rapporterna sparas
REPORT_FILE = "reports.json"

def _load_reports():
    if not os.path.exists(REPORT_FILE):
        return []
    
    try:
        with open(REPORT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            #Säkerställ att det är en lista
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, PermissionError):
        return []
        
#Sparar listan med rapporter till filen
def _save_reports(reports):
    try:
        with open(REPORT_FILE, "w", encoding="utf-8") as f:
            json.dump(reports, f, indent=4, ensure_ascii=False)
    except PermissionError:
        print("Kunde inte spara rapporten – behörighetsfel.")
 
#Lägger till en ny rapport med dagens datum och tid
def add_report(summary: str):
    reports = _load_reports()
    
    new_report = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "summary": summary.strip()
    }
    
    reports.append(new_report)
    _save_reports(reports)
    print(f"\nRapport sparad! (Totalt {len(reports)} rapporter)")

#Visar en numrerad lista över alla sparade rapporter
def list_reports() -> bool:
    reports = _load_reports()
    
    if not reports:
        print("Inga tidigare rapporter finns ännu.")
        return False
    
    print("\n=== TIDIGARE RAPPORTER ===")
    for i, report in enumerate(reports, 1):
        print(f"{i}. {report['date']}")
    
    print("==========================\n")
    return True

#Visar en specifik rapport baserat på index (0-baserat)
def show_report(index: int):
    reports = _load_reports()
    
    try:
        report = reports[index]
        print(f"\nRapport från {report['date']}\n")
        print(report['summary'])
    except IndexError:
        print("Ogiltigt rapportnummer – det finns inte!")