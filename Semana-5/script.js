// =========================================
// SCRIPT - Registro Dinámico de Productos
// AsmoRoot Ventas
// =========================================

// Esperamos a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function () {

    // Referencias a elementos del DOM
    const formProducto = document.getElementById('formProducto');
    const nombreInput = document.getElementById('nombreProducto');
    const descripcionInput = document.getElementById('descripcionProducto');
    const categoriaInput = document.getElementById('categoriaProducto');
    const mensajeValidacion = document.getElementById('mensajeValidacion');
    const listaProductos = document.getElementById('listaProductos');
    const sinProductos = document.getElementById('sinProductos');
    const totalProductos = document.getElementById('totalProductos');

    // Contador de productos registrados
    let contadorProductos = 0;

    // Capturamos el evento submit del formulario
    formProducto.addEventListener('submit', function (evento) {
        // Evitamos que la página se recargue
        evento.preventDefault();

        // Obtenemos los valores de los campos (sin espacios extra)
        const nombre = nombreInput.value.trim();
        const descripcion = descripcionInput.value.trim();
        const categoria = categoriaInput.value.trim();

        // Validamos que ningún campo esté vacío
        if (nombre === '' || descripcion === '' || categoria === '') {
            mostrarMensaje('Por favor, completa todos los campos antes de continuar.', 'danger');
            return;
        }

        // Si la validación es correcta, creamos el producto
        crearProducto(nombre, descripcion, categoria);

        // Mostramos mensaje de éxito
        mostrarMensaje('Producto agregado correctamente.', 'success');

        // Limpiamos el formulario
        formProducto.reset();
    });

    // Función para mostrar mensajes dinámicos de validación
    function mostrarMensaje(texto, tipo) {
        mensajeValidacion.textContent = texto;
        mensajeValidacion.className = `alert alert-${tipo}`;
        mensajeValidacion.classList.remove('d-none');

        // Ocultamos el mensaje automáticamente después de 3 segundos
        setTimeout(function () {
            mensajeValidacion.classList.add('d-none');
        }, 3000);
    }

    // Función para crear un nuevo producto en el DOM
    function crearProducto(nombre, descripcion, categoria) {

        // Si es el primer producto, ocultamos el mensaje "Aún no se han registrado productos"
        if (sinProductos) {
            sinProductos.remove();
        }

        // Creamos la columna (col) que contendrá la tarjeta del producto
        const columna = document.createElement('div');
        columna.className = 'col-md-6';

        // Creamos la tarjeta (card) con clases de Bootstrap
        const tarjeta = document.createElement('div');
        tarjeta.className = 'card shadow-sm h-100';

        // Cuerpo de la tarjeta
        const cuerpoTarjeta = document.createElement('div');
        cuerpoTarjeta.className = 'card-body';

        // Título del producto
        const titulo = document.createElement('h5');
        titulo.className = 'card-title';
        titulo.textContent = nombre;

        // Categoría (badge de Bootstrap)
        const badgeCategoria = document.createElement('span');
        badgeCategoria.className = 'badge bg-warning text-dark mb-2';
        badgeCategoria.textContent = categoria;

        // Descripción del producto
        const textoDescripcion = document.createElement('p');
        textoDescripcion.className = 'card-text';
        textoDescripcion.textContent = descripcion;

        // Botón para eliminar el producto
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
            }
        });

        // Armamos la tarjeta agregando cada elemento (appendChild)
        cuerpoTarjeta.appendChild(titulo);
        cuerpoTarjeta.appendChild(badgeCategoria);
        cuerpoTarjeta.appendChild(textoDescripcion);
        cuerpoTarjeta.appendChild(botonEliminar);
        tarjeta.appendChild(cuerpoTarjeta);
        columna.appendChild(tarjeta);

        // Agregamos la tarjeta al contenedor principal de productos
        listaProductos.appendChild(columna);

        // Actualizamos el contador de productos
        contadorProductos++;
        actualizarTotal();
    }

    // Función para actualizar el total de registros en pantalla
    function actualizarTotal() {
        totalProductos.textContent = contadorProductos;
    }

});