def detect_anomaly(log_text):
    if not log_text:
        return "Normal ✅"
    keywords = ["error", "fail", "exception", "crash", "timeout", "denied"]
    for k in keywords:
        if k in log_text.lower():
            return f"Anomaly Detected ❌ (keyword: {k})"
    return "Normal ✅"
