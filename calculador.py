"""
PROYECTO: CALCULADOR MONETARIO DE UNA CAFETERÍA
TECNOLÓGICO DE MONTERREY, CAMPUS QUERÉTARO

PENSAMIENTO COMPUTACIONAL PARA LA INGENIERÍA- GPO 415
PROF. BENJAMÍN VALDÉS AGUIRRE
A01713499- PAULA SOFÍA CABALLERO MARTÍNEZ

"""


def pasteles(producto_a):
    """
    Recibe: El sabor del pastel deseado.  
    Devuelve: El precio correspondiente del pastel.
    """
    if producto_a.lower().replace(" ", "") == "chocolate" :
        return 40
    elif producto_a.lower().replace(" ", "") == "vainilla" :
        return 40
    elif producto_a.lower().replace(" ", "") == "tresleches" :
        return 45
    else:
        return 0

def bebidas(producto_b):
    """
    Recibe: El tipo de bebida deseada.  
    Devuelve: El precio correspondiente de la bebida.
    """
    if producto_b.lower().replace(" ", "") == "café" :
        return 30
    elif producto_b.lower().replace(" ", "") == "malteada" :
        return 35
    elif producto_b.lower().replace(" ", "") == "té" :
        return 35
    else:
        return 0

def postres(producto_c):
    """
    Recibe: El tipo de postre deseado.  
    Devuelve: El precio correspondiente del postre.
    """
    if producto_c.lower().replace(" ", "") == "paydemanzana" :
        return 30
    elif producto_c.lower().replace(" ", "") == "galleta" :
        return 15
    elif producto_c.lower().replace(" ", "") == "cheesecake" :
        return 25
    else:
        return 0

#Menú completo que será mostrado al cliente: 
def inicio():
    """
    Muestra al cliente el menú completo
    y le pregunta la categoría de producto de desea
    """
    print("\n--- Nuestro menú se mostrará a continuación: ---")
    print(" PASTELES-> Chocolate, Vainilla, Tres leches")
    print(" BEBIDAS-> Café, Malteada, Té")
    print(" POSTRES-> Pay de manzana, Galleta, Cheesecake  \n")
    
    tipo = input("Elige tu categoría de producto e ingresa la letra"
        "correspondiente: \n A-Pasteles \n B-Bebidas \n C-Postres \n")
    
    tipo = tipo.upper() #.upper() para volverlo mayúsculas
    return tipo

#Menú de pasteles
def menuA():
    """
    Muestra el menú de pasteles para seleccionar el producto y cantidad.
    Devuelve: El nombre del producto elegido, la cantidad y total.
    """
    print("\nLos sabores se muestran a continuación:"
    "\n Chocolate - Vainilla - Tres leches")
    
    while True:
        producto = input("Ingresa tu producto: ").lower().replace(" ", "")
        # .lower() para leerlo en minúsculas
        if producto not in ["chocolate", "vainilla", "tresleches"]:
            print("No tenemos ese producto :(")
        else:
            precio = pasteles(producto)
            break
        
    if precio == 0:
        print("No tenemos ese producto :(")
        return (None, 0)
    
    while True:
        try:
            cantidad = int(input("¿Cuál será la cantidad?: "))
            if cantidad < 0:
                print("La cantidad no debe ser menor a cero, "
                      "por favor intenta de nuevo")
            else:
                total = calcularTotal(precio, cantidad)
                break
        except ValueError:
            print("Por favor ingrese un número")
    
    return producto, cantidad, total

#Menú de bebidas
def menuB():
    """
    Muestra el menú de bebidas para seleccionar el producto y cantidad.
    Devuelve: El nombre del producto elegido, la cantidad y total.
    """
    print("\nLos productos se muestran a continuación:"
    "\n Café - Malteada - Té")
    
    while True:
        producto = input("Ingresa tu producto: ").title()  
        # .title() para leerlo como título
        if producto not in ["Café", "Malteada", "Té"]:
            print("No tenemos ese producto :(")
        else:
            precio = bebidas(producto)
            break
        
    if precio == 0:
        print("No tenemos ese producto :(")
        return (None, 0)
    
    while True:
        try:
            cantidad = int(input("¿Cuál será la cantidad?: "))
            if cantidad < 0:
                print("La cantidad no debe ser menor a cero, "
                      "por favor intenta de nuevo")
            else:
                total = calcularTotal(precio, cantidad)
                break
        except ValueError:
            print("Por favor ingrese un número")
    
    return producto, cantidad, total

#Menú de postres
def menuC():
    """
    Muestra el menú de postres para seleccionar el producto y cantidad.
    Devuelve: El nombre del producto elegido, la cantidad y total.
    """
    print("\nLos sabores se muestran a continuación:"
    "\n Pay de manzana - Galleta - Cheesecake")
    
    while True:
        producto = input("Ingresa tu producto: ").title()  
        # .title() para leerlo como título
        if producto not in ["Pay de manzana", "Galleta", "Cheesecake"]:
            print("No tenemos ese producto :(")
        else:
            precio = postres(producto)
            break
        
    if precio == 0:
        print("No tenemos ese producto :(")
        return (None, 0)
   
    while True:
        try:
            cantidad = int(input("¿Cuál será la cantidad?: "))
            if cantidad < 0:
                print("La cantidad no debe ser menor a cero, "
                      "por favor intenta de nuevo")
            else:
                total = calcularTotal(precio, cantidad)
                break
        except ValueError:
            print("Por favor ingrese un número")
    
    return producto, cantidad, total

#Para el total del producto
def calcularTotal(precio, cantidad):
    """
    Calcula el costo total
    Multiplica el precio por la cantidad
    """
    return precio * cantidad


carrito = []
orden_final = []

while True:
    tipo = inicio()
    if tipo == "A":
        producto, cantidad, total = menuA()
    elif tipo == "B":
        producto, cantidad, total = menuB()
    elif tipo == "C":
        producto, cantidad, total = menuC()
    else:
        print("\nEHHHHH, está mal :( \nPor favor elige una opción válida \n")
        continue #Hace que el WHILE se vuelva a preguntar

    if producto is not None:
        carrito.append((producto, total))
        
        orden_final.append([producto, cantidad, total])
    
    continuar = input("¿Agregará otro producto al carrito? (Si/No): ").upper()
    if continuar != "SI":
        break
    

#Para mostrar el carrito y total final:
print("\n CARRITO DE COMPRAS:")
total_final = 0
#i->item
for item in carrito:
    print(f"Producto: {item[0]} - Total: ${item[1]}")
    total_final += item[1]

print(f"\nEl total final de tu compra es: ${total_final}")

#Para mostrar el resumen de la orden final 
print("\n RESUMEN DE ORDEN FINAL:")
for orden in orden_final:
    print(f"Producto: {orden[0]} || Cantidad: {orden[1]} || Total: ${orden[2]}")
    #f -> formato
