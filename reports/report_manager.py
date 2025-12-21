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
            
            if isinstance(data, list):
                return data
            return []
    except:
        return []
        
#Sparar listan med rapporter till filen
def _save_reports(reports):
    try:
        with open(REPORT_FILE, "w", encoding="utf-8") as f:
            json.dump(reports, f, indent=4, ensure_ascii=False)
    except PermissionError:
            print(" " * 18 + "Could not save report – permission error.") 

#Lägger till en ny rapport med dagens datum och tid
def add_report(summary: str, user_name: str = "Unknown"):
    reports = _load_reports()
    
    new_report = {
        "name": user_name.strip().title(),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "summary": summary.strip()
        }
    reports.append(new_report)
    _save_reports(reports)
    print(" " * 18 + "Report saved successfully! 🎀💕")

#Visar en numrerad lista över alla sparade rapporter
def list_reports(current_user: str = None):
    reports = _load_reports()
    if current_user:
        user_reports = [r for r in reports if r.get("name", "Unknown").title() == current_user.title()]
    else:
        user_reports = reports

    if not user_reports:
        print(" " * 18 + "No reports saved for you yet! 🌸")
        return False

    print("\n" + " " * 18 + "=== YOUR PREVIOUS REPORTS ===")
    for i, report in enumerate(user_reports, 1):
        print(f"{' ' * 18}{i}. {report['date']}")
    print(" " * 18 + "==============================\n")
    return True

#Visar en specifik rapport baserat på index (0-baserat)
def show_report(index: int, current_user: str = None):
    reports = _load_reports()
    if current_user:
        user_reports = [r for r in reports if r.get("name", "Unknown").title() == current_user.title()]
    else:
        user_reports = reports

    try:
        report = user_reports[index]
        print("\n" + " " * 18 + f"Report by: {report['name']} on {report['date']}")    
    except IndexError:
        print(" " * 18 + "Invalid report number!")