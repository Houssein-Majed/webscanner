from modules.headers import check_headers
from modules.pages import scan_common_paths
from modules.injection import test_injections
from utils.report import generate_html_report
from urllib.parse import urlparse
import sys

def validate_url(url):
    try:
        result = urlparse(url)
        return result.scheme in ['http', 'https'] and result.netloc
    except ValueError:
        return False

# Lecture de l'URL en argument ou via input
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = input("Entrez l'URL à scanner (ex: https://example.com) : ")

if not validate_url(url):
    print("Erreur : URL invalide. Veuillez entrer une URL valide (ex: https://example.com).")
    exit(1)

# Nettoyage de l'URL (suppression de #fragment et des query params si nécessaire)
parsed = urlparse(url)
base_url = f"{parsed.scheme}://{parsed.netloc}"

# Appel des modules après nettoyage
results = {
    "Headers": check_headers(base_url),
    "Pages communes": scan_common_paths(base_url),
    "Injections": test_injections(base_url)
}

# Génération du rapport HTML
generate_html_report(results, base_url)
print("Rapport généré dans 'rapport.html'")
