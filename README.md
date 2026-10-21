# Gestor de Reservas de Restaurantes

Proyecto backend desarrollado con Python, Django y Django REST Framework para gestionar restaurantes, sucursales, clientes, mesas, reservas y pagos.

## Requisitos

- Python 3.10 o superior
- Django
- Django REST Framework
- MySQL
- WampServer
- python-decouple

## Instalación

Desde la carpeta principal del proyecto, crea y activa el ambiente virtual:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Instala las dependencias:

pip install -r requirements.txt

## Configuración

Crear un archivo llamado:

.env

Con el siguiente contenido:

SECRET_KEY=tu_clave_secreta

DB_NAME=gestor_reservas_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306

## Base de Datos

Crear la base de datos ejecutando el archivo:

crear_bd.sql

O ejecutando:

CREATE DATABASE gestor_reservas_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

## Migraciones

Ejecutar:

python manage.py makemigrations
python manage.py migrate

## Crear Superusuario

python manage.py createsuperuser

## Ejecución

Desde la carpeta principal del proyecto ejecutar:

python manage.py runserver

Luego abrir en el navegador:

http://127.0.0.1:8000/

## Panel de Administración

http://127.0.0.1:8000/admin/

## API REST

http://127.0.0.1:8000/api/

## Endpoints Disponibles

/api/restaurantes/
/api/sucursales/
/api/clientes/
/api/mesas/
/api/estados-reserva/
/api/reservas/
/api/metodos-pago/
/api/pagos/

## Operaciones CRUD

La API permite realizar las siguientes operaciones:

- GET
- POST
- PUT
- PATCH
- DELETE

## Modelos del Sistema

- Restaurante
- Sucursal
- Cliente
- Mesa
- EstadoReserva
- Reserva
- MetodoPago
- Pago

## Estructura Principal

reservas/
├── .env
├── manage.py
├── requirements.txt
├── crear_bd.sql
├── motor_django/
└── restaurante/

## Estado del Proyecto

Actualmente el sistema cuenta con:

- Base de datos MySQL.
- API REST con Django REST Framework.
- Gestión de restaurantes.
- Gestión de sucursales.
- Gestión de clientes.
- Gestión de mesas.
- Gestión de reservas.
- Gestión de pagos.
- Panel de administración de Django.
- Operaciones CRUD completas mediante API REST.

## Autor

Benjamin Andrés Baraona González

Proyecto desarrollado para la evaluación de Backend utilizando Django, Django REST Framework y MySQL.