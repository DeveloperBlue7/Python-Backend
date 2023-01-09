def suma(a, b):
    total = a + b
    return total

print(suma(7,7))

## 
def name(nombre, apellido, inverso = True):
    if inverso:
        return f"{nombre} {apellido}"
    else:
        return f"{apellido} {nombre}"
    
print(name("Christian", "Camargo"))
print(name("Christian", "Camargo", inverso= False))
print(name(apellido="Christian", nombre="Camargo"))