from os import environ
from subprocess import Popen

PORT = environ.get('PORT',8080)
Popen(f"gunicorn server:app --bind 0.0.0.0:{PORT} --worker-class gevent", shell=True)
