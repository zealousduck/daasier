#!/bin/sh

export serverport=5000
export serverip=127.0.0.1
export FLASK_APP=daasierserver.py
python3 -m flask run --host=${serverip} --port=${serverport}
