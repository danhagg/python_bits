import pygame

class Ship():

    def __init__(self, screen): # screen is where we draw ship
        """Initializ the ship and set its starting position"""
        self.screen = screen

        # Load the ship image and get its rect
        # load func returns a surface we store in self.image
        self.image = pygame.image.load('/Users/danielhaggerty/Google Drive/py_games/wrath_of_haggerty/images/ship.bmp')
        self.rect = self.image.get_rect() #get_rect access surfaces pygame-rect attr
        self.screen_rect = screen.get_rect() # store screen's rect

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx # ship center = screen center
        self.rect.bottom = self.screen_rect.bottom # centered at bottom

        # Movement flag
        self.moving_right = False

    def update(self):
        """Update ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self): # draws image to screen at self.rect position
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)
