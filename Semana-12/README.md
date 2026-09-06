# Proyecto Integrador U3 - Avance 11/16
## Desarrollo de Aplicaciones Web - Semana 11

### Descripción del Proyecto
Este proyecto corresponde al avance de la Semana 11 de la asignatura Desarrollo de Aplicaciones Web. En esta etapa se incorporaron formularios web con validación del lado del servidor utilizando **Flask-WTF** y **WTForms**, organizados en una carpeta `forms` separada por módulo. Se implementó protección CSRF, validación de campos obligatorios, mensajes de error y procesamiento condicional de datos.

---

### Estructura del Proyecto
```text
Semana-11/
│
├── app.py
├── requirements.txt
├── README.md
│
├── forms/
│   ├── __init__.py
│   ├── producto_form.py
│   ├── cliente_form.py
│   ├── proveedor_form.py
│   └── facturacion_form.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── productos.html
│   ├── formulario_producto.html
│   ├── clientes.html
│   ├── formulario_cliente.html
│   ├── proveedores.html
│   ├── formulario_proveedor.html
│   ├── facturacion.html
│   ├── formulario_facturacion.html
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
```

---

### Tecnologías Utilizadas
- Python 3.14
- Flask 3.0.00
- Flask-WTF
- WTForms
- Jinja2
- Bootstrap 5.3

---

### Nuevas Funcionalidades - Semana 11
- Carpeta `forms/` con clases de formulario por módulo
- Formularios que heredan de `FlaskForm`
- Validadores `DataRequired()`, `Length()`, `Email()`, `NumberRange()`
- Protección CSRF mediante `form.hidden_tag()` y `SECRET_KEY`
- Rutas con métodos GET y POST
- Validación con `form.validate_on_submit()`
- Mensajes de error por campo en rojo
- Mensajes flash de éxito tras registro exitoso
- Almacenamiento temporal en listas de Python (sin base de datos)

---

### Rutas Disponibles
| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Página principal |
| `/productos` | GET | Listado de productos |
| `/productos/nuevo` | GET / POST | Formulario de nuevo producto |
| `/clientes` | GET | Listado de clientes |
| `/clientes/nuevo` | GET / POST | Formulario de nuevo cliente |
| `/proveedores` | GET | Listado de proveedores |
| `/proveedores/nuevo` | GET / POST | Formulario de nuevo proveedor |
| `/facturacion` | GET | Módulo de facturación |
| `/facturacion/nueva` | GET / POST | Formulario de nueva factura |

---

### Cómo ejecutar el proyecto
```bash
# Activar entorno virtual
venv\Scripts\activate

# Instalar dependencias
py -m pip install -r requirements.txt

# Ejecutar la aplicación
py app.py
```

Abrir en el navegador: `http://127.0.0.1:5000`

---

### Estudiante
**Carlos Daniel Castillo Cabrera**  
Desarrollo de Aplicaciones Web  
Universidad Estatal Amazónica - 2026