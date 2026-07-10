FROM  python:3.12-slim              # Verwendet ein schlankes Python-Image als Grundlage.
WORKDIR /app                        # Legt das Arbeitsverzeichnis im Container fest.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt     # Installiert alle benötigten Python-Abhängigkeiten.
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port", "8000" ]
