﻿import pygame
import os
import random
pygame.font.init()
WIDTH, HEIGHT = 1100, 700 #Size of main window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))#Main window initialize
pygame.display.set_caption("Blackjack")#Name on window
windowiconpath = os.path.join('Assets', 'ag3aw-nd7nh-001.ico')
windowicon = pygame.image.load(windowiconpath)
pygame.display.set_icon(windowicon)#Icon image next to window name
FPS = 30
CARDWIDTH, CARDHEIGHT = 125, 175
GAMEFONT = pygame.font.SysFont('rockwellextra', 20)
WHITE = 255,255,255
BLACK = 0,0,0
class Card:
    def __init__(self, cardName, cardValue, cardImage):
        self.cardName = cardName
        self.cardValue = int(cardValue)
        self.cardImage = cardImage

class CardDeck:
    def __init__(self):
        self.deck = []
        types = ['spades', 'clubs', 'diamonds', 'hearts']
        values = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
        for suit in types:
            for value in values:
                if value in ['j', 'q', 'k']:
                    card_value = 10
                elif value == 'a':
                    card_value = 11
                else:
                    card_value = int(value)
                card_name = value + suit
                card_image_path = os.path.join('Assets', f'{value}_of_{suit}.png')
                card_image = pygame.image.load(card_image_path)
                card_image = pygame.transform.scale(card_image, (CARDWIDTH, CARDHEIGHT))
                self.deck.append(Card(card_name, card_value, card_image))
        self.current_index = 0

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.deck):
            raise StopIteration
        else:
            card = self.deck[self.current_index]
            self.current_index += 1
            return card

def dealcard(playerCards, dealerCards, deck, addtoHand):
    while True:
        index = random.randint(0, 51)
        if deck.deck[index] not in playerCards and deck.deck[index] not in dealerCards:
            addtoHand.append(deck.deck[index])
            break
    return addtoHand
def drawStartMenu():
    WIN.fill((110, 153, 70))
    #lucidafax rockwellextra bookmanoldstyle
    TITLEFONT = pygame.font.SysFont('rockwellextra', 100)
    MENUFONT = pygame.font.SysFont('rockwellextra', 40)
    title = TITLEFONT.render('Blackjack', 1, BLACK)
    start_button = MENUFONT.render('Space - Start', 1, BLACK)
    save_button = MENUFONT.render('S - Save', 1, BLACK)
    quit_button = MENUFONT.render('ESC - Quit', 1, BLACK)
    rules_button = MENUFONT.render('R - Rules', 1, BLACK)
    WIN.blit(title, (200, 100))
    WIN.blit(start_button, (WIDTH/2 - start_button.get_width()/2, 300))
    WIN.blit(save_button, (WIDTH/2 - start_button.get_width()/2, 350))
    WIN.blit(rules_button, (WIDTH/2 - start_button.get_width()/2, 400))
    WIN.blit(quit_button, (WIDTH/2 - start_button.get_width()/2, 450))


    blackjackimagepath = os.path.join('Assets', 'Blackjack-icon.png')
    blackjackimage = pygame.image.load(blackjackimagepath)
    blackjackimage = pygame.transform.scale(blackjackimage, (200, 200))
    WIN.blit(blackjackimage, (800, 50))

    pygame.display.update()

def drawCardsgetTotal(playerCards, dealerCards, state):
    WIN.fill((110, 153, 70))#Background green
    dealertotal, playertotal = calculateTotal(dealerCards, playerCards)
    if state == 'show':
    # draw player cards
        x = 50
        y = 50
        for card in playerCards:
            WIN.blit(card.cardImage, (x, y))
            x += 10 + CARDWIDTH
        x = 50
        y = 50 + CARDHEIGHT + 50
        for card in dealerCards:
            WIN.blit(card.cardImage, (x, y))
            x += 10 + CARDWIDTH
        playerprinttotal = GAMEFONT.render('Total: '+str(playertotal), 1, BLACK)
        dealerprinttotal = GAMEFONT.render('Total: '+str(dealertotal), 1, BLACK)
        WIN.blit(playerprinttotal, (50,235))
        WIN.blit(dealerprinttotal, (50,460))
        balance = GAMEFONT.render('Playerbalance is:      Dealerbalance is:', 1, BLACK)
        WIN.blit(balance, (50,20))
        pygame.display.update()
        return playertotal, dealertotal

    elif state == 'hide':
        x = 50
        y = 50
        for card in playerCards:
            WIN.blit(card.cardImage, (x, y))
            x += 10 + CARDWIDTH
        x = 50
        y = 50 + CARDHEIGHT + 50
        WIN.blit(dealerCards[0].cardImage, (x, y))
        x += 10 + CARDWIDTH
        card_image_path = os.path.join('Assets', 'backside.png')
        card_image = pygame.image.load(card_image_path)
        card_image = pygame.transform.scale(card_image, (CARDWIDTH, CARDHEIGHT))
        WIN.blit(card_image, (x, y))
        playerprinttotal = GAMEFONT.render('Total: '+str(playertotal), 1, BLACK)
        dealerprinttotal = GAMEFONT.render('Total: '+str(dealerCards[0].cardValue)+' + ??', 1, BLACK)
        WIN.blit(playerprinttotal, (50,235))
        WIN.blit(dealerprinttotal, (50,460))
        balance = GAMEFONT.render('Playerbalance is:      Dealerbalance is:', 1, BLACK)
        WIN.blit(balance, (50,20))
        pygame.display.update()
        return playertotal, dealertotal



