#!/bin/sh


# Instala as dependecias do arquivo requirement.txt
pip install -r requirement.txt --force-reinstall

# Cria a virtual env com o nome django_venv
python3 -m venv django_venv

# Ativa a virtual env
. django_venv/bin/activate

sh

# Desativa a virtual env
deactivate