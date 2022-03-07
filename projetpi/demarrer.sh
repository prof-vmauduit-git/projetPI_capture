#!/bin/sh
# SCRIPT DE DEMARRAGE SERVICES PI DEXTER LYCEE
#
#
#aller dans répertoire projet
#cd /home/pi/Documents/projetpi/
#
#démarrer programme flask
export FLASK_APP=/home/pi/Documents/projetpi/app-rest-v2.py
nohup /home/pi/.local/bin/flask run --host=0.0.0.0 &
#
#aller dans répertoire des scripts
cd /home/pi/bin/
#
#démarrer programme capture
nohup python capter-D4-v5.py &
