from bird import Bird
from game_graphics import graphics_setup
import pygame


def draw_window(win, bird):
    win.blit(graphics_setup.bg_imgs, (0, 0))
    bird.draw(win)

    pygame.display.update()
    

if __name__ == '__main__':
    
    bird = Bird(200, 200)
    win = pygame.display.set_mode((graphics_setup.win_width, graphics_setup.win_height))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window(win, bird)

    pygame.quit()
    quit()        
