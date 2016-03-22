import pygame
import sys
from entity import *
from level import *
from utils import *
from game import *

#display:
BACKGROUND_COLOR = rgb()
TITLE_COLOR = (25,25,25)
BUTTONS_COLOR = (200,0,50)
LEVEL_COLOR = (0,0,0)
GAME_TITLE = "Le Labyrinthe"
BORDER_SIZE = 2

#controls:
MOVE_STEP = 3

class UserInterface(object):

    MODE=(800, 600)
    window=None
    game = None
    title = None
    running = True
    in_game = False
    moved = False
    
    def __init__(self):
        pygame.init()
        self.window=pygame.display.set_mode(self.MODE)
        self.window.fill(BACKGROUND_COLOR)
        self.menu = Menu(GAME_TITLE,self)
        pygame.display.flip()
        
#Display:
    def update(self):
        if self.moved:
            self.window.fill(BACKGROUND_COLOR)
            self.drawLevel()
            for monster in self.game.npcs.values():
                self.drawMonster(monster)
            for player in self.game.players.values():
                self.drawPlayer(player)
            self.moved = False
            
    def changeDisplay(self,display):
        self.window.fill(BACKGROUND_COLOR)
        if display == "PLAY":
            self.game = Game(self)
            self.in_game = True
            self.drawLevel()
            self.game.start()
        elif display == "QUIT":
            self.in_game = False
            self.running = False
        else:
            self.menu= Menu(display,self)
        pygame.display.update() 
        
    def drawPlayer(self, players):
        pos = players.pos.toTuple()
        pygame.draw.circle(self.window,players.color,pos,players.size)
        pygame.display.flip()
        
    def drawMonster(self, monster):
        pos = monster.pos.toTuple()
        pygame.draw.circle(self.window,monster.color,pos,monster.size)
        pygame.draw.circle(self.window,(0,0,0),pos,monster.size/3)
        pygame.display.flip()
            
    def erasePlayer(self,player):
        pos = player.pos.toTuple()
        pygame.draw.circle(self.window,BACKGROUND_COLOR,pos,player.size)
        pygame.display.flip()
        
    def eraseMonster(self, monster):
        pos = monster.pos.toTuple()
        pygame.draw.circle(self.window,BACKGROUND_COLOR,pos,monster.size) 
        pygame.display.flip()
             
    def drawLevel(self):
        for line in self.game.level.lines:
            p1 = line.p1.toTuple()
            p2 = line.p2.toTuple()
            pygame.draw.line(self.window,LEVEL_COLOR,p1,p2)
        pygame.display.flip()
         
        
#Keyboard/Mouse:        
    def mouseEvent(self, event):
        if not self.in_game:
            self.menu.mouseEvent(event)
        
    def keyEvent(self, event):
        if event.key == pygame.K_UP:
            self.movePlayer(0,(0,-1))
        elif event.key == pygame.K_DOWN:
            self.movePlayer(0,(0,1))
        elif event.key == pygame.K_RIGHT:
            self.movePlayer(0,(1,0))
        elif event.key == pygame.K_LEFT:
            self.movePlayer(0,(-1,0))
        if event.key == pygame.K_z:
            self.movePlayer(1,(0,-1))   
        elif event.key == pygame.K_s:
            self.movePlayer(1,(0,1))    
        elif event.key == pygame.K_d:
            self.movePlayer(1,(1,0))    
        elif event.key == pygame.K_q:
            self.movePlayer(1,(-1,0))    

    def movePlayer(self,pId,move):
        player = self.game.players[pId]
        v_x = move[0]*MOVE_STEP
        v_y = move[1]*MOVE_STEP
        p_x = player.pos.x + v_x
        p_y = player.pos.y + v_y
        test_pos = Point(p_x,p_y)
        p_circle = Circle(test_pos,player.size)
        if not collides(p_circle,self.game.level.lines):
            player.move(v_x,v_y)
            self.moved = True
                
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
        bright = 0.33  
        red= ((255-color[0])*bright) +color[0]
        gre= ((255-color[1])*bright) +color[1]   
        blu= ((255-color[2])*bright) +color[2]
        self.rectangle.color = (red,gre,blu)
        
    def getAction(self):
        self.bright()
        return self.action
        
    def textRectangle(self):
        if pygame.font:
            font = pygame.font.SysFont('Arial',20)
            write = font.render(self.text, 1,(0,0,255))
            x = (self.rectangle.pointUL.x+self.rectangle.pointDR.x)/2
            y = (self.rectangle.pointUL.y+self.rectangle.pointDR.y)/2
            textpos = write.get_rect(center=(x,y))
        return write,textpos

