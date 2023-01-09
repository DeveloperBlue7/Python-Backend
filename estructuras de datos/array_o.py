class Array:
    
    def __init__(self, capacidad, valor = None):
       
       self.items = list() 
       for i in range(capacidad):
           self.items.append(valor)
           

    def __len__(self):
        return len(self.items) 
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]      
    
    def __setitem__(self, index, nuevo_item):
        self.items[index] = nuevo_item
        