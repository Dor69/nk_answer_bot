FROM python:3.11
WORKDIR /app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip3 install -r ./app/requirements.txt
COPY . .
CMD ["python", "main.py"]

