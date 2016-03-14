from graphics import *

class UserInterface(object):
    window=None
    players = []
    def __init__(self):
        self.window=GraphWin()
       #self.window.getMouse()
        
    def addPlayer(self,player):
       self.players.append(player)
        
    def drawPlayers(self):
        for p in self.players:
            print p.circle
            p.circle.draw(self.window)
