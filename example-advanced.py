import pygame
from pygame import Color, key, draw # Import tools we might use often into this module's namespace
from pygame.locals import * # Import a bunch of locals into this module's namespace


class BallSprite:
    """Make a player-controlled ball."""

    radius = 10
    gravity = 0.05
    accel = 0.1

    def __init__(self, pos, keys=None, color="blue"):
        self.x, self.y = pos
        self.vx, self.vy = 0, 0
        self.color = color
        if keys is None:
            self.keys = {
                "left": K_LEFT,
                "right": K_RIGHT,
                "up": K_UP
            }
        else:
            self.keys = keys

    def draw(self, surface):
        draw.circle(surface, Color(self.color), self.get_pos(), self.radius)
    
    def get_pos(self):
        # Gets sprite's position as tuple of integers
        # Many functions in pygame only accept integers
        return (int(self.x), int(self.y))
    
    def collide(self):
        if self.x >= size[0] - self.radius: # Check if hitting right edge
            self.x = size[0] - self.radius
            self.vx *= -0.9 # Switch x direction and lose some velocity off bounce
        if self.x <= self.radius: # Check if hitting left edge
            self.x = self.radius
            self.vx *= -0.9 # Switch x direction and lose some velocity off bounce
        if self.y >= size[1] - self.radius: # Check if hitting bottom edge
            self.y = size[1] - self.radius
            self.vy *= -0.9 # Switch y direction and lose some velocity off bounce
        if self.y <= self.radius: # Check if hitting top edge
            self.y = self.radius
            self.vy *= -0.9 # Switch y direction and lose some velocity off bounce
    
    def update(self):
        # Implement some basic controls
        self.vx += self.accel * (key.get_pressed()[self.keys['right']] - key.get_pressed()[self.keys['left']])
        self.vy += self.gravity - self.accel*key.get_pressed()[self.keys['up']]
        self.x += self.vx
        self.y += self.vy
        self.collide()


if __name__ == "__main__":
    size = (700, 400) # Set a screen size

    pygame.init() # Initialize pygame. This must be called before you can use most features
    screen = pygame.display.set_mode(size) # Initialize the display and get the screen surface
    clock = pygame.time.Clock() # Get a Clock instance for controlling the game's framerate

    sprites = [
        BallSprite((100,100), color="red"), # Red, control with left, right & up
        BallSprite((200,100), {"left": K_a, "right": K_d, "up": K_w}) # Blue, control with A, D & W
    ]

    while True:
        for event in pygame.event.get():
            # Loop over the event queue. The events are piled up inbetween calls to event.get(), when the queue is cleared
            if event.type == QUIT: # Pretty self explanatory
                break
        else:
            # Go here if the for loop completed without reaching a 'break' statement

            screen.fill(Color("black")) # Fill the screen with some background colour

            for sprite in sprites:
                sprite.update()
                sprite.draw(screen)

            pygame.display.flip() # Update the screem
            clock.tick(60)
            continue # Go back to the beginning of the encapsulating while loop
        break # Break out of the while loop only if the for loop was broken out of

    print("Quitting...")
    pygame.quit() # Close pygame window and stuff
