from datetime import datetime

def generate_html_report(results_dict, url, filename="rapport.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html lang='fr'>\n")
        f.write("<head>\n")
        f.write("  <meta charset='UTF-8'>\n")
        f.write("  <title>Rapport de Scan Web</title>\n")
        f.write("  <style>\n")
        f.write("    body { font-family: Arial, sans-serif; margin: 40px; background-color: #f9f9f9; color: #333; }\n")
        f.write("    h1 { color: #2c3e50; }\n")
        f.write("    h2 { color: #2980b9; border-bottom: 1px solid #ccc; padding-bottom: 5px; }\n")
        f.write("    ul { list-style-type: square; padding-left: 20px; }\n")
        f.write("    li { margin-bottom: 10px; }\n")
        f.write("    .ok { color: green; }\n")
        f.write("    .error { color: red; }\n")
        f.write("    .footer { margin-top: 50px; font-size: 0.9em; color: #888; }\n")
        f.write("  </style>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write(f"  <h1>📋 Rapport de Scan — {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</h1>\n")
        f.write(f"  <p>URL scannée : <strong>{url}</strong></p>\n")

        for section, results in results_dict.items():
            f.write(f"  <h2>{section}</h2>\n")
            f.write("  <ul>\n")
            if results:
                for r in results:
                    css_class = "ok" if "✅" in r else "error" if "❌" in r or "⚠️" in r else ""
                    f.write(f"    <li class='{css_class}'>{r}</li>\n")
            else:
                f.write("    <li class='ok'>✅ Aucun problème détecté</li>\n")
            f.write("  </ul>\n")

        f.write("<div class='footer'>Généré par WebScanner - https://github.com/Houssein-Majed ©</div>\n")
        f.write("</body>\n")
        f.write("</html>")
