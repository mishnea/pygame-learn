import pygame


size = (700, 400) # Set a screen size

pygame.init() # Initialize pygame. This must be called before you can use most features
screen = pygame.display.set_mode(size) # Initialize the display and get the screen surface
clock = pygame.time.Clock() # Get a Clock instance for controlling the game's framerate
done = False # Controls the while loop

xpos = size[0] // 2 # Set initial x position of a sprite to half screen width
ypos = size[1] // 2 # Set the y position
radius = 10
color = pygame.Color("red") # Pygame has some built in colours which can be useful. We can also pass rgba values like (255, 0, 0, 255) where a is alpha
xvel = 5 # Set initial x velocity of sprite

while not done:
    for event in pygame.event.get():
        # Loop over the event queue. The events are piled up inbetween calls to event.get(), when the queue is cleared
        if event.type == pygame.QUIT: # Pretty self explanatory
            done = True
    
    screen.fill(pygame.Color("black")) # Clear the screen by filling with some background colour

    # Draw a circle at sprite's position to the screen
    pygame.draw.circle(screen, color, (int(xpos), ypos), radius)
    if not(radius < xpos < size[0]-radius):
        # Switch direction if hitting either edge
        xvel = xvel * -1
    xpos += xvel # Move

    pygame.display.flip() # Update the display
    clock.tick(60) # Cap FPS to 60
