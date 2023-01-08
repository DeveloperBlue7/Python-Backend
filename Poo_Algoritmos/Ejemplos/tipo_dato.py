# PRACTICAS Y EJEMPLOS 
class Computador:
    
    def __init__(self, marca, pulgadas, precio):
        self.marca = marca
        self.pulgadas = pulgadas
        self.precio = precio
        
    def prender(self, objeto):
        return f'Para prender el computador de marca {self.marca} de {self.pulgadas} que su precio es {self.precio} se necesita un {objeto}'
    
computador_1 = Computador('ASUS', '17 Pulgadas', 4000000)

print(computador_1.prender('Cargador'))


class Empleado:
    
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
    def contratar(self, ciudad):
        return f'Para contratar a {self.nombre} que tiene {self.edad} años con profesion de {self.profesion} debe vivir en {ciudad}'
    
empleado_1 = Empleado('Christian', 31, 'Programador')

print(empleado_1.contratar('Medellin'))

class Silla:
    
    def __init__(self, marca, color, medida, altura):
        self.marca = marca
        self.color = color
        self.medida = medida
        self.temaño = altura
        
    
silla_1 = Silla('Lotus', 'Blanco', 100, 10)

if silla_1.color == 'Blanco':
    print(f'Es la silla perfecta para mi casa')
else:
    print('El producto no me interesa')
    