#Calculate value of all cards
def calculateTotal(dealerCards, playerCards):
    dealertotal = 0
    dealeraces = 0
    for card in dealerCards:
        if card.cardValue == 11:
            dealeraces += 1
        dealertotal += card.cardValue
    while dealeraces > 0 and dealertotal > 21:
        dealertotal -= 10
        dealeraces -= 1
    
    playertotal = 0
    playeraces = 0
    for card in playerCards:
        if card.cardValue == 11:
            playeraces += 1
        playertotal += card.cardValue
    while playeraces > 0 and playertotal > 21:
        playertotal -= 10
        playeraces -= 1
    return dealertotal, playertotal

def checkWinner(playertotal, dealertotal):
    #TODO: fix bet and balances later
    bet = 0
    playerbalance = 0
    dealerbalance = 0
    PRINTTEXT = ''
    if playertotal > 21: 
        PRINTTEXT = 'Bust! Dealer wins.'
        playerbalance -= bet
        dealerbalance += bet
    elif playertotal == 21 and dealertotal != 21:
        PRINTTEXT = "Blackjack! You win"
        #0.5 added so it doesnt round down when betting odd and converting to int
        winnings = bet * 3/2+0.5
        winnings = int(winnings)
        playerbalance += winnings
        dealerbalance -= winnings
    elif dealertotal > 21:
        PRINTTEXT = "You win!"
        playerbalance += bet
        dealerbalance -= bet
    elif playertotal == dealertotal:
        PRINTTEXT = "Push, nobody wins"
    elif playertotal > dealertotal:
        PRINTTEXT = "You win!"
        playerbalance += bet
        dealerbalance -= bet
    elif playertotal < dealertotal:
        PRINTTEXT = "You lose!"
        playerbalance -= bet
        dealerbalance += bet
    PRINTTEXT = GAMEFONT.render(PRINTTEXT, 1, BLACK)
    WIN.blit(PRINTTEXT, (50, 500))
    pygame.display.update()
    pygame.time.delay(2000)
    return playerbalance, dealerbalance 

def dealerTurn(playerCards, dealerCards, deck, playertotal, dealertotal):
    while dealertotal < 17:
        dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
        playertotal, dealertotal = drawCardsgetTotal(playerCards, dealerCards, 'show')
        pygame.time.delay(1000)
    
    
    dealertotal, playertotal = calculateTotal(dealerCards, playerCards)
    playerbalance, dealerbalance = checkWinner(playertotal, dealertotal)
    return playerbalance, dealerbalance
#TODO: Make main menu
##TODO: make dealer turn function
#TODO: make balance and betting functions
#TODO: Implement rules and save from main menu
#TODO: Make game over/win function
def main():
    GAMESTATE = "start_menu"
    #initialize deck and players/dealer hands
    deck = CardDeck() 
    playerCards = []
    dealerCards = []
    #deals two cards to each
    playerCards = dealcard(playerCards, dealerCards, deck, playerCards) 
    playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
    dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
    dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
    playerbalance = 50
    dealerbalance = 100
    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(FPS)#update window at 30 frames per second
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for QUIT event. If QUIT, then set running to false.
            if event.type == pygame.QUIT:
                pygame.quit()

            if GAMESTATE == "start_menu":
                drawStartMenu()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        GAMESTATE = "game"
                        #game_over = False
                    if event.key == pygame.K_s:#NYI
                        ()
                    if event.key == pygame.K_r:#NYI
                        ()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        #game_over = False

            elif GAMESTATE == "game":

                    WIN.fill((110, 153, 70))#Background green
                    #prints out the the cards, hidding the dealer's second card
                    playertotal, dealertotal = drawCardsgetTotal(playerCards, dealerCards, 'hide')

                    if playertotal == 21 or dealertotal == 21:
                        playertotal, dealertotal = drawCardsgetTotal(playerCards, dealerCards, 'show')
                        checkWinner(playertotal, dealertotal)
                        running = False
                        break

                    #keys_pressed = pygame.key.get_pressed()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:#hit
                            playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
                            playertotal, dealertotal = drawCardsgetTotal(playerCards, dealerCards, 'hide')
                            if playertotal > 21:
                                playertotal, dealertotal = drawCardsgetTotal(playerCards, dealerCards, 'show')
                                checkWinner(playertotal, dealertotal)
                                running = False
                                break
                            elif playertotal == 21:
                                dealerTurn(playerCards, dealerCards, deck, playertotal, dealertotal)
                                running = False
                                break
                            else:
                                continue
                    
                        if event.key == pygame.K_s:#stand
                            playertotal, dealertotal = drawCardsgetTotal(playerCards, dealerCards, 'show')
                            dealerTurn(playerCards, dealerCards, deck, playertotal, dealertotal)
                            running = False
                            break
                    
                        if event.key == pygame.K_d:#left
                    
                            playertotal, dealertotal = drawCardsgetTotal(playerCards, dealerCards, 'hide')
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            break

    #GAMESTATE = "start_menu"
    main()

if __name__ == "__main__":
    main()

