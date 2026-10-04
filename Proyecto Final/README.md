# Proyecto Final - Desarrollo de Aplicaciones Web
## Sistema de Gestión Integral - AsmoRoot

### Descripción del Proyecto
Este proyecto corresponde al Proyecto Final de la asignatura Desarrollo de Aplicaciones Web. El sistema es una aplicación web completa desarrollada con Flask que integra autenticación de usuarios, operaciones CRUD completas y persistencia de datos mediante SQLite. El sistema permite gestionar productos, clientes, proveedores y facturación desde una interfaz web responsiva construida con Bootstrap.

---

### Tecnologías Utilizadas
- Python 3.14
- Flask 3.0.0
- Flask-WTF
- WTForms
- SQLite3
- Jinja2
- Bootstrap 5.3
- HTML5 / CSS3 / JavaScript

---

### Estructura del Proyecto
```text
Proyecto Final/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── ferreteria.db
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
│   ├── login.html
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

### Funcionalidades Implementadas

#### Autenticación
- Login con usuario y contraseña
- Protección de rutas mediante sesiones Flask
- Logout con cierre de sesión
- Redirección automática al login si no hay sesión activa

#### CRUD Completo - Productos
- Crear nuevo producto
- Listar todos los productos
- Editar producto existente
- Eliminar producto

#### CRUD Completo - Clientes
- Crear nuevo cliente
- Listar todos los clientes
- Editar cliente existente
- Eliminar cliente

#### CRUD Completo - Proveedores
- Crear nuevo proveedor
- Listar todos los proveedores
- Editar proveedor existente
- Eliminar proveedor

#### Facturación
- Visualización de facturas
- Formulario de nueva factura con validación

---

### Base de Datos SQLite
El sistema utiliza una base de datos local `ferreteria.db` con las siguientes tablas relacionadas:

| Tabla | Campos |
|-------|--------|
| usuarios | id, username, password |
| productos | id, nombre, categoria, precio, stock |
| clientes | id, nombre, email, telefono, activo |
| proveedores | id, empresa, contacto, telefono, ciudad |

---

### Rutas Disponibles

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/login` | GET / POST | Inicio de sesión |
| `/logout` | GET | Cerrar sesión |
| `/` | GET | Página principal |
| `/productos` | GET | Listado de productos |
| `/productos/nuevo` | GET / POST | Crear producto |
| `/productos/editar/<id>` | GET / POST | Editar producto |
| `/productos/eliminar/<id>` | GET | Eliminar producto |
| `/clientes` | GET | Listado de clientes |
| `/clientes/nuevo` | GET / POST | Crear cliente |
| `/clientes/editar/<id>` | GET / POST | Editar cliente |
| `/clientes/eliminar/<id>` | GET | Eliminar cliente |
| `/proveedores` | GET | Listado de proveedores |
| `/proveedores/nuevo` | GET / POST | Crear proveedor |
| `/proveedores/editar/<id>` | GET / POST | Editar proveedor |
| `/proveedores/eliminar/<id>` | GET | Eliminar proveedor |
| `/facturacion` | GET | Módulo de facturación |
| `/facturacion/nueva` | GET / POST | Nueva factura |

---

### Credenciales de Acceso
| Usuario | Contraseña |
|---------|------------|
| admin | admin123 |

---

### Cómo ejecutar el proyecto
```bash
# 1. Navegar a la carpeta del proyecto
cd "Proyecto Final"

# 2. Activar el entorno virtual
venv\Scripts\activate

# 3. Instalar dependencias
py -m pip install -r requirements.txt

# 4. Ejecutar la aplicación
py app.py
```

Abrir en el navegador: `http://127.0.0.1:5000`

---

### Estudiante
**Carlos Daniel Castillo Cabrera**
Desarrollo de Aplicaciones Web
Universidad Estatal Amazónica - 2026