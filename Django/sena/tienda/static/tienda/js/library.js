nombre = prompt("Digite su nombre: ")
edad = parseInt(prompt("Digite su edad: "))

if (edad > 18 || edad == 18){
    alert("Bienvenido a nuestra Tienda " + nombre+ " !!")
}

else{
    alert("Lo siento, no puede comprar...")
}

console.log("Terminamos...")
