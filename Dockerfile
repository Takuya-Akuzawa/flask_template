FROM python:3.7

WORKDIR /usr/src/app

COPY ./flask_package /usr/src/app/flask_package
COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/bash"]