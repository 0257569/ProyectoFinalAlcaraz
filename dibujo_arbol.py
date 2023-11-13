import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Circle in Pygame")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the circle parameters
profundidad = 5
cantidadLimiteNodosUltimoNivel = 2**profundidad
nodosNivel = 1
radius = width/(cantidadLimiteNodosUltimoNivel*2)
espacioVacioHeight = height - profundidad*radius
espacioVacioWidth = width - cantidadLimiteNodosUltimoNivel*radius
print("El espacio vacio es de: ", espacioVacioWidth)
level = []
columnas = []
columnas.append(radius)
level.append(radius)
#Code for stablishing the heights of the levels
for i in range(profundidad - 1):
    level.append(level[i] + (radius*2) + (espacioVacioHeight/profundidad)) 

for i in range(cantidadLimiteNodosUltimoNivel - 1):
    columnas.append(columnas[i] + (radius*2)) 

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)

    # Draw the circle
    for i in range(len(level)):
        nodosNivel = 2**i
        for k in range(nodosNivel):
            pygame.draw.circle(screen, white, (columnas[k], level[i]), radius)
    # Update the display
    pygame.display.flip()
