class Horario:
    
    def __init__(self, cedula, materias):
        self._cedula = cedula
        self._materias = materias
        self._clase = None
        
    @property
    def clase(self):
        return self._clase
    
    @clase.setter
    def clase(self, clase):
        if clase in self._materias:
            self._materias = clase
        else:
            raise ValueError(f'la clase {clase} no esta en las materias {self._materias} permitidas')
        
horario = Horario(1019056615, ['Matematicas', 'Quimica'])

print(horario.clase)

horario.clase = "Ingles"

print(horario.clase)
