import random
import time

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
DIR_STR = ["LEFT","RIGHT","UP","DOWN"]

class Point(object):
    #represente une position x et y dans le plan
    
    x=None
    y=None
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def move(self,x,y):
        self.x += x
        self.y += y
            
    def __str__(self): #affichage d'une position (console) ex: (x:0 ; y:0)
        return "(x:"+str(self.x)+" ; y:"+str(self.y)+")"
        
    def toTuple(self): #retourne un tuple (x,y)
        return (self.x,self.y)
       
class Line(object):
    #represente un segment de droite dans le plan
    
    p1 = None
    p2 = None
    
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
    def move(self,x,y):
        self.p1.move(x,y)
        self.p2.move(x,y)

class Circle(object):
    #represente un cercle dans le plan
    
    center = None
    radius = None
    
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius
        
    def move(self,x,y):
        self.center.move(x,y)
        
    def hitbox(self):
        up_right = Point(self.center.x+self.radius,self.center.y-self.radius)
        up_left =  Point(self.center.x-self.radius,self.center.y-self.radius)
        down_right = Point(self.center.x+self.radius,self.center.y+self.radius)
        down_left = Point(self.center.x-self.radius,self.center.y+self.radius)
        line_up = Line(up_right,up_left)
        line_left = Line(up_left,down_left)
        line_down = Line(down_left,down_right)
        line_right = Line(down_right,up_right)
        return [line_up,line_left,line_down,line_right]

class Rectangle(object): 
   
    pointUL= None #up - left
    pointDR = None #down - right
    color = None
    
    def __init__(self,pointUL,pointDR,color):
        self.pointUL = pointUL
        self.pointDR = pointDR
        self.color = color
       
def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)   
         
def intersects(line1, line2):
    A = line1.p1
    B = line1.p2
    C = line2.p1
    D = line2.p2
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
 
def collides(circle,lines):
    hitbox = circle.hitbox()
    for line in lines:
        for border in hitbox:
            if intersects(line,border):
                return True
    return False
    
def inside_rect(point1,rect):
    point=rect.pointUL
    point2=rect.pointDR
    print point, point1, point2
    if point1[0]>= point.x and point1[0] <= point2.x:
        if point1[1] >=point.y and point1[1]<=point2.y:
            inrect=True
        else:
            inrect=False
    else:
        inrect=False
    return inrect  
    
def rgb():
    rgb = []
    for i in range(3):
        n = random.randrange(0,255,1)
        rgb.append(n)
    return rgb 
            
def inside_line (line,little_line):
    if little_line.p1.x == little_line.p2.x or line.p1.x == line.p2.x:
        if little_line.p1.x == line.p1.x and little_line.p2.x == line.p2.x:
            if little_line.p1.y > line.p1.y and little_line.p2.y < line.p2.y:
                return True
        return False    
    else:
        if little_line.p1.x > line.p1.x and little_line.p1.y > line.p1.y:
            if little_line.p2.x < line.p2.x and little_line.p2.y < line.p2.y:
                line_y = line.p2.y-line.p1.y
                line_x = line.p2.x-line.p1.x
                little_line_y= little_line.p2.y-little_line.p1.y
                little_line_x= little_line.p2.x-little_line.p1.x
                m1= float(line_y)/line_x
                m2=  float(little_line_y)/little_line_x 
                if m1 == m2:
                    return True
        return False 

def squar(point,lines,PAS_x):
    linel = Line(Point(point.x-PAS_x/2,point.y-PAS_x/2),Point(point.x-PAS_x/2,point.y+PAS_x/2))
    liner = Line(Point(point.x+PAS_x/2,point.y-PAS_x/2),Point(point.x+PAS_x/2,point.y+PAS_x/2))
    lined = Line(Point(point.x-PAS_x/2,point.y+PAS_x/2),Point(point.x+PAS_x/2,point.y+PAS_x/2))
    lineu = Line(Point(point.x-PAS_x/2,point.y-PAS_x/2),Point(point.x+PAS_x/2,point.y-PAS_x/2))
    full_square = [linel,liner,lineu,lined]
    real_square = []
    for side in full_square:
        exists = False
        for line in lines:
            if inside_line(line,side):
                exists = True
                real_square.append(exists)
                break
        if not exists:
            real_square.append(exists)
    return real_square

def get_random_direction(d):
    direction = random.randrange(4)
    if direction == LEFT:
        return (LEFT,(-d,0))
    if direction == RIGHT:
        return (RIGHT,(d,0))
    if direction == UP:
        return (UP,(0,-d/2))
    if direction == DOWN:
        return (DOWN,(0,d/2))

def get_direction(point, radius, lines):
    while True:
        rand = get_random_direction(radius)
        test_pos = Point(point.x+rand[1][0],point.y+rand[1][1])
        m_circle = Circle(test_pos,radius)
        if not collides(m_circle,lines):
            return rand[1]
    print "move bug"
    return (0,0)
            
    
    
    
    
    
        

        
        
    square = (((point.x-PAS_x/2),(point.y-PAS_x/2)),((point.x-PAS_x/2),(point.y+PAS_x/2)),((point.x+PAS_x/2),(point.y-PAS_x/2)),())
    
