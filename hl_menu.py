import os
import pygame
import pygame_menu
from pygame_menu.themes import Theme

font = pygame_menu.font.FONT_BEBAS

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode((900, 600))


def set_difficulty(selected, value):
    print('Set difficulty to {} ({})'.format(selected[0], value))


def start_the_game():
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    print('Do the job here !')


font = pygame_menu.font.FONT_OPEN_SANS_BOLD
design = Theme(background_color=(228, 100, 36),
               selection_color=(255, 255, 255),
               title_background_color=(170, 65, 50),
               widget_font_color=(0, 0, 0),
               widget_font_size=30,
               widget_font=font,
               title_font=font)

menu = pygame_menu.Menu(
    height=600,
    theme=design,
    title='Vítej v naučné aplikaci',
    width=900
)

menu.add_button('Start', start_the_game)
menu.add_selector('Obtížnost: ', [('Jednoduché', 1), ('Střední', 2), ('Těžké', 3)], onchange=set_difficulty)
menu.add_button('Opustit aplikaci', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)