from threading import Thread
from entity import *

class Game(Thread):
    
    running = True
    level = None
    players = {}
    npcs = {}
    
    def __init__(self,level):
        Thread.__init__(self)
        self.level = level
        self.players[0]=Entity(0,Point((level.PAS_X/2)*15,300))
        self.players[1]=Entity(1,Point((level.PAS_X/2)*15,300))
        self.npcs[0] = Monster(self,0,Point(level.PAS_X/2,200))
        self.npcs[0].setAI(BasicAI)
        
    def run(self):
        while self.running:
            print "AI decision"
            for npc in self.npcs.values():
                npc.action()
                
    def stop(self):
        self.running = False
