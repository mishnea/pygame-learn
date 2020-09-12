import pygame
from pygame import Color, key, draw # Import tools we might use often into this module's namespace
from pygame.locals import * # Import a bunch of locals into this module's namespace

# ---------------------------------------------------------------------------------------------------------------------
#
# Define any classes and functions here
#
# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    FPS = 60 # Set game FPS
    size = (700, 400) # Set a screen size

    pygame.init() # Initialize pygame. This must be called before you can use most features
    screen = pygame.display.set_mode(size) # Initialize the display and get the screen surface
    clock = pygame.time.Clock() # Get a Clock instance for controlling the game's framerate
    myfont = pygame.font.SysFont("consolas", 15) # Initialize a font for showing text. In this case, size 15 consolas

    while True:
        for event in pygame.event.get():
            # Loop over the event queue. Eevents are piled up inbetween calls to event.get(), when the queue is cleared
            if event.type == QUIT: # Pretty self explanatory
                break

            # You can add some other checks for events you might find useful, like mouse clicks or key presses
        else:
            # Go here if the for loop completed without reaching a 'break' statement

            screen.fill(Color("black")) # Clear the screen by filling with some background colour

            # ---------------------------------------------------------------------------------------------------------
            #
            # Update and draw sprites here
            #
            # ---------------------------------------------------------------------------------------------------------

            # Generate a surface with text, showing the (computed) fps
            writing = myfont.render(
                f"FPS: {clock.get_fps()}", # text to render
                True, # Antialisaing on
                Color("red"), # Text colour
            ) 
            screen.blit(writing, (20, 20)) # Draws the text suface to the screen at position (20, 20)

            pygame.display.flip() # Update the screen
            clock.tick(FPS) # Cap framerate
            continue # Go back to the beginning of the encapsulating while loop
        break # Break out of the while loop only if the for loop was broken out of

    pygame.quit()