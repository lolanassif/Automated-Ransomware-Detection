import os

# Extensions غالبًا طبيعية ومسموح بيها
WHITELIST_EXTENSIONS = [
    ".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx",
    ".jpg", ".jpeg", ".png", ".gif", ".mp4", ".mp3"
]

# Extensions مشبوهة
SUSPICIOUS_EXTENSIONS = [
    ".locked", ".encrypted", ".crypt", ".enc", ".wncry", ".block"
]

def analyze(file_path, old_size, new_size, old_time, new_time):
    score = 0
    reasons = []

    ext = os.path.splitext(file_path)[1].lower()

    # 1) لو الامتداد مشبوه جدًا
    if ext in SUSPICIOUS_EXTENSIONS:
        score += 70
        reasons.append("suspicious extension")

    # 2) تغيير كبير في الحجم
    size_diff = abs(new_size - old_size)
    if size_diff > 50000:   # 50 KB
        score += 20
        reasons.append("large size change")

    # 3) تعديل سريع جدًا
    time_diff = new_time - old_time
    if time_diff < 0.5:
        score += 10
        reasons.append("rapid modification")

    # 4) تقليل الخطورة لو الملف من whitelist
    # عشان ملف PDF عادي أو DOCX عادي مايتبلوكش بسهولة
    if ext in WHITELIST_EXTENSIONS:
        score -= 20
        reasons.append("whitelisted extension")

    # ماينفعش السcore يبقى بالسالب
    score = max(score, 0)

    return score, reasons, ext