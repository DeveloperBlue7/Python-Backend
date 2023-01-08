class Suma:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def operacion(self, num):
        operacion1 = (self.num1 + num.num1)/2
        operacion2 = (self.num2 + num.num2)/2
        
        return (operacion1 + operacion2)
    
if __name__ == '__main__':
    suma1 = Suma(5,5)
    suma2 = Suma(15,15)
    suma3 = Suma(7,53)
    
    print(suma1.operacion(suma2))
    print(suma2.operacion(suma3))

class Trabajo:
    
    def __init__(self, ida, vuelta):
        self.ida = ida
        self.vuelta = vuelta 
        
    def dias(self, dias_laborados):
        mes1 = (self.ida + self.vuelta) * dias_laborados
        return mes1
        
turno_mañana = Trabajo(1, 2)
turno_noche = Trabajo(2, 4)


print(f'me demoro {turno_mañana.dias(22)} horas al mes')
print(f'me demoro {turno_noche.dias(30)} horas al mes')
    
    