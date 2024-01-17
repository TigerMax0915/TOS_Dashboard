FROM python:3.10

WORKDIR /home/

RUN git clone https://github.com/TigerMax0915/TOS_Dashboard.git

RUN echo "SECRET_KEY='django-insecure-i6iz#rpdznl@79&wy02_kt!qcdbqb2b2!c@ypgz0xx*$exl4^z'
DEBUG=True" > .env

WORKDIR /home/TOS_Dashboard

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python" "manage.py", "runserver", "0.0.0.0:8000"]