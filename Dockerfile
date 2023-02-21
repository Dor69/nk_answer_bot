FROM python:3.7
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN chmd 755 .
COPY . .
