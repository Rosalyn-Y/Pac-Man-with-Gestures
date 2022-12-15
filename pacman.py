'''
Function:
	Pac-Man Game
'''
import os
import random
import sys
import pygame
import Levels

from calendar import c
from pygame import font
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
import Levels

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

ICONPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
FONTPATH = os.path.join(os.getcwd(), 'resources/font/ALGER.TTF')
HEROPATH = os.path.join(os.getcwd(), 'resources/images/pacman.png')
BlinkyPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')


def startLevelGame(level, screen, font):
    clock = pygame.time.Clock()
    SCORE = 0
    wall_setup = level.setupWalls(BLUE)

    hero_setup, ghost_setup = level.setupPlayers(HEROPATH, BlinkyPATH)
    food_setup = level.setupFood(YELLOW)

    success = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(-1)
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for hero in hero_setup:
                        hero.changeSpeed([-1, 0])

                elif event.key == pygame.K_RIGHT:
                    for hero in hero_setup:
                        hero.changeSpeed([1, 0])

                elif event.key == pygame.K_UP:
                    for hero in hero_setup:
                        hero.changeSpeed([0, -1])

                elif event.key == pygame.K_DOWN:
                    for hero in hero_setup:
                        hero.changeSpeed([0, 1])

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        scene = InterFace()
                        scene.start_interface()

        screen.fill(BLACK)

        for hero in hero_setup:
            hero.update(wall_setup)

        hero_setup.draw(screen)

        for hero in hero_setup:
            food_eaten = pygame.sprite.spritecollide(hero, food_setup, True)
        SCORE += len(food_eaten)
        wall_setup.draw(screen)
        food_setup.draw(screen)

        for ghost in ghost_setup:
            if ghost.temp[1] < ghost.tracks[ghost.temp[0]][2]:
                ghost.changeSpeed(ghost.tracks[ghost.temp[0]][0: 2])
                ghost.temp[1] += 1
            else:
                if ghost.temp[0] < len(ghost.tracks) - 1:
                    ghost.temp[0] += 1
                else:
                    ghost.temp[0] = 0
                ghost.changeSpeed(ghost.tracks[ghost.temp[0]][0: 2])
                ghost.temp[1] = 0

            # direction = [0.5, 0]
            # ghost.changeSpeed(direction)
            # res = ghost.defco(wall_setup, direction)
            # while res:
            #     ghost.changeSpeed([-direction[0], direction[1]])
            #     res = ghost.defco(wall_setup, direction)

            # direction = random.choice(
            #     [[-0.5, 0], [0.5, 0], [0, 0.5], [0, -0.5]])
            # ghost.changeSpeed(direction)
            ghost.update(wall_setup)

        ghost_setup.draw(screen)
        score_text = font.render("Score: %s" % SCORE, True, RED)
        screen.blit(score_text, [10, 10])

        if len(food_setup) == 0:
            success = True
            break

        # collide detection
        if pygame.sprite.groupcollide(hero_setup, ghost_setup, False, False):
            success = False
            break

        pygame.display.flip()
        clock.tick(10)

    return success


