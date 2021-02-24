#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flask_blog/")

from flask_blog import app as application
application.secret_key = 'winter is coming'

