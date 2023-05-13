import pygame
import os

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

def draw_window(card):
    WIN.fill((110, 153, 70))#Background green
    WIN.blit(card.cardImage,(50,50 ))
    pygame.display.update()

def main():
    deck = CardDeck() #initialize deck
    card = pygame.Rect(50,50,CARDWIDTH, CARDHEIGHT)#First nr is x, second y(position), other is size of rectangel
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
                    draw_window(deck.__next__())
                    card.x-=1
                if event.key == pygame.K_s:#stand
                    draw_window(deck.__next__())
                    card.x-=1
                if event.key == pygame.K_d:#left
                    card.x-=1
                    draw_window(deck.__next__())

    pygame.quit()

if __name__ == "__main__":
    main()

