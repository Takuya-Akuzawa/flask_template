import os

bind = '0.0.0.0:' + str(os.getenv('PORT', 5050))
proc_name = 'Infrastructure-gunicorn-Flask'
workers = 1
reload = True