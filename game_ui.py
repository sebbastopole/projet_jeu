from graphics import *

class UserInterface(object):
    window=None #fenetre du jeu
    players = [] #liste de joueurs
    def __init__(self):
        self.window=GraphWin() #init fenetre
       #self.window.getMouse()
        
    def addPlayer(self,player): #ajoute un joueur
       self.players.append(player)
        
    def drawPlayers(self): #dessine chaque joueur (cercle)
        for p in self.players:
            print p.circle
            p.circle.draw(self.window)
