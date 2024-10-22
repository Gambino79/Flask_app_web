#!/usr/bin/python
import sys
import logging

activate_this = "/var/www/webapp/venv/bin/activate_this.py"
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/webapp')

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from main import app as application
