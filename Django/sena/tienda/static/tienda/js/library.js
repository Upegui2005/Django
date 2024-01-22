function ver_carrito(url_django){
    $.ajax({
        url: url_django
    })
    .fail(function( result ) {
        alert("Error: " + result)
    })
    .done(function( result ) {
        cuerpo = $('#respuesta_carrito')
        cuerpo.html(result)
        const myOffcanvas = $('#offcanvasRight');
        myOffcanvas.offcanvas('toggle');
    });
}

function actualizar_totales(id, precio, cantidad){
    console.log(`ID producto ${id} - cantidad ${cantidad} - Precio ${precio}`);

    id_subtotal = document.getElementById("subtotal_"+id);
    id_subtotal.innerHTML = "Subtotal: "+ (cantidad * precio).toLocaleString();

    precios = document.getElementsByName("precios")
    cantidades = document.getElementsByName("cantidades")

    total = 0
     for (obj=0; obj < precios.length; obj++){
        total = total + (precios[obj].value * cantidades[obj].value);
    }

    total_carrito.innerHTML = "Total: "+ total.toLocaleString()

}