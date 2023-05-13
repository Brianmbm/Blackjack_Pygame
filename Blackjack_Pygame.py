import pygame

WIDTH, HEIGHT = 900, 500#Size of main window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))#Main window initialize
pygame.display.set_caption("Blackjack")#Name on window

def main():
    running = True
    while running:
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for QUIT event. If QUIT, then set running to false.
            if event.type == pygame.QUIT:
                running = False
            WIN.fill((110, 153, 70))#Background green
            pygame.display.update()
if __name__ == "__main__":
    main()

pygame.quit()
