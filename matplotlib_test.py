import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((800, 600))

# Set up the font
font = pygame.font.Font("Font/PressStart2P-Regular.ttf", 30)

# Create a text surface
text_surface = font.render("Hello, world!", True, (255, 255, 255))

# Get the size of the text surface
text_width, text_height = text_surface.get_size()

# Calculate the position to center the text
x = (800 - text_width) // 2
y = (600 - text_height) // 2

# Draw the text on the screen
screen.blit(text_surface, (x, y))

# Update the screen
pygame.display.update()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
