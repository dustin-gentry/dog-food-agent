FROM python:3.13-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY agent.py ./dog_food_agent/

CMD ["sh", "-c", "exec adk web --host 0.0.0.0 --port \"${PORT:-8080}\" /app"]