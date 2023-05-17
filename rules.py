import pygame
import Blackjack_Pygame
RULESFONT = pygame.font.SysFont('rockwellextra', 18)
RED = Blackjack_Pygame.RED

def rules_render():
    rulesstring = """Rules of Blackjack
===================
The hand with the highest total wins as long as it doesn't exceed 21. 
A hand with a higher total than 21 is said to bust.
Cards 2 through 10 are worth their face value, and face cards (jack, queen, king) are also worth 10. 
An ace's value is 11 unless this would a bust, in which case it is worth 1.
The goal of each player is to beat the dealer by having the higher, unbusted hand. 
If the player busts he loses, even if the dealer also busts.
If both the player and the dealer have the same point value, neither win the hand.
The dealer gives two cards to each player, including himself.
One of the dealer's two cards is face-up, and the other is face down.
The play goes as follows:
If the dealer has blackjack and the player doesn't, the player automatically loses.
If the player has blackjack and the dealer doesn't, the player automatically wins.
If both the player and dealer have blackjack then it's a push.
If neither side has blackjack, then the player plays out his hand.
When the player has finished the dealer plays his hand.
The player's options are:
   - Hit: Take another card.
   - Stand: Take no more cards.
   - Double down: Double the wager, take exactly one more card, and then stand.
The player's turn is over after deciding to stand, doubling down to take a single card, or busting.
If the player busts, they lose the bet even if the dealer goes on to bust.
When the player is done the dealer then reveals his or her hidden hole card and plays the hand. 
House rules say that the dealer must hit until at least 17, regardless of what the player has.
Blackjack has a 3:2 payout, the rest has a 1:1 payout on the bet.
"""

    ruleslist = rulesstring.split('\n')
    Blackjack_Pygame.WIN.fill(Blackjack_Pygame.BACKGROUNDGREEN)
    backtomenu = "Press ENTER to go back to the main menu"
    backtomenu = RULESFONT.render(backtomenu, 1, RED)
    Blackjack_Pygame.WIN.blit(backtomenu,(15, 665))
    i = 0
    x = 15
    y = 12
            
    for line in ruleslist:
        ruleslist[i] = RULESFONT.render(ruleslist[i], 1, Blackjack_Pygame.BLACK)
        Blackjack_Pygame.WIN.blit(ruleslist[i], (x,y))
        y+=25
        i+=1
    
    pygame.display.update()
    pygame.time.delay(2000)
    rulesrunning = True
    while rulesrunning == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Blackjack_Pygame.GAMESTATE = "start_menu"
                    rulesrunning = False
                    return Blackjack_Pygame.GAMESTATE
    
        
