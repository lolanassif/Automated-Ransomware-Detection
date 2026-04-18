import os
import shutil
from datetime import datetime

QUARANTINE_DIR = "quarantine"

def log_event(level, file_path, details=""):
    with open("logs.txt", "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()} - {level} - {file_path} - {details}\n")

def warn(file_path, reasons=None, score=None):
    print(f"⚠️ Warning only: {file_path}")
    details = f"score={score}, reasons={reasons}" if reasons else ""
    log_event("WARNING", file_path, details)

def respond(file_path, reasons=None, score=None):
    print("🚨 Ransomware-like behavior detected!")

    details = f"score={score}, reasons={reasons}" if reasons else ""
    log_event("BLOCKED", file_path, details)

    try:
        if not os.path.exists(QUARANTINE_DIR):
            os.makedirs(QUARANTINE_DIR)

        filename = os.path.basename(file_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_path = os.path.join(QUARANTINE_DIR, f"{timestamp}_{filename}.blocked")

        shutil.move(file_path, new_path)
        print(f"🛑 File moved to quarantine: {new_path}")

    except Exception as e:
        print(f"❌ Error handling file: {e}")
        log_event("ERROR", file_path, str(e))