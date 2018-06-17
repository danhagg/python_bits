import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create screen object
    # Initialize pygame, settings and screen object
    pygame.init()  # init background settings pygame needs to work properly
    ai_settings = Settings() # create an instance of Setiings
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height)) # window dim
    pygame.display.set_caption("Wrath of Haggerty")

    # Make instance of a ship
    ship = Ship(screen)

    # Start main loop of game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)



run_game()
