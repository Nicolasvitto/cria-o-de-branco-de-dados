class Cliente:
    def __init__(self,n,Fone):
        
        
        self._nome = n
        self._telefone = Fone

    #metodo get

    def get_Nome(self):
        return self._nome
    

    # metodo set
    def set_Nome(self,nome):
        self._nome = nome

