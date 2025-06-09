def classify_payload(payload):
    payload_lower = payload.lower()

    if any(x in payload_lower for x in ["<script", "<img", "onerror", "svg", "alert("]):
        return ("XSS", "Critique")
    elif any(x in payload_lower for x in ["' or", '" or', "1=1", "drop table", "union select"]):
        return ("SQL Injection", "Critique")
    elif any(x in payload_lower for x in [";","|", "$(", "`id`", "whoami", "/etc/passwd"]):
        return ("Command Injection", "Critique")
    elif any(x in payload_lower for x in ["../../", "file://", "php://", ".env", ".git"]):
        return ("File Inclusion / Disclosure", "Critique")
    elif any(x in payload_lower for x in ["{{", "${", "<%="]):
        return ("SSTI", "Critique")
    elif any(x in payload_lower for x in ["http://", "https://", "redirect=", "next="]):
        return ("Open Redirect", "Moyen")
    else:
        return ("Inconnu", "Info")
