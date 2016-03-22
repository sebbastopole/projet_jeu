from utils import *

class CondActionAI(object):

    game = None
    entId = None
    actions = []
    
    def __init__(self, game, entId):
        self.game = game
        self.entId = entId
        
    def addAction(self, action):
        self.actions.append(action)
        
    def doAction(self):
        for action in self.actions:
            action(self)
    
class BasicAI(CondActionAI):
    
    def __init__(self, game, entId):
        CondActionAI.__init__(self,game,entId)
        self.addAction(BasicAI.basicMove)
    
    def basicMove(self):
        npc = self.game.npcs[self.entId]
        pos = npc.pos
        pas_x = self.game.level.PAS_X
        lines = self.game.level.lines
        d = get_direction(pos,npc.size,lines)
        if d != (0,0):
            npc.move(*d)
            self.game.ui.moved = True
            

