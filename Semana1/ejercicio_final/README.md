Mi Primera API FastAPI - Bootcamp

👤 Desarrollador: Camilo Andrés León Roldán 📧 Correo: camilo-leon@users.noreply.github.com 🔒 Privacidad: Email configurado según buenas prácticas de GitHub 📅 Fecha de creación: 2025-08-14 22:15:00 📂 Ubicación del proyecto: /c/Users/Aprendiz/desarrollo-personal/camilo-leon-bootcamp/mi-primera-api-fastapi 💻 Equipo de trabajo: SENA – ADSO Ficha 3147246

🔧 Configuración Local Este proyecto está configurado para trabajo en equipo compartido:

Entorno virtual aislado: venv-personal/ Configuración Git local: Solo para este proyecto Dependencias independientes: No afecta otras instalaciones

🚀 Instalación y Ejecución

1. Activar entorno virtual
source venv-camilo/bin/activate # Linux/Mac venv-camilo\Scripts\activate # Windows

2. Instalar dependencias
pip install -r requirements.txt

3. Ejecutar servidor en modo desarrollo
uvicorn main:app --reload --port 8000

📝 Notas del Desarrollador

Git: Configurado únicamente para este proyecto. Correo: Uso de email privado de GitHub para proteger información personal. Entorno virtual: Todas las librerías instaladas en venv-camilo/. Puerto: Por defecto 8000, modificable si existe conflicto. Estado actual: Semana 1 – API básica con validación y type hints.

🛠️ Resolución de Problemas No se activa el entorno virtual: rm -rf venv-camilo && python -m venv venv-camilo Puerto en uso: Cambiar el valor de --port en el comando de Uvicorn. Git no responde: Revisar configuración local con:

git config user.name git config user.email

Cambiar correo en Git: Configurar desde GitHub → Settings → Emails.

📌 ¿Qué hace esta API?

Es una API inicial creada con FastAPI, que incluye validación automática de datos y anotaciones de tipo (type hints) para mayor claridad y robustez.



▶️ Cómo ejecutar rápidamente pip install fastapi pydantic uvicorn uvicorn main:app --reload
   
