import pygame
import sys
import time
from game import Game
from level import Level
from player import *
from utils import *
from pygame.locals import *



class UserInterface(object):

    MODE=(800, 600)
    window=None
    game = None
    running = True
    in_game = False
    title = None

    
    def __init__(self):
        pygame.init()
        self.window=pygame.display.set_mode(self.MODE)
        self.window.fill((255, 255, 255))
        self.menu = Menu("Le Labyrinthe",self)
        pygame.display.flip()
        
#Display:
    def tick(self):
        if self.in_game:
            self.drawMonsters(self.game.npcs.values())
    def changeDisplay(self,display):
        self.window.fill((255, 255, 255))
        if display == "PLAY":
            self.game = Game(Level(self.MODE))
            self.drawLevel()
            self.drawMonsters(self.game.npcs.values())
            self.drawPlayers(self.game.players.values())
            self.in_game = True
        elif display == "QUIT":
            self.in_game = False
            self.running = False
        else:
            self.menu= Menu(display,self)
        pygame.display.update() 
        
    def drawPlayers(self, players):
        color = rgb()
        if type(players) == list:
            for player in players:
                pos = player.pos.toTuple()
                pygame.draw.circle(self.window,color,pos,player.size)
        else:
            pos = players.pos.toTuple()
            pygame.draw.circle(self.window,color,pos,players.size)
        pygame.display.flip()
        
    def drawMonsters(self, monsters):
        for monster in monsters:
            pos = monster.pos.toTuple()
            pygame.draw.circle(self.window,monster.color,pos,monster.size)
            pygame.draw.circle(self.window,(0,0,0),pos,monster.size/2)
        pygame.display.flip()
            
    def erasePlayer(self,player):
        pos = player.pos.toTuple()
        black = (255,255,255)
        pygame.draw.circle(self.window,black,pos,player.size)
        pygame.display.flip()
            
    def drawLevel(self):
        for line in self.game.level.lines:
            p1 = line.p1.toTuple()
            p2 = line.p2.toTuple()
            pygame.draw.line(self.window,(0,0,0),p1,p2)
        pygame.display.flip()
        
    def movePlayer(self,player,x,y):
        self.erasePlayer(player)
        player.move(x,y)
        self.drawPlayers(player) 
        
#Keyboard/Mouse:        
    def mouseEvent(self, event):
        if not self.in_game:
            self.menu.mouseEvent(event)
        
    def keyEvent(self, event):
        if event.key == pygame.K_UP:
            test_pos = Point(self.game.players[0].pos.x,self.game.players[0].pos.y-10)
            if not collides(Circle(test_pos,self.game.players[0].size),self.game.level.lines):
                self.movePlayer(self.game.players[0],0,-10)
        elif event.key == pygame.K_DOWN:
            test_pos = Point(self.game.players[0].pos.x,self.game.players[0].pos.y+10)
            if not collides(Circle(test_pos,self.game.players[0].size),self.game.level.lines):
                self.movePlayer(self.game.players[0],0,10)
        elif event.key == pygame.K_RIGHT:
            test_pos = Point(self.game.players[0].pos.x+10,self.game.players[0].pos.y)
            if not collides(Circle(test_pos,self.game.players[0].size),self.game.level.lines):
                self.movePlayer(self.game.players[0],10,0)
        elif event.key == pygame.K_LEFT:
            test_pos = Point(self.game.players[0].pos.x-10,self.game.players[0].pos.y)
            if not collides(Circle(test_pos,self.game.players[0].size),self.game.level.lines):
                self.movePlayer(self.game.players[0],-10,0)
        if event.key == pygame.K_z:
                test_pos = Point(self.game.players[1].pos.x,self.game.players[1].pos.y-10)
                if not collides(Circle(test_pos,self.game.players[1].size),self.game.level.lines):
                    self.movePlayer(self.game.players[1],0,-10)
        elif event.key == pygame.K_s:
                test_pos = Point(self.game.players[1].pos.x,self.game.players[1].pos.y+10)
                if not collides(Circle(test_pos,self.game.players[1].size),self.game.level.lines):
                    self.movePlayer(self.game.players[1],0,10)
        elif event.key == pygame.K_d:
                test_pos = Point(self.game.players[1].pos.x+10,self.game.players[1].pos.y)
                if not collides(Circle(test_pos,self.game.players[1].size),self.game.level.lines):
                    self.movePlayer(self.game.players[1],10,0)
        elif event.key == pygame.K_q:
                test_pos = Point(self.game.players[1].pos.x-10,self.game.players[1].pos.y)
                if not collides(Circle(test_pos,self.game.players[1].size),self.game.level.lines):
                    self.movePlayer(self.game.players[1],-10,0)
        print "player1: ",self.game.players[0].pos
        print "player2: ",self.game.players[1].pos

                
