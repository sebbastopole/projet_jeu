from game_ui import *
from player import *

def main():
    ui = UserInterface()
    player = Player(0,50)
    player.move(50,50)
    ui.addPlayer(player)
    ui.drawPlayers()
    
main()

while(1):
    pass
#bonjour j'ai fait une modif
