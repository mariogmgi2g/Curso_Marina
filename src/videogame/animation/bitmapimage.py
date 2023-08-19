from importlib import resources
from config import cfg_item, Config
import os
import pygame
ruta_imagen = os.path.join(
    os.path.dirname(__file__), 
    'assets/images/walking_animation.png')

class BitmapImage:

    def __init__(self):
        # self.__image = pygame.image.load(cfg_item("image", "file")).convert
        # self.__image = pygame.image.load(ruta_imagen).convert_alpha()
        self.__image = pygame.image.load(ruta_imagen).convert()

        self.__frames = []
        rect_size = cfg_item("image","rects_size")

        for i in range(cfg_item("image", "rects_per_line")):
            left = rect_size[0] * i
            top = rect_size[1] * i
            # Se almacenan las coordenadas de los sprites en los que se dividen
            # la imagen
            self.__frames.append(
                pygame.Rect(left, top, rect_size[0], rect_size[1]))
        print(len(self.__frames))


    def render(self, surface_dst, rect, pos):
        surface_dst.blit(self.__image, self.__frames[rect], pos)


if __name__ == "__main__":
    BitmapImage()

    