class Button(object):
    rectangle = None
    action = None
    text = None
    def __init__(self,rectangle,text,action):
        self.rectangle = rectangle    
        self.action = action
        self.text = text
    def bright(self):
        color = self.rectangle.color 
        bright = 1.0/2   
        red= ((255-color[0])*bright) +color[0]
        green = ((255-color[1])*bright) +color[1]   
        blue = ((255-color[2])*bright) +color[2]
        self.rectangle.color = (red,green,blue)
    def getAction(self):
        self.bright()
        return self.action
    def textRectangle(self):
        if pygame.font:
            font = pygame.font.SysFont('Arial',20)
            write = font.render(self.text, 1,(0,0,255))
            textpos = write.get_rect(center=((self.rectangle.pointUL.x+self.rectangle.pointDR.x)/2,(self.rectangle.pointUL.y+self.rectangle.pointDR.y)/2))
        return write, textpos

class Menu(object):
    title = None
    buttons = []
    ui = None
    prop_title = None
    def __init__(self,title,ui):
        self.title = title
        self.ui = ui
        self.buttons = []
        self.make()
        self.display(True)
    
    def make_buttons(self,list_names):
        n = len(list_names)
        self.prop_title= self.ui.MODE[1]/(n+1)
        prop_script= (self.ui.MODE[1]*n)/(n+1)
        nb_u=1.5+(1.5*n)
        u = prop_script/nb_u
        color = rgb()
        rect_l = (self.ui.MODE[0])/3
        rect_r = (2*self.ui.MODE[0])/3
        rect_up = self.prop_title+u
        for name in list_names:
            rect_dr= rect_up+u
            pointUL = Point(rect_l,rect_up)
            pointDR = Point(rect_r,rect_dr)
            r = Rectangle(pointUL,pointDR,color)
            if type(name) == tuple:
                b = Button(r,name[0],name[1])   
            else:
                b = Button(r,name,name)
            rect_up += u+(u/2)
            self.buttons.append(b)
            
    def make(self):
        if self.title == "Le Labyrinthe":
            self.make_buttons(["1PLAYER","MULTIPLAYER","EDITOR","CREDIT","QUIT"])
        if self.title == "1PLAYER":
            self.make_buttons(["DIFFICULTE","AVATAR","SEED","GAME TYPE","PLAY",("BACK","Le Labyrinthe")])
        if self.title == "MULTIPLAYER":
            self.make_buttons(["DIFFICULTE","AVATAR","SEED","GAME TYPE","PLAY",("BACK","Le Labyrinthe")])
        if self.title == "EDITOR":
            self.make_buttons(["WIGHT","HIGHT","SEED","GENERATE",("BACK","Le Labyrinthe")])
        if self.title=="CREDIT":
            self.make_buttons(["FUCK IT"])
        if self.title == "QUIT":
            pygame.quit       
        if self.title == "DIFFICULTE":
            self.make_buttons(["EASY","MEDIUM","HARD"])
        if self.title == "AVATAR":
            self.make_buttons(["AVATAR_1","AVATAR_2","AVATAR_3"])
        if self.title == "SEED":
            input("seed:")
        if self.title == "GAME TYPE":
            self.make_buttons(["CHRONO","VERSUS","SURVIVAL"])
        
    def display(self,pushed):
        self.ui.window.fill(rgb())
        font = pygame.font.SysFont('Arial',50)
        text = font.render(self.title, 1,rgb())
        textpos = text.get_rect(center=(self.ui.MODE[0]/2,self.prop_title/2))
        self.ui.window.blit(text,textpos)
        for button in self.buttons:
            x = button.rectangle.pointUL.x
            y = button.rectangle.pointUL.y
            w = self.ui.MODE[0]/3
            h = button.rectangle.pointDR.y-button.rectangle.pointUL.y
            if pushed:
                pygame.draw.rect(self.ui.window,rgb(),(x,y,w+2,h+2))
            else:
                pygame.draw.rect(self.ui.window,rgb(),(x-2,y-2,w+2,h+2))
            pygame.draw.rect(self.ui.window,button.rectangle.color,(x,y,w,h))
            t=button.textRectangle()
            self.ui.window.blit(t[0],t[1])

            pygame.display.flip()   
            pygame.display.update()
        
        
    def mouseEvent(self, event):
        for button in self.buttons:        
            if inside_rect(event.pos,button.rectangle):
                a = button.getAction()
                self.display(False)
                time.sleep(0.5)
                self.ui.changeDisplay(a)
        
            
