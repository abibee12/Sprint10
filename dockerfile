# Usa una imagen oficial de Python como imagen principal
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el contenido del directorio actual al contenedor en /app
COPY . /app

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 (ajusta según sea necesario)
EXPOSE 5000

# Define la variable de entorno
ENV FLASK_APP=app.py

# Ejecuta la aplicación cuando se lance el contenedor
CMD ["flask", "run", "--host=0.0.0.0"]
