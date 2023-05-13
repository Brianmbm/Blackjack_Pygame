import pygame
import os
import random

WIDTH, HEIGHT = 1100, 700 #Size of main window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))#Main window initialize
pygame.display.set_caption("Blackjack")#Name on window
FPS = 30
CARDWIDTH, CARDHEIGHT = 125, 175

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

def printCards(playerCards, dealerCards, state):
    WIN.fill((110, 153, 70))#Background green
    
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
    # draw dealer cards

    
    pygame.display.update()

def main():
    #initialize deck and players/dealer hands
    deck = CardDeck() 
    playerCards = []
    dealerCards = []

    #deals two cards to each
    playerCards = dealcard(playerCards, dealerCards, deck, playerCards) 
    playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
    dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
    dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)

    #prints out the the cards, hidding the dealer's second card
    printCards(playerCards, dealerCards, 'hide')
    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(FPS)#update window at 30 frames per second
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for QUIT event. If QUIT, then set running to false.
            if event.type == pygame.QUIT:
                running = False
            #keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:#hit
                    playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
                    printCards(playerCards, dealerCards, 'hide')
                    
                if event.key == pygame.K_s:#stand
                    printCards(playerCards, dealerCards)
                    
                if event.key == pygame.K_d:#left
                    
                    printCards(playerCards, dealerCards)
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break

    pygame.quit()

if __name__ == "__main__":
    main()

