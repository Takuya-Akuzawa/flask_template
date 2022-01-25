import os
wsgi_app = 'flask_package:create_app()'
bind = '0.0.0.0:' + str(os.getenv('PORT', 5050))
proc_name = 'Infrastructure-gunicorn-Flask'
workers = 1
reload = True