// =========================================
// SCRIPT - Registro Dinámico de Productos
// AsmoRoot Ventas - Semana 6
// Validaciones dinámicas + CRUD en tiempo real
// =========================================

document.addEventListener('DOMContentLoaded', function () {

    // ---------- Referencias a elementos del DOM ----------
    const formProducto = document.getElementById('formProducto');
    const nombreInput = document.getElementById('nombreProducto');
    const descripcionInput = document.getElementById('descripcionProducto');
    const categoriaSelect = document.getElementById('categoriaProducto');

    const feedbackNombre = document.getElementById('feedbackNombre');
    const feedbackDescripcion = document.getElementById('feedbackDescripcion');
    const feedbackCategoria = document.getElementById('feedbackCategoria');

    const mensajeValidacion = document.getElementById('mensajeValidacion');
    const listaProductos = document.getElementById('listaProductos');
    let sinProductos = document.getElementById('sinProductos');
    const totalProductos = document.getElementById('totalProductos');

    // ---------- Reglas de validación ----------
    const LONGITUD_MIN_NOMBRE = 3;
    const LONGITUD_MIN_DESCRIPCION = 10;

    // Contador de productos registrados
    let contadorProductos = 0;

    // =========================================
    // FUNCIONES DE VALIDACIÓN POR CAMPO
    // =========================================

    // Valida el campo "Nombre del producto"
    function validarNombre() {
        const valor = nombreInput.value.trim();

        if (valor === '') {
            marcarInvalido(nombreInput, feedbackNombre, 'El nombre del producto es obligatorio.');
            return false;
        }

        if (valor.length < LONGITUD_MIN_NOMBRE) {
            marcarInvalido(nombreInput, feedbackNombre, `El nombre debe tener al menos ${LONGITUD_MIN_NOMBRE} caracteres.`);
            return false;
        }

        marcarValido(nombreInput);
        return true;
    }

    // Valida el campo "Descripción"
    function validarDescripcion() {
        const valor = descripcionInput.value.trim();

        if (valor === '') {
            marcarInvalido(descripcionInput, feedbackDescripcion, 'La descripción es obligatoria.');
            return false;
        }

        if (valor.length < LONGITUD_MIN_DESCRIPCION) {
            marcarInvalido(descripcionInput, feedbackDescripcion, `Escribe una descripción más completa (mínimo ${LONGITUD_MIN_DESCRIPCION} caracteres).`);
            return false;
        }

        marcarValido(descripcionInput);
        return true;
    }

    // Valida el campo "Categoría / Tipo"
    function validarCategoria() {
        const valor = categoriaSelect.value;

        if (valor === '') {
            marcarInvalido(categoriaSelect, feedbackCategoria, 'Debes seleccionar una categoría.');
            return false;
        }

        marcarValido(categoriaSelect);
        return true;
    }

    // Valida el formulario completo (usado en el submit)
    function validarFormulario() {
        // Usamos & en vez de && para forzar que las 3 funciones se ejecuten
        // siempre y así se marquen todos los campos, aunque el primero falle.
        const nombreValido = validarNombre();
        const descripcionValida = validarDescripcion();
        const categoriaValida = validarCategoria();

        return nombreValido && descripcionValida && categoriaValida;
    }

    // =========================================
    // FUNCIONES AUXILIARES DE ESTILO (Bootstrap)
    // =========================================

    // Marca un campo como inválido y muestra su mensaje de error
    function marcarInvalido(campo, elementoFeedback, texto) {
        campo.classList.remove('is-valid');
        campo.classList.add('is-invalid');
        if (elementoFeedback) {
            elementoFeedback.textContent = texto;
        }
    }

    // Marca un campo como válido
    function marcarValido(campo) {
        campo.classList.remove('is-invalid');
        campo.classList.add('is-valid');
    }

    // Quita todas las clases de validación (usado tras un registro exitoso)
    function limpiarValidaciones() {
        [nombreInput, descripcionInput, categoriaSelect].forEach(function (campo) {
            campo.classList.remove('is-valid', 'is-invalid');
        });
    }

    // Muestra el mensaje general de éxito o error debajo del formulario
    function mostrarMensaje(texto, tipo) {
        mensajeValidacion.textContent = texto;
        mensajeValidacion.className = `alert alert-${tipo}`;
        mensajeValidacion.classList.remove('d-none');

        setTimeout(function () {
            mensajeValidacion.classList.add('d-none');
        }, 3000);
    }

    // =========================================
    // EVENTOS DE VALIDACIÓN EN TIEMPO REAL
    // =========================================

    // Nombre: validamos mientras escribe y al salir del campo
    nombreInput.addEventListener('input', validarNombre);
    nombreInput.addEventListener('blur', validarNombre);

    // Descripción: validamos mientras escribe y al salir del campo
    descripcionInput.addEventListener('input', validarDescripcion);
    descripcionInput.addEventListener('blur', validarDescripcion);

    // Categoría: validamos al cambiar la selección y al salir del campo
    categoriaSelect.addEventListener('change', validarCategoria);
    categoriaSelect.addEventListener('blur', validarCategoria);

    // =========================================
    // EVENTO SUBMIT DEL FORMULARIO
    // =========================================
    formProducto.addEventListener('submit', function (evento) {
        // Evitamos que la página se recargue
        evento.preventDefault();

        // Validamos todo el formulario antes de registrar
        if (!validarFormulario()) {
            mostrarMensaje('Revisa los campos marcados en rojo antes de continuar.', 'danger');
            return;
        }

        // Obtenemos los valores ya validados
        const nombre = nombreInput.value.trim();
        const descripcion = descripcionInput.value.trim();
        const categoria = categoriaSelect.value;

        // Creamos el producto en el DOM
        crearProducto(nombre, descripcion, categoria);

        // Mostramos mensaje de éxito
        mostrarMensaje('Producto agregado correctamente.', 'success');

        // Limpiamos el formulario y las clases de validación
        formProducto.reset();
        limpiarValidaciones();
    });

    // =========================================
    // CRUD DINÁMICO DE PRODUCTOS
    // =========================================

    // Crea un nuevo producto en el DOM
    function crearProducto(nombre, descripcion, categoria) {

        // Si es el primer producto, quitamos el mensaje "Aún no se han registrado productos"
        if (sinProductos) {
            sinProductos.remove();
            sinProductos = null;
        }

        const columna = document.createElement('div');
        columna.className = 'col-md-6';

        const tarjeta = document.createElement('div');
        tarjeta.className = 'card shadow-sm h-100';

        const cuerpoTarjeta = document.createElement('div');
        cuerpoTarjeta.className = 'card-body';

        const titulo = document.createElement('h5');
        titulo.className = 'card-title';
        titulo.textContent = nombre;

        const badgeCategoria = document.createElement('span');
        badgeCategoria.className = 'badge bg-warning text-dark mb-2';
        badgeCategoria.textContent = categoria;

        const textoDescripcion = document.createElement('p');
        textoDescripcion.className = 'card-text';
        textoDescripcion.textContent = descripcion;

        const botonEliminar = document.createElement('button');
        botonEliminar.className = 'btn btn-outline-danger btn-sm';
        botonEliminar.innerHTML = '<i class="bi bi-trash"></i> Eliminar';

        // Evento click para eliminar el producto
        botonEliminar.addEventListener('click', function () {
            columna.remove();
            contadorProductos--;
            actualizarTotal();

            // Si ya no quedan productos, volvemos a mostrar el mensaje inicial
            if (contadorProductos === 0) {
                const mensajeVacio = document.createElement('p');
                mensajeVacio.className = 'text-muted';
                mensajeVacio.id = 'sinProductos';
                mensajeVacio.textContent = 'Aún no se han registrado productos.';
                listaProductos.appendChild(mensajeVacio);
                sinProductos = mensajeVacio;
            }
        });

        cuerpoTarjeta.appendChild(titulo);
        cuerpoTarjeta.appendChild(badgeCategoria);
        cuerpoTarjeta.appendChild(textoDescripcion);
        cuerpoTarjeta.appendChild(botonEliminar);
        tarjeta.appendChild(cuerpoTarjeta);
        columna.appendChild(tarjeta);

        listaProductos.appendChild(columna);

        contadorProductos++;
        actualizarTotal();
    }

    // Actualiza el total de registros en pantalla
    function actualizarTotal() {
        totalProductos.textContent = contadorProductos;
    }

});