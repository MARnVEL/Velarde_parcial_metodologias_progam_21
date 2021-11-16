
from room import Room
from item import Item, Comestible, Transportador, Mision
from player import Player, Npc
from stack import Stack, inverse
from parser_commands import Parser
# from npc import noPlayer

class Game:
    def __init__(self):
        self.createRooms()
        self.player = Player('Jugador 1', 20)
        self.npc = Npc('Mago', 0, 'Soy un mago')
        
        self.parser = Parser()
        self.stack = Stack()

    def createRooms(self):
        
        ##CREAR LAS SALAS
        outside = Room("OUTSIDE THE MAIN ENTRANCE of the university <-")
        theater = Room("in a LECTURE THEATER <-")
        pub = Room("in the CAMPUS PUB <-")
        lab = Room("in a COMPUTING LAB <-")
        office = Room("in the COMPUTIN ADMIN OFFICE <-")
        basement = Room ("In the BASEMENT <-")
        rooftop = Room("In the ROOFTOP <-")
        mainStreet = Room ("out! On the MAIN STREET <-")
        downtown = Room("outside, in THE CITY!!! In THE DOWNTOWN <-")
        beach = Room("outside the city!!! In the BEACH <-")

        
        ##Inicializar las salidas de las salas

        outside.setExits(mainStreet, theater, lab, pub, None, None)
        theater.setExits(mainStreet, None, None, outside, None, basement)
        basement.setExits(None, None, None, None, theater, None)
        pub.setExits(None, outside, None, None, rooftop, None)
        rooftop.setExits(None, None, None, None, None, pub)
        lab.setExits(outside, office, None, None, None, None)
        office.setExits(None, None, None, lab, None, None)        
        mainStreet.setExits(None, downtown, outside, beach, None, None)
        downtown.setExits(None, None, None, mainStreet, None, None)
        beach.setExits(None, mainStreet, None, None, None, None)


        ## Creas los ITEMS:
        espada = Item('espada','esot es una espada', 5)
        cookie = Comestible('cookie','esto es una galleta mágica', 0.1, 5, 'max_weight')
        rice = Comestible('rice','Esto es un poco de arroz', 0.25, 20, 'agility')
        apple = Comestible('apple', 'Esto es una manzana roja', 0.15, 7, 'strength')
        drink = Comestible('drink', 'Este es un refresco mágico', 0.10, 10, 'strength')

        antigua_llave = Mision('antigua_llave', 'Esto es llave magica',0.2)

        alas = Transportador('alas', 'Estas son alas para transportarse magicamente', 3)

        mago = Npc('mago', 'Hola amigo soy un mago. En que te puedo ayudar', 'Hola amigo soy un mago')

        
        
        zapatillas = Item('zapatillas','estas son zapatillas', 0.87)
        silla = Item('silla','una silla para descanzar', 2)
        ropero = Item('ropero','un ropero antiguo', 15, picked_up=False)

        #Ubicar los ITEMS en las distintas habitaciones
        outside.setNpc(mago)
        outside.setItem(antigua_llave)
        outside.setItem(espada)
        outside.setItem(cookie)
        outside.setItem(rice)
        outside.setItem(apple)
        outside.setItem(zapatillas)
        outside.setItem(alas)
        theater.setItem(silla)
        basement.setItem(ropero)
        pub.setItem(drink)
        
        # lab.setItem(mision)
        



        self.currentRoom = mainStreet ##Comenzar el juego en la calle principal.
        
        return
    
    







    def play(self):
        self.printWelcome()        

        finished = False
        while(not finished):
            command = self.parser.getCommand()
            finished = self.processCommand(command)
        print("Thank you for playing.  Good bye.")


    #Imprimir el mensaje de salida para el jugador. #

    def printWelcome(self):
        print()
        print("Bienvenido al mundo de Zuul!")
        print("El mundo de Zull es un nuevo e increíble juego de aventuras.")
        print("Escribe 'help' si necesitas ayuda.")
        print("")
        #Modificacion de la infromacion de la ubicacion actual.
        # Se creo un nuevo metodo : "print_location_info()"#
        self.currentRoom.print_location_information()
        print()


    def processCommand(self,command):
        wantToQuit = False

        if(command.isUnknown()):
            print("No entiendo lo que quieres decir...")
            return False
        
        commandWord = command.getCommandWord()

        if(commandWord == "help"):
            self.printHelp()
        elif(commandWord == "go"):
            self.goRoom(command)
        elif(commandWord == "quit"):
            wantToQuit = self.quit(command)

        elif(commandWord == "look"):#Este es el comando para observar los elementos que hay en la habitacion
            self.look_items()
        
        elif(commandWord == "bag"):
            self.bag_items()
        
        elif(commandWord == "back"):
            self.goBack()

        elif(commandWord == "take"):
            self.takeItem(command)
        
        elif(commandWord == "eat"):
            self.eatItem(command)

        elif(commandWord == "drop"):
            self.dropItem(command)

        elif(commandWord == "activate"):
            self.activateTransportador(command)

        elif(commandWord == "open"):
            self.openTransportador(command)

        elif(commandWord == "talk"):
            self.talk_npc(command)
        
        return wantToQuit

    def printHelp(self):
        print("Estás perdido y solo en los alrededores del CAMPUS DE LA UNIVERSIDAD")
        print()
        print("Las palabras de comando son:")
        print("   go | quit | help | look | bag | back | take | drop  | eat | talk  | activate | open")
        print()
        print("* look: permite observar todos los items que hay en la habitación.")
        print("* bag: permite observar todos los items que hay en la mochila que porta el jugador.")
        print("* take: permite al jugador tomar un item y guardarlo en la mochila.")
        print("* drop: permite al jugador dejar/soltar un item y dejarlo en la habitación en la que se encuentra el jugador.")
        print("* eat: permite al jugador comer un item (si este es comible) y modificar sus capacidades y/o habilidades.")
        print("* back: permite al jugador regresar a la habitación anterior.")
        print("* talk: permite al jugador hablar con un mago en la habitación")
        


    # Tratar de ir en una dirección. Si hay una salida, entrar en la nueva 
    # sala; en caso contrario, imprimir un mensaje de error.#

    def goRoom(self,command):
        if(not command.hasSecondWord()):
            ##Si no hay una segunda palabra no sabemos a dónde ir
            print("Go where?")
            print("Hey Dog. You must tell me the direction where you wanna go!!!")
            self.currentRoom.print_location_information()
            return
        
        direction = command.getSecondWord()
        #Tratar de salir de la sala actual.#
        nextRoom = self.currentRoom.get_exit(direction)


        if(nextRoom is None):
            print("Bad luck. There is no door!")
        else:
            self.currentRoom = nextRoom
            self.currentRoom.print_location_information()
            self.stack.push(direction)
            print()
            

        # nextRoom = None
        # if(direction == "north"):
        #     nextRoom = self.currentRoom.northExit
        # if(direction == "east"):
        #     nextRoom = self.currentRoom.eastExit
        # if(direction == "south"):
        #     nextRoom = self.currentRoom.southExit
        # if(direction == "west"):
        #     nextRoom = self.currentRoom.westExit
        # if(direction == "up"):
        #     nextRoom = self.currentRoom.upExit
        # if(direction == "down"):
        #     nextRoom = self.currentRoom.downExit
        
        # if(nextRoom == None):
        #     print("There is no door!")
        # else:
        #     self.currentRoom = nextRoom
        #     self.currentRoom.print_location_info()
    
    def takeItem(self, command):
        if(not command.hasSecondWord()):
            print("Take what?")
            print("Hey Dog. You must tell me what item you wanna take!!!")
            return

        item_name = command.getSecondWord()
        item = self.currentRoom.getItem(item_name)

        if (item is None):
            print("There isn't any item in the Room with this name!")
        else:
            if(item.picked_up):
                if(self.player.can_picked_up_new_item(item.weight)):
                    self.player.setItem(item)
                else:
                    print('You can not take this item because you have not weight enough!!')
                    self.currentRoom.setItem(item)
            else:
                print('You can not take this item!!')
                self.currentRoom.setItem(item)


    def dropItem(self, command):
        if(not command.hasSecondWord()):
            print("Drop what?")
            print("Hey Dog. You must tell me what item you wanna drop!!!")
            return

        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)

        if (item is None):
            print("You have NOT any item with this name to drop!")
        else:
            self.currentRoom.setItem(item)
        # else:
        #     if(item.drop):
        #         if(self.player.can_dropped_up_new_item(item.weight)):
        #             self.player.setItem(item)
        #         else:
        #             print('You can not take this item because you have not weight enough!!')
        #     else:
        #         print('You can not take this item!!')
        #         self.currentRoom.setItem(item)


    def eatItem(self, command):
        if(not command.hasSecondWord()):
            print("Eat what?")
            print("Hey Dog. I don't know whath you want to eat. You must tell me that!!!")
            print("Be aware, not all item can be eaten! :-(")
            return
        
        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)

        if(item is None):
            print("There is not item in the player bag with this name!")
        else:
            if(isinstance(item, Comestible)):#####
                response = item.comer(self.player)
                if(not response):
                    self.player.setItem(item)            
            else:
                print('Este item no es comestible')
                self.player.setItem(item)
        

    def activateTransportador(self, command):

        if(not command.hasSecondWord()):
            print("activate what?")
            print("Hey Dog. I don't know what you want to activate. You must tell me that!!!")
            print("Be aware, not all item can be activated! :-(")
            return
        
        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)

        if(item is None):
            print("There is not item in the player bag with this name!")
        else:
            if(isinstance(item, Transportador)):#####
                if(item.is_active()):
                    print("TRANSPORTANDOME/VOLANDO")
                    self.currentRoom = item.room_back
                    self.currentRoom.print_location_information()

                else:
                    print("El transportador no fue abierto todavia")
                    self.player.setItem(item)   
            else:
                print('Este item no es del tipo transportador y no se puede activar')
                self.player.setItem(item)

    def openTransportador(self, command):
        if(not command.hasSecondWord()):
            print("Open what?")
            print("Hey. I don't know what you want to open. You must tell me that!!!")
            print("Be aware, not all item can be open! :-(")
            return
        
        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)

        if(item is None):
            print("There is not item in the player bag with this name!")
        else:
            if(isinstance(item, Transportador)):#####
                print("The room set to back is: ", self.currentRoom.description)
                item.room_back = self.currentRoom       
            else:
                print('Este item no es del tipo transportador y no se puede abrir')

            self.player.setItem(item)

    def talk_npc(self, command):
        if(not command.hasSecondWord()):
            print("Talk with who?")
            print("Hey. I don't know with who to talk. You must tell me that!!!")
            print("Be aware, not all item can talk! :-(")
            return
        
        npc_name = command.getSecondWord()
        npc = self.player.getNpc(npc_name)

        if(npc is None):
            print("There is not Npc in the room with this name!")
        else:
            if(isinstance(npc, Npc)):#####
                print(self.talk_npc())
                # item.room_back = self.currentRoom       
            else:
                print('Este item no puede hablar')

            self.player.setNpc(npc)



    def look_items(self):
        self.currentRoom.print_items_information()
        self.currentRoom.print_npcs_information()
        # self.currentRoom.mision_description()

    def bag_items(self):
        self.player.print_items_information()
    
    def goBack(self):
        direction = self.stack.pop()
        if(direction):
            nextRoom = self.currentRoom.get_exit(direction)
       
            if(nextRoom is None):
                print("There is no door to go!", direction)
                self.stack.push(inverse[direction])
            else:
                self.currentRoom = nextRoom
                self.currentRoom.print_location_information()
                print()
        else:
            print('you are in the initial position: "Main Street". You can not go back')
            self.currentRoom.print_location_information()


    def quit(self, command):
        if(command.hasSecondWord()):
            print("Quit what?")
            return False
        else:
            return True

g = Game()
g.play()
