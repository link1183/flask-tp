FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5556

ENV FLASK_APP=run_mon_app.py
ENV FLASK_ENV=development

RUN mkdir -p /app/database

CMD ["python", "run_mon_app.py"]
