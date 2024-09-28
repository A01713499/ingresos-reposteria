def pasteles(producto_a):
    if producto_a.lower().replace(" ","") == "chocolate":
        return 40
    elif producto_a.lower().replace(" ","") == "vainilla":
        return 40
    elif producto_a.lower().replace(" ","") == "tresleches":
        return 45
    else:
        return 0
def bebidas(producto_b):  
    if producto_b.lower().replace(" ","") == "café":
        return 30
    elif producto_b.lower().replace(" ","")  == "malteada":
        return 35
    elif producto_b.lower().replace(" ","")  == "té":
        return 35
    else:
        return 0
def postres(producto_c): 
    if producto_c.lower().replace(" ","") == "paydemanzana":
        return 30
    elif producto_c.lower().replace(" ","")  == "galleta":
        return 15
    elif producto_c.lower().replace(" ","")  == "cheesecake":
        return 25
    else:
        return 0
def inicio(): 
    print("\n Nuestro menú se mostrará a continuación:\n POSTRES-> Pays de manzana, Galletas, Cheescakes")
    print(" PASTELES-> Chocolate, Vainilla, Tres leches")
    print(" BEBIDAS-> Café, Malteada, Té  \n")

    tipo = input("Elige tu categoría de producto e ingresa la letra correspondiente: \n A-Postres \n B-Pasteles \n C-Bebidas \n")
    tipo = tipo.upper()
    return tipo
 
def calcularTotal(precio):
    cantidad = int(input("¿Cuál será la cantidad?: "))
    total = precio * cantidad
    print("El total de tu compra es: ", total)
    
    
def menuA ():
    print (" \nLos sabores se muestran a continuación: \n Chocolate - Vainilla - Tres leche")
    precio = pasteles(str(input("Ingresa tu producto: ")))
    calcularTotal(precio)
def menuB ():
    print (" \nLos productos se muestran a continuación: \n Café - Malteada - Té")
    precio = bebidas(str(input("Ingresa tu producto: ")))
    
    if precio == 0:
        print("No tenemos ese producto :(")
        return
        
    calcularTotal(precio)    
def menuC ():
    print (" \nLos productos se muestran a continuación: \n Pay de manzana - Galleta - Cheesecake")
    precio = postres(str(input("Ingresa tu producto: ")))
    calcularTotal(precio)
 
while True:
    tipo = inicio()
    if tipo == "A":
        menuA()  
    elif tipo == "B":
        menuB()
    elif tipo == "C":
        menuC()
    else: tipo=input("Incorrecto, elige una opción valida: \n")
    
    productos = {
    "A": {
        "Chocolate": 40,
        "Vainilla": 40,
        "Tres leches": 45
    },
    "B": {
        "Café": 30,
        "Malteada": 35,
        "Té": 35
    },
    "C": {
        "Pay de manzana": 30,
        "Galleta": 15,
        "Cheesecake": 25
    }
}