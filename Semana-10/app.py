from flask import Flask, render_template

app = Flask(__name__)

# Ruta 1: Página Principal Informativa (Index)
@app.route('/')
def index():
    empresa_info = {
        "nombre": "Sistemas y Soluciones Tecnológicas",
        "eslogan": "Innovación y Desarrollo Web A Medida",
        "descripcion": "Plataforma de gestión integral para la administración de inventarios, clientes, proveedores y facturación.",
        "servicios": ["Desarrollo Web", "Soporte Técnico", "Mantenimiento de Software", "Optimización de Sistemas"]
    }
    return render_template('index.html', empresa=empresa_info)

# Ruta 2: Módulo de Productos
@app.route('/productos')
def productos():
    lista_productos = [
        {"id": 1, "nombre": "Teclado Mecánico RGB", "precio": 45.00, "stock": 12, "categoria": "Periféricos"},
        {"id": 2, "nombre": "Monitor Gamer 24 pulgadas", "precio": 180.50, "stock": 0, "categoria": "Pantallas"},
        {"id": 3, "nombre": "Ratón Inalámbrico Ergonómico", "precio": 25.00, "stock": 8, "categoria": "Periféricos"},
        {"id": 4, "nombre": "Disco Duro SSD 1TB", "precio": 75.00, "stock": 5, "categoria": "Almacenamiento"},
        {"id": 5, "nombre": "Memoria RAM 16GB DDR4", "precio": 55.00, "stock": 0, "categoria": "Componentes"}
    ]
    return render_template('productos.html', productos=lista_productos)

# Ruta 3: Módulo de Clientes
@app.route('/clientes')
def clientes():
    lista_clientes = [
        {"id": 101, "nombre": "Carlos Mendoza", "email": "carlos.mendoza@email.com", "telefono": "0991234567", "activo": True},
        {"id": 102, "nombre": "Ana Rodríguez", "email": "ana.rodriguez@email.com", "telefono": "0987654321", "activo": True},
        {"id": 103, "nombre": "Luis Morales", "email": "luis.morales@email.com", "telefono": "0998887766", "activo": False},
        {"id": 104, "nombre": "María López", "email": "maria.lopez@email.com", "telefono": "0971122334", "activo": True}
    ]
    return render_template('clientes.html', clientes=lista_clientes)

# Ruta 4: Módulo de Proveedores
@app.route('/proveedores')
def proveedores():
    lista_proveedores = [
        {"empresa": "TechImport S.A.", "contacto": "Juan Pérez", "telefono": "022345678", "ciudad": "Quito"},
        {"empresa": "Distribuidora del Norte", "contacto": "Sonia Gómez", "telefono": "042987654", "ciudad": "Guayaquil"},
        {"empresa": "Global Electronics", "contacto": "Pedro Ramírez", "telefono": "072111222", "ciudad": "Cuenca"}
    ]
    return render_template('proveedores.html', proveedores=lista_proveedores)

# Ruta 5: Módulo de Facturación
@app.route('/facturacion')
def facturacion():
    factura_ejemplo = {
        "numero": "FAC-0001",
        "cliente": "Carlos Mendoza",
        "fecha": "2026-08-23",
        "detalles": [
            {"descripcion": "Teclado Mecánico RGB", "cantidad": 2, "precio_unitario": 45.00},
            {"descripcion": "Ratón Inalámbrico", "cantidad": 1, "precio_unitario": 25.00}
        ],
        "subtotal": 115.00,
        "iva": 13.80,
        "total": 128.80,
        "pagada": True
    }
    return render_template('facturacion.html', factura=factura_ejemplo)

if __name__ == '__main__':
    app.run(debug=True)