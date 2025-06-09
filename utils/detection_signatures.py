detection_signatures = {
    "LFI": [
        "root:x:",          # signature typique de /etc/passwd
        "/bin/bash",
        "daemon:x:"
    ],
    "RFI": [
        "shell by",         # mot commun dans des webshells
        "uname -a",         # output attendu si exécuté
        "uid=",
        "<?php"
    ],
    "Command Injection": [
        "uid=",             # sortie de `id`
        "gid=",             # sortie de `id`
        "Linux",            # sortie de `uname -a`
        "root",             # si command injection donne accès au shell
    ],
    "SSTI": [
        "49",               # résultat de {{7*7}}
        "343",              # résultat de {{7*7*7}}
    ]
}
