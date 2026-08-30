from flask import Flask, render_template, redirect, url_for, flash
from forms.producto_form import ProductoForm
from forms.cliente_form import ClienteForm
from forms.proveedor_form import ProveedorForm
from forms.facturacion_form import FacturacionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asmoroot-secret-key-2026'

# Almacenamiento temporal en memoria (sin base de datos aún)
productos_registrados = []
clientes_registrados = []
proveedores_registrados = []
facturas_registradas = []

# ===================== RUTAS SEMANA 10 (sin cambios) =====================

@app.route('/')
def index():
    empresa_info = {
        "nombre": "Sistemas y Soluciones Tecnológicas",
        "eslogan": "Innovación y Desarrollo Web A Medida",
        "descripcion": "Plataforma de gestión integral para la administración de inventarios, clientes, proveedores y facturación.",
        "servicios": ["Desarrollo Web", "Soporte Técnico", "Mantenimiento de Software", "Optimización de Sistemas"]
    }
    return render_template('index.html', empresa=empresa_info)

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

@app.route('/clientes')
def clientes():
    lista_clientes = [
        {"id": 101, "nombre": "Carlos Mendoza", "email": "carlos.mendoza@email.com", "telefono": "0991234567", "activo": True},
        {"id": 102, "nombre": "Ana Rodríguez", "email": "ana.rodriguez@email.com", "telefono": "0987654321", "activo": True},
        {"id": 103, "nombre": "Luis Morales", "email": "luis.morales@email.com", "telefono": "0998887766", "activo": False},
        {"id": 104, "nombre": "María López", "email": "maria.lopez@email.com", "telefono": "0971122334", "activo": True}
    ]
    return render_template('clientes.html', clientes=lista_clientes)

@app.route('/proveedores')
def proveedores():
    lista_proveedores = [
        {"empresa": "TechImport S.A.", "contacto": "Juan Pérez", "telefono": "022345678", "ciudad": "Quito"},
        {"empresa": "Distribuidora del Norte", "contacto": "Sonia Gómez", "telefono": "042987654", "ciudad": "Guayaquil"},
        {"empresa": "Global Electronics", "contacto": "Pedro Ramírez", "telefono": "072111222", "ciudad": "Cuenca"}
    ]
    return render_template('proveedores.html', proveedores=lista_proveedores)

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

# ===================== RUTAS SEMANA 11 (formularios nuevos) =====================

@app.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        producto = {
            "nombre": form.nombre.data,
            "categoria": form.categoria.data,
            "precio": form.precio.data,
            "stock": form.stock.data
        }
        productos_registrados.append(producto)
        flash('Producto registrado correctamente.', 'success')
        return redirect(url_for('productos'))
    return render_template('formulario_producto.html', form=form, titulo='Nuevo Producto')

@app.route('/clientes/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = {
            "nombre": form.nombre.data,
            "email": form.email.data,
            "telefono": form.telefono.data,
            "activo": form.activo.data
        }
        clientes_registrados.append(cliente)
        flash('Cliente registrado correctamente.', 'success')
        return redirect(url_for('clientes'))
    return render_template('formulario_cliente.html', form=form, titulo='Nuevo Cliente')

@app.route('/proveedores/nuevo', methods=['GET', 'POST'])
def nuevo_proveedor():
    form = ProveedorForm()
    if form.validate_on_submit():
        proveedor = {
            "empresa": form.empresa.data,
            "contacto": form.contacto.data,
            "telefono": form.telefono.data,
            "ciudad": form.ciudad.data
        }
        proveedores_registrados.append(proveedor)
        flash('Proveedor registrado correctamente.', 'success')
        return redirect(url_for('proveedores'))
    return render_template('formulario_proveedor.html', form=form, titulo='Nuevo Proveedor')

@app.route('/facturacion/nueva', methods=['GET', 'POST'])
def nueva_factura():
    form = FacturacionForm()
    if form.validate_on_submit():
        factura = {
            "numero": form.numero.data,
            "cliente": form.cliente.data,
            "fecha": form.fecha.data,
            "total": form.total.data
        }
        facturas_registradas.append(factura)
        flash('Factura registrada correctamente.', 'success')
        return redirect(url_for('facturacion'))
    return render_template('formulario_facturacion.html', form=form, titulo='Nueva Factura')

if __name__ == '__main__':
    app.run(debug=True)