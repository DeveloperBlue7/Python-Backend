# definición 
class persona:
    def __init__(self, nombre, edad, estatura):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        
    def saludo(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre} tengo {self.edad} años, en mi cedula mido {self.estatura}'
    
# Uso
David = persona('David', 31, 1.75)
Marcela = persona('Marcela', 34, 1.65)
Carlos = persona('Carlos',31, 1.70)

print(David.saludo(Carlos))