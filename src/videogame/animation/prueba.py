import os
import pygame
from config import cfg_item
# Dimensiones del spritesheet 640x256 (anchoxalto)
 
class SpriteSheet:
    """Función que selecciona el sprite adecuado de spritesheet"""
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        width = self.sprite_sheet.get_width()
        tamanio = self.sprite_sheet.get_size()
        print(f"SPRITE SHEET| Tamaño: {tamanio}, anchura: {width}")
    
    def get_sprite(self, x, y, w, h):
        """Función que escoge el sprite de la spritesheet
        w y h son las dimensiones del sprite individual, mientras que x e y es
        donde se encuentran en el spritesheet tomando como referencia el punto
        (0, 0) la esquina superior izquierda relativa"""
        sprite = pygame.Surface((w, h))
        # Devuelve la imagen que queremos del sprite según la posición y 
        # las dimentsiones y las pinta en el canvas
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        width = sprite.get_width()
        tamanio = sprite.get_size()
        print(f"SPRITE| Tamaño: {tamanio}, anchura: {width}")
        return sprite
    
    # def parse_sprite(self, name):


####
if __name__ == '__main__':
    pygame.init()
    DISPLAY_W, DISPLAY_H = cfg_item("game", "screen_size")
    canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
    window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    running = True

ruta_imagen = os.path.join(
    os.path.dirname(__file__), 'assets/images/walking_animation.png')
h, w = cfg_item("image", "rects_size")
my_spritesheet = SpriteSheet(ruta_imagen)

# Como de ancho el spritesheet mide 640 pixeles, se va desplazando la anchura 
# proporcionalmente
chica_derecha = [my_spritesheet.get_sprite(w*i, 0, w, h) for i in range(10)]
chica_izquierda = [my_spritesheet.get_sprite(w*i, h, w, h) for i in range(10)]
chica_movimientos = {0: chica_derecha, 1: chica_izquierda}
# 0: movimiento derecha; 1: movimiento izquierda

sprite1 = my_spritesheet.get_sprite(0, 0, w, h)
# sprite1 = my_spritesheet.get_sprite(0, 0, 640, 256)

index = 0
direccion = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direccion = 0
                index = (index + 1) % len(chica_derecha)
            if event.key == pygame.K_LEFT:
                direccion = 1
                index = (index + 1) % len(chica_izquierda)

    canvas.fill((255, 255, 255))
    # La segunda dupla de valores del blit controla dónde se materializa el
    # sprite con referencia del canvas, siendo su esquina superior izquierda
    # el punto 0, 0
    canvas.blit(chica_movimientos[direccion][index], (0, 0))
    window.blit(canvas, (0, 0))
    pygame.display.update()