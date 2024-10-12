def pasteles(producto_a):
    if producto_a.lower().replace(" ", "") == "chocolate":
        return 40
    elif producto_a.lower().replace(" ", "") == "vainilla":
        return 40
    elif producto_a.lower().replace(" ", "") == "tresleches":
        return 45
    else:
        return 0

def bebidas(producto_b):  
    if producto_b.lower().replace(" ", "") == "café":
        return 30
    elif producto_b.lower().replace(" ", "") == "malteada":
        return 35
    elif producto_b.lower().replace(" ", "") == "té":
        return 35
    else:
        return 0

def postres(producto_c): 
    if producto_c.lower().replace(" ", "") == "paydemanzana":
        return 30
    elif producto_c.lower().replace(" ", "") == "galleta":
        return 15
    elif producto_c.lower().replace(" ", "") == "cheesecake":
        return 25
    else:
        return 0

#Menú:
def inicio(): 
    print("\n--- Nuestro menú se mostrará a continuación: ---")
    print(" PASTELES-> Chocolate, Vainilla, Tres leches")
    print(" BEBIDAS-> Café, Malteada, Té")
    print(" POSTRES-> Pays de manzana, Galletas, Cheescakes  \n")
    
    tipo = input("Elige tu categoría de producto e ingresa la letra correspondiente: \n A-Pasteles \n B-Bebidas \n C-Postres \n")
    tipo = tipo.upper() #Volverlo mayúsculas
    return tipo

#Menú de pasteles
def menuA():
    print("\nLos sabores se muestran a continuación: \n Chocolate - Vainilla - Tres leches")
    producto = input("Ingresa tu producto: ")
    precio = pasteles(producto)
    if precio == 0:
        print("No tenemos ese producto :(")
        return (None, 0)
    cantidad = int(input("¿Cuál será la cantidad?: "))
    total = calcularTotal(precio, cantidad)
    return (producto, cantidad, total)
#Menú de bebidas
def menuB():
    print("\nLos productos se muestran a continuación: \n Café - Malteada - Té")
    producto = input("Ingresa tu producto: ")
    precio = bebidas(producto)
    if precio == 0:
        print("No tenemos ese producto :(")
        return (None, 0)
    cantidad = int(input("¿Cuál será la cantidad?: "))
    total = calcularTotal(precio, cantidad)
    return (producto, cantidad, total)
#Menú de postres
def menuC():
    print("\nLos productos se muestran a continuación: \n Pay de manzana - Galleta - Cheesecake")
    producto = input("Ingresa tu producto: ")
    precio = postres(producto)
    if precio == 0:
        print("No tenemos ese producto :(")
        return (None, 0)
    cantidad = int(input("¿Cuál será la cantidad?: "))
    total = calcularTotal(precio, cantidad)
    return (producto, cantidad, total)

#Para el total del producto
def calcularTotal(precio, cantidad):
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
        print("\nINCORRECTO, POR FAVOR ELIGE UNA OPCIÓN VÁLIDA\n")
        continue #Hace que el WHILE se vuelva a preguntar

    if producto is not None:
        carrito.append((producto, total))
        
        orden_final.append([producto, cantidad, total])
    
    continuar = input("¿Desea agregar otro producto al carrito? (Si/No): ").upper()
    if continuar != "SI":
        break
    

#Para el carrito y total final:
print("\n CARRITO DE COMPRAS:")
total_final = 0
#i->item
for item in carrito:
    print(f"Producto: {item[0]} - Total: ${item[1]}")
    total_final += item[1]

print(f"\nEl total final de tu compra es: ${total_final}")

# 
print("\n RESUMEN DE ORDEN FINAL:")
for orden in orden_final:
    print(f"Producto: {orden[0]} || Cantidad: {orden[1]} || Total: ${orden[2]}")