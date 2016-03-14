from game_ui import *
from player import *

def main():
    ui = UserInterface()
    player = Player(0,500)
    player.move(50,50)
    ui.addPlayer(player)
    ui.drawPlayers()
    i=0
    while(i<10000):
        time.sleep(1)
        player.move(10,10)
        i+=1
    
main()

while(1):
    pass
#bonjour j'ai fait une modif
