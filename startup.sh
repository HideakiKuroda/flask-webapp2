#!/bin/bash
python -m venv /home/site/wwwroot/antenv
source source /home/site/wwwroot/antenv/bin/activate
COPY /home/site/wwwroot/startup.sh /opt/startup/startup.sh
pip install -r /home/site/wwwroot/requirements.txt
gunicorn --bind=0.0.0.0 --timeout 600 app:app