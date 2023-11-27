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
