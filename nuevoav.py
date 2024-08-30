print("Nuestro menú se mostrará a continuación:\n POSTRES/núm-> 25 Pays de manzana - 50 Galletas - 40 Cheescakes")
print(" PASTELES-> Chocolate, Vainilla, Tres leches")
print(" BEBIDAS-> Café, Malteada, Té  \n")

#si es pastel, especificar el sabor"

producto=str(input("Ingresa tu producto:"))

def pasteles(producto_a):
    if producto_a.lower().replace(" ","") == "pasteldechocolate":
        print (40)
    elif producto_a.lower().replace(" ","") == "pasteldevainilla":
        print (40)
    elif producto_a.lower().replace(" ","") == "pasteldetresleches":
        print (45) 
def bebidas(producto_b):  
    if producto_b.lower().replace(" ","") == "café":
        print (30)
    elif producto_b.lower().replace(" ","")  == "malteada":
        print (35)
    elif producto_b.lower().replace(" ","")  == "té":
        print (35)
def postres(producto_c): 
    if producto_c.lower().replace(" ","") == "paydemanzana":
        print (30)
    elif producto_c.lower().replace(" ","")  == "galleta":
        print (15)
    elif producto_c.lower().replace(" ","")  == "cheesecake":
        print (25)

pasteles(producto)
bebidas(producto)
postres(producto)