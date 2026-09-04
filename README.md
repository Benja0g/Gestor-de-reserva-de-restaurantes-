# Gestor de Reservas de Restaurantes

Proyecto backend desarrollado con Python y Django para gestionar reservas de mesas en un restaurante.

## Requisitos

- Python 3.10 o superior
- Django

## Instalacion

Desde la carpeta principal del proyecto, crea y activa el ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instala Django:

```powershell
pip install django
```

## Ejecucion

Entra a la carpeta que contiene `manage.py` y ejecuta el servidor:

```powershell
cd reservas\Scripts
python manage.py runserver
```

Luego abre en el navegador:

```text
http://127.0.0.1:8000/
```

## Rutas principales

- `/`: pagina de bienvenida del proyecto.
- `/admin/`: panel de administracion de Django.
- Cualquier URL inexistente muestra la pagina personalizada de error 404.

## Estructura principal

```text
reservas/
└── Scripts/
	├── manage.py
	├── motor_django/    # Configuracion principal del proyecto
	└── reservas/        # Aplicacion Django
```

## Estado del proyecto

Actualmente incluye la configuracion inicial de Django, una aplicacion llamada `reservas`, la pagina de bienvenida y el manejo personalizado del error 404. Las funcionalidades de reservas y el modelo de datos se incorporaran en las siguientes etapas.