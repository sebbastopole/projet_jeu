from utils import *
from threading import Thread

AI_INTERVAL = 0.5

class CondActionAI(Thread):

    game = None
    entId = None
    actions = []
    
    def __init__(self, game, entId):
    
        Thread.__init__(self)
        self.game = game
        self.entId = entId
        
    def addAction(self, action):
        self.actions.append(action)
        
    def run(self):
        for action in self.actions:
            action(self)
        time.sleep(AI_INTERVAL)      
    
class BasicAI(CondActionAI):
    
    def __init__(self, game, entId):
        CondActionAI.__init__(self,game,entId)
        self.addAction(BasicAI.basicMove)
    
    def basicMove(self):
        npc = self.game.npcs[self.entId]
        pos = npc.pos
        pas_x = self.game.level.PAS_X
        lines = self.game.level.lines
        d = get_direction(pos,pas_x,lines)
        if d != (0,0):
            npc.move(*d)
            

