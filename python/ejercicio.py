print('Cordial saludo estimado usuario')

precio=float(input("Por favor ingresa el precio del producto"))
 

print(f"Has ingresado el precio: {precio}")

while precio<=0:
    precio=float(input("El precio debe ser positvo"))


categoria=str(input("Por favor ingresa la categoria del producto a la cual pertece el producto (Electrónica, Ropa, Alimentos, Libros):"))


match categoria:
    case "Electrónica":
        print("Tu producto es de la categoría Electrónica por tal motivo tienes un descuento del 10 porciento en el, te queda en")
        descuento=0.1
        resultado=precio-(precio*descuento)
        print(resultado)
        
    case "Ropa": 
        print("Tu producto es de la categoría Ropa por tal motivo tienes un descuento del 15 porciento en el, te queda en")
        descuento=0.15
        resultado=precio-(precio*descuento)
        print(resultado)
    case "Alimento":
        print("Tu producto es de la categoría Alimentos por tal motivo tienes un descuento del 5 porciento en el, te queda en")
        descuento=0.05
        resultado=precio-(precio*descuento)
        print(resultado)
    case "Libros":
        print("Tu producto es de la categoría Libros por tal motivo tienes un descuento del 20 porciento en el, te queda en")
        descuento=0.2
        resultado=precio-(precio*descuento)
        print(resultado)
    case _: 
        print("Has ingresado una categoría no válida, por favor intenta de nuevo o escribela tal y como aparece en la indicación")
    
   
        
