import random
class block():
    def __init__(self):
        self.standable = True
        self.color = (0,0,0)
        self.infectlvl = 0

    def interact(self,player):
        pass


class chair(block):
    def __init__(self):
        self.name = 'chair'
        block.__init__(self)
        self.color = (153, 187, 255)

    def interact(self,player):
        sneez = random.randint(0,110-player.infeclvl)
        if sneez >= (105-player.infeclvl):
            player.sneez = True
            self.infectlvl += random.randint(0,(player.infeclvl+4)//5)
            print(self.infectlvl)


class floor(block):
    def __init__(self):
        self.name = 'floor'
        block.__init__(self)
        self.color = (183, 183, 149)

    def interact(self,player):
        sneez = random.randint(0, 110 - player.infeclvl)
        if sneez >= (110 - player.infeclvl):
            player.sneez = True
            self.infectlvl += random.randint(0, (player.infeclvl + 4) // 5)
            print(self.infectlvl)


class wall(block):
    def __init__(self):
        self.name = 'wall'
        block.__init__(self)
        self.color = (224, 224, 209)
        self.standable = False

    def interact(self,player):
        print('wall')


class table(block):
    def __init__(self):
        self.name = 'table'
        block.__init__(self)
        self.color = (172, 115, 57)
        self.standable = False


class food(block):
    def __init__(self):
        block.__init__(self)
        self.name = 'food'
        self.color = (255,140,0)
        self.standable = False

    def interact(self,player):
        player.hunger = 100
        sneez = random.randint(0, 105 - player.infeclvl)
        if sneez >= (105 - player.infeclvl):
            player.sneez = True
            self.infectlvl += random.randint(0, (player.infeclvl + 4) // 5)
            print(self.infectlvl)


class rr(block):
    def __init__(self):
        block.__init__(self)
        self.name = 'rr'
        self.color = (30,144,255)
        self.standable = False

    def interact(self, player):
        player.rr = 100
        print('rr')
        sneez = random.randint(0, 105 - player.infeclvl)
        if sneez >= (105 - player.infeclvl):
            player.sneez = True
            self.infectlvl += random.randint(0, (player.infeclvl + 4) // 5)
            print(self.infectlvl)


class expert(block):
    def __init__(self):
        block.__init__(self)
        self.name = 'expert'
        self.color = (128, 0, 0)
        self.standable = False

    def interact(self, player):
        player.roadBlock = False
        print('ex')
        sneez = random.randint(0, 105 - player.infeclvl)
        if sneez >= (105 - player.infeclvl):
            player.sneez = True
            self.infectlvl += random.randint(0, (player.infeclvl + 4) // 5)
            print(self.infectlvl)


class leave(block):
    def __init__(self):
        block.__init__(self)
        self.name = 'leave'
        self.color = (5, 5, 5)
        self.standable = False

    def interact(self, player):
        player.qlvl +=1
        if player.qlvl > 5:
            player.out = True



