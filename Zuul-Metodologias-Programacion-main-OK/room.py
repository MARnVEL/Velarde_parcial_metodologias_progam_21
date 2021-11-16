
class Room:
    def __init__(self, description):
        self.description = description
        self.exits = {} #! clave -> valor
        #Se agregan items
        self.items = {}
        self.npcs = {}
        # ! listas y diccionarios
        # [mesa, silla, espada]
        # {'mesa': mesa, 'silla': silla, 'espada': espada}


        #self.northExit = None
        #self.southExit = None
        #self.eastExit = None
        #self.westExit = None
        #self.upExit = None
        #self.downExit = None
        
    """
    Definir las salidas de esta sa la. Cada dirección conduce a otra sala o tiene el valor
    None (no hay salida ahi).
    """


    def setExits(self, north, east, south, west, up, down):
        if(north != None):
            self.exits['north'] = north
        if(east != None):
            self.exits['east'] = east
        if(south != None):
            self.exits['south'] = south
        if(west != None):
            self.exits['west'] = west
        if(up != None):
            self.exits['up'] = up
        if(down != None):
            self.exits['down'] = down
        return


    def setItem(self, item):
        self.items[item.name] = item  #LA CLAVE VA A SER EL NOMBRE Y EL ITEM QUE LE PASO ES EL VALOR.
    
    def setNpc(self, npc):
        self.npcs[npc.name] = npc

    ##Con este metodo el jugador agarra un item

    def getItem(self, item):
        if(item in self.items):
            return self.items.pop(item)
        else:
            return None


    def getNpc(self, npc):
        if(npc in self.npcs):
            return self.npcs.pop(npc)
        else:
            return None


#Devuelve la descripción de la sala (la que se haya definido en el constructor)

    def getDescription(self):
        return self.description

    def print_location_information(self):
        print("-> You are " + self.getDescription())
        print("If you want to know if there is any item in the room type: look ")
        print("Salidas: ")  
        exits = ' | '
        for direction in self.exits.keys(): # direction está definida en la clase Game en el método goRoom. Es la segunda palabra ingresada en el comando go
            exits += direction + ' | '
        print(exits)
        #self.print_items_information()

        # if(self.northExit is not None):
        #     print("north ")
        # if(self.eastExit is not None):
        #     print("east ")
        # if(self.southExit is not None):
        #     print("south ")
        # if(self.westExit is not None):
        #     print("west ")
        # if(self.upExit is not None):
        #     print("up ")
        # if(self.downExit is not None):
        #     print("down ")
        # print()


    def get_exit(self, direction):
        if(direction in self.exits):
            return self.exits[direction]
        else:
            return None
    
    def print_items_information(self):
        print("Items: ")
        items = ''
        for item in self.items.keys(): #Para la "llave/clave" item en el diccionario items: carga en el diccionario
            # self.items[item] es el nombre de la clave del diccionario items 
            items += self.items[item].name + ' '
        
        if(len(items) == 0):
            print("There is no items in the room")
        else:
            print(items)

        # if(self.items[''] == 'Mision'):
        #     print(self.description)

    def print_npcs_information(self):
        print("Npcs: ")
        npcs = ''
        for npcs in self.npcs.keys(): #Para la "llave/clave" item en el diccionario items: carga en el diccionario
            # self.items[item] es el nombre de la clave del diccionario items 
            npcs += self.npcs[npcs].name + ' '
            



