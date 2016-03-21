from player import *

class Game(object):
    
    level = None
    players = {}
    npcs = {}
    
    def __init__(self,level):
        self.level = level
        self.players[1]=Player(1,Point(425,300))
        self.players[2]=Player(2,Point(425,300))
        self.npcs[0] = Monster(self,0,Point(145,200))
        self.npcs[0].setAI(BasicAI)
        
    def tick(self):
        for npc in self.npcs.values():
            npc.action()
    
