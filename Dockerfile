FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /app

COPY ./flask_package /app/flask_package
COPY ./requirements.txt ./
COPY ./uwsgi.ini ./
COPY ./prestart.sh ./

RUN pip install --no-cache-dir -r requirements.txt

# tiangolo/uwsgi-nginx-flask custom config
ENV STATIC_PATH=/app/flask_package/static/
RUN rm ./main.py

# own flask package environment config
ENV TZ=Asia/Tokyo
ENV FLASK_APP_ENV=development
ENV FLASK_APP="flask_package:create_app()"