#!/bin/sh
source ./.venv/bin/activate
pyinstaller ./main.py --onefile -w -n pycalcbar