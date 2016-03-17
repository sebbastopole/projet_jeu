class Point(object):
    #represente une position x et y dans le plan
    
    x=int()
    y=int()
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def move(self,x,y):
        self.x += x
        self.y += y
            
    def __str__(self): #affichage d'une position (console) ex: (x:0-y:0)
        return "(x:"+str(self.x)+"-y:"+str(self.y)+")"
        
    def toTuple(self): #retourne un tuple (x,y)
        return (self.x,self.y)
       
class Line(object):
    #represente un segment de droite dans le plan
    
    p1 = Point()
    p2 = Point()
    
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def move(self,x,y):
        self.p1.move(x,y)
        self.p2.move(x,y)
    def getDirection(self):
        if self.p2.x != self.p1.x:
            return float((self.p2.y-self.p1.y))/(self.p2.x-self.p1.x)
        return "NaN"
    def getOffset(self):
        return self.p1.y-(self.getDirection()*self.p1.x)

class Circle(object):
    #represente un cercle dans le plan
    
    center = Point()
    radius = int()
    
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius
    def move(self,x,y):
        self.center.move(x,y)
    def hitbox(self):
        up_right = Point(self.center.x-self.radius,self.center.y-self.radius)
        up_left =  Point(self.center.x+self.radius,self.center.y-self.radius)
        down_right = Point(self.center.x-self.radius,self.center.y+self.radius)
        down_left = Point(self.center.x+self.radius,self.center.y+self.radius)
        line_up = Line(up_right,up_left)
        line_left = Line(up_left,down_left)
        line_down = Line(down_left,down_right)
        line_right = Line(down_right,up_right)
        return [line_up,line_left,line_down,line_right]
        
def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)   
         
def intersects(line1, line2):
    A = line1.p1
    B = line1.p2
    C = line2.p1
    D = line2.p2
    print A,B,C,D
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
    return False
 
def collides(circle,lines):
    hitbox = circle.hitbox()
    for line in lines:
        for border in hitbox:
            if intersects(line,border):
                return True
    return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
