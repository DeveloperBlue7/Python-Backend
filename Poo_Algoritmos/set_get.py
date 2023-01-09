# Clases sin getters y setters

class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia
        
    def convertir_kilometros(self):
        print(self.distancia * 1.609344)
        
avion = Millas()

avion.distancia = 500

print(avion.distancia)

print(avion.convertir_kilometros())

    