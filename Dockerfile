FROM python:3.11
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost/ || exit 1
EXPOSE 3000
CMD ["python", "main.py"]
