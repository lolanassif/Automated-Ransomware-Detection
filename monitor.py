import time
import os
from detector import analyze
from response import respond, warn

WATCH_FOLDER = "./testfolder"

seen_files = {}

# Thresholds
THRESHOLD_BLOCK = 70
THRESHOLD_WARN = 30

def monitor():
    print("👀 Monitoring started ...")

    while True:
        try:
            for root, dirs, files in os.walk(WATCH_FOLDER):
                for file in files:
                    file_path = os.path.join(root, file)

                    try:
                        current_size = os.path.getsize(file_path)
                        current_time = os.path.getmtime(file_path)

                        if file_path in seen_files:
                            old_size, old_time = seen_files[file_path]

                            score, reasons, ext = analyze(
                                file_path,
                                old_size,
                                current_size,
                                old_time,
                                current_time
                            )

                            # قاعدة خاصة للـ whitelist:
                            # لو الامتداد طبيعي، مايتعملوش block
                            # إلا لو فيه سبب قوي جدًا أو أكتر من علامة خطر
                            is_whitelisted = "whitelisted extension" in reasons
                            danger_signs = [r for r in reasons if r != "whitelisted extension"]

                            if is_whitelisted:
                                if score >= THRESHOLD_BLOCK and len(danger_signs) >= 2:
                                    print(f"🚨 HIGH RISK ({score}) -> {file_path} | {reasons}")
                                    respond(file_path, reasons, score)
                                elif score >= THRESHOLD_WARN:
                                    print(f"⚠️ MEDIUM RISK ({score}) -> {file_path} | {reasons}")
                                    warn(file_path, reasons, score)
                            else:
                                if score >= THRESHOLD_BLOCK:
                                    print(f"🚨 HIGH RISK ({score}) -> {file_path} | {reasons}")
                                    respond(file_path, reasons, score)
                                elif score >= THRESHOLD_WARN:
                                    print(f"⚠️ MEDIUM RISK ({score}) -> {file_path} | {reasons}")
                                    warn(file_path, reasons, score)

                        seen_files[file_path] = (current_size, current_time)

                    except FileNotFoundError:
                        continue
                    except PermissionError:
                        continue

            time.sleep(2)

        except KeyboardInterrupt:
            print("🛑 Monitoring stopped.")
            break

if __name__ == "__main__":
    monitor()