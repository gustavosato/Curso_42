#!/bin/sh

# Install the dependencies from the requirement.txt file
pip install -r requirement.txt --force-reinstall

# Create a virtual environment named django_venv
python3 -m venv django_venv

# Activate the virtual environment
. django_venv/bin/activate

# Deactivate the virtual environment
deactivate  