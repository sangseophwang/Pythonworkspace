FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip3 install flask
RUN chmod +x /app/app.py
CMD ["python3", "app.py"]