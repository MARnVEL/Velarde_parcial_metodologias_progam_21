

class Item:

    def __init__(self, name, descripton, weight, picked_up=True, comestible = True):
        self.name = name
        self.description = descripton
        self.weight = weight
        self.picked_up = picked_up
        self.comestible = comestible
    
class Comestible(Item):

    def __init__(self, name, description, weight, increment, atribute, picked_up=True):
        # super(Comestible, self).__init__(*args))
        super().__init__(name, description, weight, picked_up)
        self.increment = increment
        self.atribute = atribute

    
    def comer(self, player):
        # return super().comer(player)
        if(self.atribute in player.__dict__):
            print('Valor actual:', self.atribute, player.__dict__[self.atribute])
            print('El jugador se ha comido: ', self.name)
            player.__dict__[self.atribute] += self.increment
            print('Valor nuevo: ', self.atribute, player.__dict__[self.atribute])
            return True
        else:
            print('El jugador no tiene atributo: ', self.atribute)
            return False


class Mision(Item):
    def __init__(self, name, descripton, weight, picked_up=True):
        super().__init__(name, descripton, weight, picked_up=picked_up)
        # self.mision_description()

    def mision_description(self):
        print ("DESCRIPCION DE LA MISION")



class Equipamiento(Item):

    def __init__(self, name, description, weight, type, increment, atribute, picked_up=True):
        super().__init__(name, description, weight, picked_up = picked_up)


class Transportador(Item):
    def __init__(self, name, descripton, weight, picked_up=True):
        super().__init__(name, descripton, weight, picked_up=picked_up)
        self.room_back = None
    
    def is_active(self):
        return self.room_back is not None
    

    

        