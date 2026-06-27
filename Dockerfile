FROM python:3.11

WORKDIR /app

# install dependencies
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy backend + frontend
COPY backend /app/backend
COPY frontend /app/frontend

# set python path
ENV PYTHONPATH=/app/backend

EXPOSE 8080

CMD sh -c "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"