def showText(screen, smallfont, bigfont, success, flag=False):
    clock = pygame.time.Clock()
    if not success:
        msg = 'Game Over'
        positions = [[180, 200], [90, 280], [150, 320]]
    else:
        msg = 'You Won!'
        positions = [[190, 200], [90, 280], [150, 320]]

    surface = pygame.Surface((400, 200))
    surface.set_alpha(10)
    surface.fill((128, 128, 128))
    screen.blit(surface, (100, 200))

    texts = [bigfont.render(msg, True, WHITE),
             smallfont.render(
                 'Press ENTER to back to the menu', True, WHITE),
             smallfont.render('Press ESCAPE to quit', True, WHITE)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    scene = InterFace()
                    scene.start_interface()

                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                    pygame.quit()

        for idx, (text, position) in enumerate(zip(texts, positions)):
            screen.blit(text, position)
        pygame.display.flip()
        clock.tick(10)


def initialize():
    pygame.init()
    icon_image = pygame.image.load(ICONPATH)
    pygame.display.set_icon(icon_image)
    screen = pygame.display.set_mode([536, 536])
    pygame.display.set_caption('Pac-Man')
    return screen


def main(screen):
    pygame.font.init()
    smallfont = pygame.font.Font(FONTPATH, 22)
    bigfont = pygame.font.Font(FONTPATH, 32)
    level = Levels.Level1()
    success = startLevelGame(level, screen, smallfont)
    showText(screen, smallfont, bigfont, success, True)


def main2(screen):
    pygame.font.init()
    smallfont = pygame.font.Font(FONTPATH, 22)
    bigfont = pygame.font.Font(FONTPATH, 32)
    level = Levels.Level2()
    success = startLevelGame(level, screen, smallfont)
    showText(screen, smallfont, bigfont, success, True)


def main3(screen):
    pygame.font.init()
    smallfont = pygame.font.Font(FONTPATH, 22)
    bigfont = pygame.font.Font(FONTPATH, 32)
    level = Levels.Level3()
    success = startLevelGame(level, screen, smallfont)
    showText(screen, smallfont, bigfont, success, True)


# interface part
class Color:
    ACHIEVEMENT = (220, 160, 87)
    VERSION = (220, 160, 87)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    SKYBLUE = (0, 191, 255)
    TRANSPARENT = (255, 255, 255, 0)


ICONPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')


class Text:
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        self.text = text
        self.text_color = text_color
        self.font_type = font_type
        self.font_size = font_size

        font = pygame.font.Font(os.path.join(
            'font', (self.font_type)), self.font_size)
        self.text_image = font.render(
            self.text, True, self.text_color).convert_alpha()

        self.text_width = self.text_image.get_width()
        self.text_height = self.text_image.get_height()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        upperleft_x = center_x - self.text_width / 2
        upperleft_y = center_y - self.text_height / 2
        surface.blit(self.text_image, (upperleft_x, upperleft_y))


class Image:
    def __init__(self, img_name: str, ratio=1):
        self.img_name = img_name
        # ratio: The image scaling ratio to fit the main screen, default value is 0.4
        self.ratio = ratio

        self.image_1080x1920 = pygame.image.load(
            os.path.join('image', self.img_name)).convert_alpha()
        self.img_width = int(self.image_1080x1920.get_width())
        self.img_height = int(self.image_1080x1920.get_height())

        self.size_scaled = int(self.img_width * self.ratio), int(self.img_height * self.ratio)

        self.image_scaled = pygame.transform.smoothscale(
            self.image_1080x1920, self.size_scaled)
        self.img_width_scaled = self.image_scaled.get_width()
        self.img_height_scaled = self.image_scaled.get_height()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        # center_x, center_y: <center coordinates> of the image placed on the surface
        upperleft_x = center_x - self.img_width_scaled / 2
        upperleft_y = center_y - self.img_height_scaled / 2
        surface.blit(self.image_scaled, (upperleft_x, upperleft_y))


class ColorSurface:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

        self.color_image = pygame.Surface(
            (self.width, self.height)).convert_alpha()
        self.color_image.fill(self.color)

    def draw(self, surface: pygame.Surface, center_x, center_y):
        upperleft_x = center_x - self.width / 2
        upperleft_y = center_y - self.height / 2
        surface.blit(self.color_image, (upperleft_x, upperleft_y))


class ButtonText(Text):
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        super().__init__(text, text_color, font_type, font_size)
        self.rect = self.text_image.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y

    def handle_event(self, command):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command()


class ButtonImage(Image):
    def __init__(self, img_name: str, ratio=0.4):
        super().__init__(img_name, ratio)
        self.rect = self.image_scaled.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y

    def handle_event(self, command):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command()


class ButtonColorSurface(ColorSurface):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.rect = self.color_image.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y

    def handle_event(self, command, *args):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command(*args)


class InterFace():
    def __init__(self):
        pygame.init()

    def basic_background(self):
        # Set logo and interface title
        icon_image = pygame.image.load(ICONPATH)
        game_caption = 'Pac-Man'
        pygame.display.set_icon(icon_image)
        pygame.display.set_caption(game_caption)

        # Set main interface
        show_ratio = 1
        size = width, height = 536, 536
        screen = pygame.display.set_mode(size)

        # set background
        Image('background.jpg').draw(screen, width / 2, height / 2)

        return size, screen

    def start_interface(self):
        # set start_interface
        size, screen = self.basic_background()
        width, height = size

        # Image('ink.png', ratio=0.4).draw(
        #     screen, width * 0.52, height * 0.67)
        Image('achievement_icon.png', ratio=0.25).draw(
            screen, width * 0.93, height * 0.05)
        Text('Pac-Game', Color.WHITE, 'HYHanHeiW.ttf', 50).draw(
            screen, width / 2, height * 1 / 3)
        Text('1.0', Color.VERSION, 'msyh.ttc', 12).draw(
            screen, width / 2, height * 0.97)
        Text('Score', Color.ACHIEVEMENT, 'msyh.ttc', 16).draw(
            screen, width * 0.93, height * 0.09)

        button_game_start = ButtonText(
            'Easy Level', Color.WHITE, 'HYHanHeiW.ttf', 23)
        button_game_start.draw(screen, width / 2, height * 8.1 / 11)

        button_game_start2 = ButtonText(
            'Hard Level', Color.WHITE, 'HYHanHeiW.ttf', 23)
        button_game_start2.draw(screen, width / 2, height * 13/16)

        button_game_start3 = ButtonText(
            'Learning', Color.WHITE, 'HYHanHeiW.ttf', 23)
        button_game_start3.draw(screen, width / 2, height * 2 / 3)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_game_start.handle_event(
                        self.initial_attribute_interface)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_game_start2.handle_event(
                        self.initial_attribute_interface2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_game_start3.handle_event(
                        self.initial_attribute_interface3)

            pygame.display.update()

    def initial_attribute_interface(self):
        screen2 = pygame.display.set_mode([536, 536])
        size, screen = self.basic_background()
        width, height = size

        main(screen2)

    def initial_attribute_interface2(self):
        screen2 = pygame.display.set_mode([536, 536])
        size, screen = self.basic_background()
        width, height = size

        main2(screen2)

    def initial_attribute_interface3(self):
        screen2 = pygame.display.set_mode([536, 536])
        size, screen = self.basic_background()
        width, height = size

        main3(screen2)
