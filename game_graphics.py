import pygame
import neat

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
            pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png')))]

PIPE_IMGS = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
BASE_IMGS = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BG_IMGS = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
