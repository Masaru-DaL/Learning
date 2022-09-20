import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("Pygame テスト")
    screen = pygame.display.set_mode((400,300))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)
    timer = 0
    
    while True:
        timer += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        text = font.render(str(timer/10), True, (255,255,255))
        screen.fill((0,0,0))
        screen.blit(text, [150, 120])
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
