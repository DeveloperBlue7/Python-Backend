class Audifonos:
    
    def __init__(self):
        pass
    
    def conectar(self, estado='prendido'):
        self._analizando(estado)
        self._conectando()
        self._configurando()
        
    def _analizando(self, estado):
        print(f'analizando el dispositivo {estado}')
        
    def _conectando(self):
        print(f'Conectando dispositivo')
        
    def _configurando(self):
        print(f'configurando dispositivo listo para utilizar')
        
if __name__ == '__main__':
    audifonos = Audifonos()
    audifonos.conectar()