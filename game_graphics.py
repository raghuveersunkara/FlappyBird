import pygame
import neat
import os


class GraphicsSetup:

    WIN_WIDTH = 600
    WIN_HEIGHT = 800

    BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
                pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
                pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png')))]
    PIPE_IMGS = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
    BASE_IMGS = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
    BG_IMGS = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))

    def __init__(self):
        super().__init__()

        self.win_width = self.WIN_WIDTH
        self.win_height = self.WIN_HEIGHT

        self.bird_imgs = self.BIRD_IMGS

        self.pipe_imgs = self.PIPE_IMGS
        self.base_imgs = self.BASE_IMGS
        self.bg_imgs = self.BG_IMGS


graphics_setup = GraphicsSetup()
