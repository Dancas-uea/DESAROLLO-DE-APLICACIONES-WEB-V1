from flask import Flask, render_template, redirect, url_for, flash, session, request
import sqlite3
import os
from forms.producto_form import ProductoForm
from forms.cliente_form import ClienteForm
from forms.proveedor_form import ProveedorForm
from forms.facturacion_form import FacturacionForm
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asmoroot-secret-key-2026'

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'ferreteria.db')

# ===================== BASE DE DATOS =====================
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            activo INTEGER NOT NULL DEFAULT 1
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proveedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa TEXT NOT NULL,
            contacto TEXT NOT NULL,
            telefono TEXT NOT NULL,
            ciudad TEXT NOT NULL
        )
    ''')

    # Usuario admin por defecto
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO usuarios (username, password) VALUES (?, ?)",
            ('admin', 'admin123')
        )

    conn.commit()
    conn.close()

init_db()

# ===================== DECORADOR LOGIN =====================
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario' not in session:
            flash('Debes iniciar sesión primero.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# ===================== LOGIN / LOGOUT =====================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['usuario'] = username
            flash(f'Bienvenido, {username}.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('login'))

# ===================== INDEX =====================
@app.route('/')
@login_required
def index():
    empresa_info = {
        "nombre": "Sistemas y Soluciones Tecnológicas",
        "eslogan": "Innovación y Desarrollo Web A Medida",
        "descripcion": "Plataforma de gestión integral para la administración de inventarios, clientes, proveedores y facturación.",
        "servicios": ["Desarrollo Web", "Soporte Técnico", "Mantenimiento de Software", "Optimización de Sistemas"]
    }
    return render_template('index.html', empresa=empresa_info)

# ===================== PRODUCTOS =====================
@app.route('/productos')
@login_required
def productos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, categoria, precio, stock FROM productos')
    lista_productos = cursor.fetchall()
    conn.close()
    return render_template('productos.html', productos=lista_productos)

@app.route('/productos/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)',
            (form.nombre.data, form.categoria.data, form.precio.data, form.stock.data)
        )
        conn.commit()
        conn.close()
        flash('Producto registrado correctamente.', 'success')
        return redirect(url_for('productos'))
    return render_template('formulario_producto.html', form=form, titulo='Nuevo Producto')

@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_producto(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, categoria, precio, stock FROM productos WHERE id=?', (id,))
    p = cursor.fetchone()
    conn.close()
    if not p:
        flash('Producto no encontrado.', 'danger')
        return redirect(url_for('productos'))
    form = ProductoForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE productos SET nombre=?, categoria=?, precio=?, stock=? WHERE id=?',
            (form.nombre.data, form.categoria.data, form.precio.data, form.stock.data, id)
        )
        conn.commit()
        conn.close()
        flash('Producto actualizado correctamente.', 'success')
        return redirect(url_for('productos'))
    # Prellenar formulario
    form.nombre.data = p[1]
    form.categoria.data = p[2]
    form.precio.data = p[3]
    form.stock.data = p[4]
    return render_template('formulario_producto.html', form=form, titulo='Editar Producto')

@app.route('/productos/eliminar/<int:id>')
@login_required
def eliminar_producto(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM productos WHERE id=?', (id,))
    conn.commit()
    conn.close()
    flash('Producto eliminado.', 'warning')
    return redirect(url_for('productos'))

# ===================== CLIENTES =====================
@app.route('/clientes')
@login_required
def clientes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, email, telefono, activo FROM clientes')
    lista_clientes = cursor.fetchall()
    conn.close()
    return render_template('clientes.html', clientes=lista_clientes)

@app.route('/clientes/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO clientes (nombre, email, telefono, activo) VALUES (?, ?, ?, ?)',
            (form.nombre.data, form.email.data, form.telefono.data, 1 if form.activo.data else 0)
        )
        conn.commit()
        conn.close()
        flash('Cliente registrado correctamente.', 'success')
        return redirect(url_for('clientes'))
    return render_template('formulario_cliente.html', form=form, titulo='Nuevo Cliente')

@app.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_cliente(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, email, telefono, activo FROM clientes WHERE id=?', (id,))
    c = cursor.fetchone()
    conn.close()
    if not c:
        flash('Cliente no encontrado.', 'danger')
        return redirect(url_for('clientes'))
    form = ClienteForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE clientes SET nombre=?, email=?, telefono=?, activo=? WHERE id=?',
            (form.nombre.data, form.email.data, form.telefono.data, 1 if form.activo.data else 0, id)
        )
        conn.commit()
        conn.close()
        flash('Cliente actualizado correctamente.', 'success')
        return redirect(url_for('clientes'))
    form.nombre.data = c[1]
    form.email.data = c[2]
    form.telefono.data = c[3]
    form.activo.data = bool(c[4])
    return render_template('formulario_cliente.html', form=form, titulo='Editar Cliente')

@app.route('/clientes/eliminar/<int:id>')
@login_required
def eliminar_cliente(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clientes WHERE id=?', (id,))
    conn.commit()
    conn.close()
    flash('Cliente eliminado.', 'warning')
    return redirect(url_for('clientes'))

# ===================== PROVEEDORES =====================
@app.route('/proveedores')
@login_required
def proveedores():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, empresa, contacto, telefono, ciudad FROM proveedores')
    lista_proveedores = cursor.fetchall()
    conn.close()
    return render_template('proveedores.html', proveedores=lista_proveedores)

@app.route('/proveedores/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_proveedor():
    form = ProveedorForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO proveedores (empresa, contacto, telefono, ciudad) VALUES (?, ?, ?, ?)',
            (form.empresa.data, form.contacto.data, form.telefono.data, form.ciudad.data)
        )
        conn.commit()
        conn.close()
        flash('Proveedor registrado correctamente.', 'success')
        return redirect(url_for('proveedores'))
    return render_template('formulario_proveedor.html', form=form, titulo='Nuevo Proveedor')

@app.route('/proveedores/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_proveedor(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, empresa, contacto, telefono, ciudad FROM proveedores WHERE id=?', (id,))
    p = cursor.fetchone()
    conn.close()
    if not p:
        flash('Proveedor no encontrado.', 'danger')
        return redirect(url_for('proveedores'))
    form = ProveedorForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE proveedores SET empresa=?, contacto=?, telefono=?, ciudad=? WHERE id=?',
            (form.empresa.data, form.contacto.data, form.telefono.data, form.ciudad.data, id)
        )
        conn.commit()
        conn.close()
        flash('Proveedor actualizado correctamente.', 'success')
        return redirect(url_for('proveedores'))
    form.empresa.data = p[1]
    form.contacto.data = p[2]
    form.telefono.data = p[3]
    form.ciudad.data = p[4]
    return render_template('formulario_proveedor.html', form=form, titulo='Editar Proveedor')

@app.route('/proveedores/eliminar/<int:id>')
@login_required
def eliminar_proveedor(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM proveedores WHERE id=?', (id,))
    conn.commit()
    conn.close()
    flash('Proveedor eliminado.', 'warning')
    return redirect(url_for('proveedores'))

# ===================== FACTURACIÓN =====================
@app.route('/facturacion')
@login_required
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

@app.route('/facturacion/nueva', methods=['GET', 'POST'])
@login_required
def nueva_factura():
    form = FacturacionForm()
    if form.validate_on_submit():
        flash('Factura registrada correctamente.', 'success')
        return redirect(url_for('facturacion'))
    return render_template('formulario_facturacion.html', form=form, titulo='Nueva Factura')

if __name__ == '__main__':
    app.run(debug=True)