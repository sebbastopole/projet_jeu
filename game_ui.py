import pygame
from level import Level
from player import Player
from utils import Point



class UserInterface(object):

    
    window=None #fenetre du jeu
    level = None
    p1 = Player(1,Point(400,300))
    p2 = Player(2,Point(450,300))

    
    def __init__(self):
        self.window=pygame.display.set_mode((800, 600))
        self.window.fill((255, 255, 255)) #Ecran blanc
        pygame.display.flip()
             
    def setLevel(self,level):
        self.level = level   
        
    def drawPlayer(self, player):
        color = player.p_color
        pos = player.pos.toTuple()
        pygame.draw.circle(self.window,color,pos,player.size)
        pygame.display.flip()
        
    def erasePlayer(self,player):
        pos = player.pos.toTuple()
        black = (255,255,255)
        pygame.draw.circle(self.window,black,pos,player.size)
        pygame.display.flip()
            
    def drawLevel(self):
        for line in self.level.lines:
            p1 = line.p1.toTuple()
            p2 = line.p2.toTuple()
            pygame.draw.line(self.window,(0,0,0),p1,p2)
        pygame.display.flip() #applique modification a l ecran
        
    def movePlayer(self,player,x,y):
        self.erasePlayer(player)
        player.move(x,y)
        self.drawPlayer(player) 
    def event(self, event):
        if event.key == pygame.K_UP:
            self.movePlayer(self.p1,0,-5)
        elif event.key == pygame.K_DOWN:
            self.movePlayer(self.p1,0,5)
        elif event.key == pygame.K_RIGHT:
            self.movePlayer(self.p1,5,0)
        elif event.key == pygame.K_LEFT:
            self.movePlayer(self.p1,-5,0)
        if event.key == pygame.K_z:
            self.movePlayer(self.p2,0,-5)
        elif event.key == pygame.K_s:
            self.movePlayer(self.p2,0,5)
        elif event.key == pygame.K_d:
            self.movePlayer(self.p2,5,0)
        elif event.key == pygame.K_q:
            self.movePlayer(self.p2,-5,0)
        print "player1: ",self.p1.pos
        print "player2: ",self.p2.pos
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
