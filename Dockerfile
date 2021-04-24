FROM python:3.9-slim
LABEL maintainer="Lauro Gomes <laurobmb@gmail.com>"

COPY requirements.txt /
RUN pip install pip --upgrade && \
    pip install -r requirements.txt
ADD app.py /app.py

EXPOSE 8000
CMD [ "python","app.py" ]
