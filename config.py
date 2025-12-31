import os

REPORTS_DIR = "reports"
REPORT_FILE = os.path.join(REPORTS_DIR, "reports.json")

# Skapa mappen om den inte finns
os.makedirs(REPORTS_DIR, exist_ok=True)