class Menu(object):

    ui = None
    title = None
    buttons = []
    
    def __init__(self,title,ui):
        
        self.ui = ui
        self.title = title
        self.buttons = []
        self.make()
        self.display(True)
    
    def make_buttons(self,list_names):
        n = len(list_names)
        prop_title= self.ui.MODE[1]/(n+1)
        prop_script= (self.ui.MODE[1]*n)/(n+1)
        nb_u=1.5+(1.5*n)
        u = prop_script/nb_u
        color = BUTTONS_COLOR
        rect_l = (self.ui.MODE[0])/3
        rect_r = (2*self.ui.MODE[0])/3
        rect_up = prop_title+u
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
            self.make_buttons([
            "1PLAYER",
            "MULTIPLAYER",
            "EDITOR",
            "CREDIT",
            "QUIT"])
            
        if self.title == "1PLAYER":
            self.make_buttons([
            "PLAY",
            "DIFFICULTE",
            "AVATAR",
            "SEED",
            "GAME TYPE",
            ("BACK","Le Labyrinthe")])
            
        if self.title == "MULTIPLAYER":
            self.make_buttons([
            "DIFFICULTE",
            "AVATAR",
            "SEED",
            "GAME TYPE",
            "PLAY",
            ("BACK","Le Labyrinthe")])
            
        if self.title == "EDITOR":
            self.make_buttons([
            "WIDTH",
            "HIGHT",
            "SEED",
            "GENERATE",
            ("BACK","Le Labyrinthe")])
            
        if self.title=="CREDIT":
            self.make_buttons([
            "FUCK IT"])
            
        if self.title == "DIFFICULTE":
            self.make_buttons([
            "EASY",
            "MEDIUM",
            "HARD"])
            
        if self.title == "AVATAR":
            self.make_buttons([
            "AVATAR_1",
            "AVATAR_2",
            "AVATAR_3"])
            
        if self.title == "SEED":
            input("seed:")
            
        if self.title == "GAME TYPE":
            self.make_buttons([
            "CHRONO",
            "VERSUS",
            "SURVIVAL"])
        
    def display(self,pushed):
        self.ui.window.fill(BACKGROUND_COLOR)
        prop_title= self.ui.MODE[1]/(len(self.buttons)+1)
        font = pygame.font.SysFont('Arial',50) #TODO taille adaptee
        text = font.render(self.title, 1,TITLE_COLOR)
        textpos = text.get_rect(center=(self.ui.MODE[0]/2,prop_title/2))
        self.ui.window.blit(text,textpos)
        for button in self.buttons:
            x = button.rectangle.pointUL.x
            y = button.rectangle.pointUL.y
            w = self.ui.MODE[0]/3
            h = button.rectangle.pointDR.y-button.rectangle.pointUL.y
            wb = w+BORDER_SIZE
            hb = h+BORDER_SIZE
            if pushed:
                pygame.draw.rect(self.ui.window,(0,0,0),(x,y,wb,hb))
            else:
                xb = x-BORDER_SIZE
                yb = y-BORDER_SIZE
                pygame.draw.rect(self.ui.window,(0,0,0),(xb,yb,wb,hb))
            pygame.draw.rect(self.ui.window,button.rectangle.color,(x,y,w,h))
            self.ui.window.blit(*button.textRectangle())
            pygame.display.flip()   
            pygame.display.update()
        
    def mouseEvent(self, event):
        for button in self.buttons:        
            if inside_rect(event.pos,button.rectangle):
                a = button.getAction()
                self.display(False)
                time.sleep(0.05)
                self.ui.changeDisplay(a)
        
            
