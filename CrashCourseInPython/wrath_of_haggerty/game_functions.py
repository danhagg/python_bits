"""Isolate event management loop check_events() from rest of main code"""
import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN: # checks for a key press
            if event.key == pygame.K_RIGHT: # if right arrow
                ship.moving_right = True

        elif event.type == pygame.KEYUP: # checks for a key press
            if event.key == pygame.K_RIGHT: # if right arrow
                ship.moving_right = False

def update_screen(ai_settings, screen, ship):
    """Update images on screen and flip to new screen"""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme() # ship added to screen after background so ship on top

    # Make the most recently drawn screen visible.
    pygame.display.flip()
