
# Verwendet ein schlankes Python-Image als Grundlage.
FROM python:3.12-slim              
# Legt den Arbeitsordner innerhalb des Containers fest.
WORKDIR /app                       
# Kopiert die Liste der benötigten Python-Pakete.
COPY requirements.txt .
# Installiert alle Abhängigkeiten für die FastAPI-Anwendung.
RUN pip install --no-cache-dir -r requirements.txt  
# Kopiert den gesamten Projektcode in den Container.
COPY . .   
# Gibt den Port der FastAPI-Anwendung bekannt.
EXPOSE 8000
# Startet die FastAPI-Anwendung beim Container-Start.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port", "8000" ]
