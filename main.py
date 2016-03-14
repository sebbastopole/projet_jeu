from game_ui import *
from player import *

def main():
    ui = UserInterface() #init interface utilisateur
    player = Player(0,10) #init player 0 avec taille 10
    player.move(50,50) 
    ui.addPlayer(player)
    ui.drawPlayers()
    i=0
    while(i<100): #boucle pour mouvement
        time.sleep(0.5) #attendre 0.5s
        player.move(10,10)
        i+=1
    
main()
while(1): #empeche fermeture fenetre (temporaire)
    pass
