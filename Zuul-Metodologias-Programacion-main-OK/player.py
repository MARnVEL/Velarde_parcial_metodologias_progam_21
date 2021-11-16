


class Player():
    def __init__(self, name, max_weight):
        self.name = name
        self.max_weight = max_weight
        self.items = {}
        
        self.strength = 1
        self.defense = 1
        self.equipement = {'casco':None, 'arma':None, 'armadura':None}

    def setItem(self, item):
        self.items[item.name] = item
    
    def print_items_information(self):
        print("Items: ")
        items = ''
        for item in self.items.keys():
            items += self.items[item].name + ' '
        print(items)
        # print('peso total')  #No entiendo para que esta esta linea


    # def dropItem(self, item):
    #     self.items[item.name] = item

    # def takeItem(self, item):
    #     self.items[item.name] = item
    
    def can_picked_up_new_item(self, weight):
        peso_total = 0
        for item in self.items.values():
            peso_total += item.weight
        peso_total += weight
        return peso_total <= self.max_weight

        # if(newWeight <= 20):
        #     newWeight=self.items

    def getItem(self, item):
        if(item in self.items):
            return self.items.pop(item)
        else:
            return None

class Npc(Player):
    def __init__(self, name, max_weight, talk):
        super().__init__(name, max_weight)
        self.talk = talk
        self.npcs = {}

    def setNpc(self, npc):
        self.npcs[npc.name] = npc

    def getNpc(self, npc):
        if(npc in self.npcs):
            return self.npcs.pop(npc)
        else:
            return None

    def talk_npc(self):
        print("Hello my friend I'm a magician")













