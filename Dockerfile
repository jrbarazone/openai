# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y el código fuente al contenedor
COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Especifica el comando para ejecutar el asistente de IA
CMD ["python", "main.py"]
