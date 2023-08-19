import pygame

from config import cfg_item
from bitmapimage import BitmapImage

class Scroll:
    def __init__(self):
        self.__rect = cfg_item("scroll", "image")
        self.__pos = pygame.math.Vector2(
            cfg_item("game", "screen_size")[0], 
            (cfg_item("game", "screen_size")[1] / 2))
        self.__image = BitmapImage()


    def update(self, delta_time):
        self.__pos.x -= cfg_item("scroll", "speed") * delta_time


    def render(self, surface_dst):
        for i in range(self.__rect):
            print(f'Iteracion: {i}')
            self.__image.render(
                surface_dst, 
                i,
                (self.__pos.x, # + i * cfg_item("image","rects_size")[0],
                    self.__pos.y))

