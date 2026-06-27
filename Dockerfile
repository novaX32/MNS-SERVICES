FROM python:3.11

WORKDIR /app/backend

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

EXPOSE 8000

ENV PYTHONPATH=/app/backend

CMD sh -c "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"