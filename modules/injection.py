import requests
import os
from utils.classifier import classify_payload
from utils.detection_signatures import detection_signatures

def load_payloads(filepath="payloads.txt"):
    if not os.path.exists(filepath):
        print(f"[!] Fichier {filepath} introuvable.")
        return []
    
    with open(filepath, "r", encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]

def test_injections(url):
    results = []
    payloads = load_payloads()

    for payload in payloads:
        test_url = url + "?test=" + payload
        try:
            r = requests.get(test_url, timeout=5)
            if payload in r.text:
                vuln_type, severity = classify_payload(payload)

                # Vérification si la vulnérabilité semble réellement exploitée
                indicators = detection_signatures.get(vuln_type, [])
                real_effect = any(ind in r.text for ind in indicators)

                if real_effect:
                    results.append(f"{severity} ({vuln_type}) → {payload} ✅ exploit détecté")
                else:
                    results.append(f"{severity} ({vuln_type}) → {payload} ⚠️ reflet détecté")
        except requests.exceptions.RequestException as e:
            results.append(f"⚠️ Erreur pour {test_url} : {e}")

    return results