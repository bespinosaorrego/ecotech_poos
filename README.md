# EcoTech 

Trabajo de la Evaluación Sumativa 3 de Programación Orientada a Objeto Seguro.

La idea fue tomar lo que ya tenía de EcoTech y agregarle consultas a APIs externas (dólar y clima), login con contraseña encriptada, y que los datos quedaran guardados en una base local aunque cerremos el programa. Además, se implementaron roles (Administrador y Funcionario) con sus respectivas restricciones de seguridad


## Antes de ejecutar

Necesitas Python instalado y conexión a internet (para las APIs)

### 1.Crear el entorno virtual

En la carpeta de ecotech_benjamin

Click derecho y mostrar mas opciones-Open git bash here

py -m venv .venv
.venv\Scripts\Activate

# Instalar dependencias

pip install -r requirements.txt

## INSTALAR BCRYPT

pip install bcrypt

# Crear el archivo .env

copy .env.example .env

# Crear las tablas

python -m src.persistencia.semilla_bd

# Ejecutar

python main.py

## SI PASA CUALQUIER COSA Y QUIERES BORRAR LA BASE DE DATOS Y LIMPIAR

Remove-Item ecotech.db


### CUENTAS PARA PROBAR Admin/Empleado

Admin
Admin2025!
---------------
ana_torres
Ana2025!