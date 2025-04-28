#!/bin/sh
source ./.venv/bin/activate
pyinstaller ./main.py --onefile -n pycalcbar
