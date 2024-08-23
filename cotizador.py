def cotizador(producto):
    if producto == "Pastel":
        return 20
    elif producto == "Baguette":
        return 15
    elif producto == "Café":
        return 7
    elif producto == "Galletas":
        return 5
    else:
        print("No existe ese producto")
        exit()

producto=input("Escribe el producto: ")
precio=cotizador(producto)
print(precio)
    
