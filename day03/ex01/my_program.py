#!/usr/bin/env python3

import sys
from local_lib.path import Path

def main():
    pasta = Path("pasta_criada")

    if pasta.exists():
        print("Pasta já criada.")
    else: 
        folder = pasta.mkdir()
        file = folder / "sucesso.txt"
        file.write_text("Hello world!!")

        content = file.read_text()
        print("File content:", content)

if __name__ == "__main__":
    main()