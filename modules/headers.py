import requests

def check_headers(url):

    response = requests.get(url)
    headers = response.headers
    issues = []

    if 'X-Frame-Options' not in headers:
        issues.append(
            "❌ X-Frame-Options manquant — <a href='https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/X-Frame-Options' target='_blank'>[solution]</a>"
        )

    if 'Content-Security-Policy' not in headers:
        issues.append(
            "❌ CSP manquant — <a href='https://developer.mozilla.org/fr/docs/Web/HTTP/CSP' target='_blank'>[solution]</a>"
        )

    if 'X-Content-Type-Options' not in headers:
        issues.append(
            "❌ X-Content-Type-Options manquant — <a href='https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/X-Content-Type-Options' target='_blank'>[solution]</a>"
        )

    if 'Strict-Transport-Security' not in headers:
        issues.append(
            "❌ HSTS manquant — <a href='https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Strict-Transport-Security' target='_blank'>[solution]</a>"
        )

    if 'Referrer-Policy' not in headers:
        issues.append(
            "❌ Referrer-Policy manquant — <a href='https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Referrer-Policy' target='_blank'>[solution]</a>"
        )

    return issues
