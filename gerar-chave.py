#!/usr/bin/env python3
"""
Gera o nome de arquivo para cada PDF a partir da palavra-chave da noite.

Uso:
    python3 gerar-chave.py "estrategia"
    python3 gerar-chave.py "estrategia" "tabuleiro" "sala de guerra"

O nome do arquivo e derivado da palavra-chave. Quem nao tem a palavra
nao consegue montar a URL do PDF, e o codigo-fonte da pagina nao a revela.

A normalizacao e a MESMA que roda no navegador (index.html):
minusculas, sem acento, so letras e numeros.
"""

import hashlib
import sys
import unicodedata

SAL = "blackbook-tutory-2026"   # precisa ser identico ao SAL do index.html


def normalizar(palavra: str) -> str:
    """minusculas, sem acento, so a-z0-9 — igual ao normalizar() do JS."""
    sem_acento = unicodedata.normalize("NFD", palavra.lower())
    sem_acento = "".join(c for c in sem_acento if unicodedata.category(c) != "Mn")
    return "".join(c for c in sem_acento if c.isalnum())


def nome_arquivo(palavra: str, parte: int) -> str:
    """O numero da parte entra no hash: a mesma palavra em partes
    diferentes gera arquivos diferentes."""
    base = normalizar(palavra)
    semente = "%s:%d:%s" % (SAL, parte, base)
    digest = hashlib.sha256(semente.encode("utf-8")).hexdigest()
    return digest[:20] + ".pdf"


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__.strip())
        return 1

    print()
    for palavra in sys.argv[1:]:
        base = normalizar(palavra)
        if not base:
            print(f'  "{palavra}"  ->  INVALIDA (vazia depois de normalizar)')
            continue
        print(f'  palavra-chave : "{palavra}"')
        print(f'  normalizada   : {base}')
        for parte in (1, 2, 3):
            print(f'    parte {parte} -> pdfs/{nome_arquivo(palavra, parte)}')
        print()

    print("  Coloque os arquivos renomeados em lp-blackbook/pdfs/ e publique.")
    print("  Anuncie a palavra-chave na live. O resto a pagina resolve.")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
