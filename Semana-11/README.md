# Proyecto Integrador U3 - Avance 10/16
## Desarrollo de Aplicaciones Web - Semana 10

### Descripción del Proyecto
Este proyecto corresponde al avance de la Semana 10 de la asignatura Desarrollo de Aplicaciones Web. En esta etapa se implementó la generación de contenido dinámico mediante el motor de plantillas **Jinja2** integrado con **Flask**, aplicando variables, estructuras de control (`{% for %}`, `{% if %}`), filtros y componentes reutilizables.

El sistema simula la gestión integral de una plataforma comercial organizada en módulos de Inicio, Productos, Clientes, Proveedores y Facturación.

---

### Estructura del Proyecto
```text
Semana-10/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── productos.html
│   ├── clientes.html
│   ├── proveedores.html
│   ├── facturacion.html
│   │
│   └── components/
│       ├── navbar.html
│       └── footer.html
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── img/