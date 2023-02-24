FROM python:3.11
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
HEALTHCHECK --interval=30s --timeout=3s \
CMD ["python", "main.py"]
