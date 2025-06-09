import requests
import os
import logging

logging.basicConfig(filename='scanner.log', level=logging.INFO)

def load_common_paths(filepath="paths.txt"):
    if not os.path.exists(filepath):
        print(f"[!] Fichier {filepath} introuvable.")
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def scan_common_paths(base_url):
    found = []
    paths = load_common_paths()

    for path in paths:
        url = base_url.rstrip("/") + path
        try:
            r = requests.get(url, timeout=3)
            if r.status_code < 400:
                found.append(f"🔍 Trouvé : {url} (status {r.status_code})")
        except requests.Timeout:
            logging.warning(f"Timeout sur {url}")
        except requests.ConnectionError:
            logging.warning(f"Erreur de connexion sur {url}")
        except requests.HTTPError as e:
            logging.warning(f"Erreur HTTP sur {url} : {e}")
        except requests.RequestException as e:
            logging.error(f"Erreur inattendue sur {url} : {e}")

    return found