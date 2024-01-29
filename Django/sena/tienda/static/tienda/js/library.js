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

function actualizar_totales(id, cantidad, precio){
    console.log(`Id producto ${id} - cantidad ${cantidad} - Precio ${precio}`);

    id_subtotal = document.getElementById("subtotal_"+id);
    total_carrito = document.getElementById("total_carrito")

    id_subtotal.innerHTML = "$"+ (cantidad * precio).toLocaleString()

    precios = document.getElementsByName("precios")
    cantidades = document.getElementsByName("cantidades")

    total = 0
     for (obj=0; obj < precios.length; obj++){
        total = total + (precios[obj].value * cantidades[obj].value);
     }

     console.log(total)

    total_carrito.innerHTML = "Total: "+ total.toLocaleString()

}

function actualizar_carrito(url_django, id, cantidad){
    loader = $('#loading_cc');
    loader.removeClass("d-none");
    loader.addClass("d-block");

    $.ajax({
        url: url_django,
        method: "GET",
        data: {"id": id, "cantidad": cantidad}
    })
    .fail(function( result ) {
        alert("Error: " + result);
        loader.removeClass("d-block");
        loader.addClass("d-none");
    })
    .done(function( result ) {
        loader.removeClass("d-block");
        loader.addClass("d-none");
    });
}