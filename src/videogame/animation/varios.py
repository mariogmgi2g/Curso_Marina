import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

# Creación de la ventana
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Walking Animation")

# Carga de la imagen de la animación
animation_image = pygame.image.load("walking_animation.png")
animation_width = 64  # Anchura de cada frame de la animación
animation_height = 129  # Altura de cada frame de la animación

# Variables de posición y dirección
character_x = 0
character_y = WINDOW_HEIGHT - animation_height
character_direction = 1  # 1 para derecha, -1 para izquierda

# Variables para controlar la animación
frame_index = 0
frame_counter = 0
frame_delay = 5  # Retraso entre frames (ajustable)

# Bucle principal del programa
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Cambio de dirección cuando se alcanza el borde de la pantalla
    if character_x <= 0 or character_x >= WINDOW_WIDTH - animation_width:
        character_direction *= -1

    # Actualización de la posición del personaje
    character_x += character_direction

    # Actualización del contador de frames
    frame_counter += 1
    if frame_counter >= frame_delay:
        frame_index = (frame_index + 1) % 4  # 4 frames en la animación
        frame_counter = 0

    # Pintado de la ventana y dibujado del personaje
    window.fill((255, 255, 255))  # Color de fondo blanco
    current_frame = pygame.Rect(
        frame_index * animation_width,
        0,
        animation_width,
        animation_height,
    )
    window.blit(animation_image, (character_x, character_y), current_frame)

    pygame.display.flip()
