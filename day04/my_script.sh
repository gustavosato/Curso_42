#!/bin/sh

# Create a virtual environment named django_venv
python3 -m venv django_venv

# Activate the virtual environment
. django_venv/bin/activate

# Verifica a versão do 'pip' instalado
python -m pip --version

# Install the dependencies from the requirement.txt file
python -m pip install --force-reinstall -r requirement.txt