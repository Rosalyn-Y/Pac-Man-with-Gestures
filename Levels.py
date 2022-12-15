'''
difine level
'''
import pygame
from Define import *

level_num = 0


class Level1():
    level_num = 1

    def __init__(self):
        self.info = 'level1'

    def setupWalls(self, wall_color):
        self.wall_setup = pygame.sprite.Group()
        wall_positions = [[0, 0, 6, 536], [0, 0, 536, 6], [0, 530, 536, 6], [530, 0, 6, 536],
                          [0, 106, 214, 6], [322, 106, 214, 6], [
                              0, 424, 214, 6], [322, 424, 214, 6],
                          [214, 212, 107, 6], [115, 318, 99, 6], [322, 318, 99, 6], [115, 212, 6, 106], [415, 212, 6, 106]]

        for wall_position in wall_positions:
            wall = Wall(*wall_position, wall_color)
            self.wall_setup.add(wall)
        return self.wall_setup

    def setupPlayers(self, hero_image_path, ghost_images_path):
        self.hero_sprites = pygame.sprite.Group()
        self.ghost_sprites = pygame.sprite.Group()
        self.hero_sprites.add(Player(255, 465, hero_image_path))

        player = Player(35, 56, ghost_images_path)

        player.tracks = [[0.5, 0, 23], [0, 0.5, 11], [0.5, 0, 20], [0, 0.5, 15], [-0.5, 0, 20], [0, 0.5, 12],
                         [0.5, 0, 15],  [-0.5, 0, 35], [0.5, 0,
                                                        20], [0, -0.5, 20], [-0.5, 0, 10],
                         [0, -0.5, 10], [-0.5, 0, 10], [0, 0.5, 20], [0.5,
                                                                      0, 20], [0, -0.5, 10], [0.5, 0, 10], [0, -0.5, 10],
                         [-0.5, 0, 10], [0, -0.5, 7], [-0.5, 0, 23]]
        self.ghost_sprites.add(player)

        return self.hero_sprites, self.ghost_sprites

    def setupFood(self, food_color):
        self.food_setup = pygame.sprite.Group()
        for row in range(5):
            for col in range(10):
                if (row == 4) and (col == 4 or col == 5):
                    continue
                if (row == 3):
                    food = Food(50*col+35, 100*row+70, 15,
                                15, food_color)
                if (row == 4):
                    food = Food(50*col+35, 100*row+70, 15,
                                15, food_color)
                else:
                    food = Food(50*col+35, 100*row+56, 15,
                                15, food_color)
                is_collide = pygame.sprite.spritecollide(
                    food, self.wall_setup, False)
                if is_collide:
                    continue
                is_collide = pygame.sprite.spritecollide(
                    food, self.hero_sprites, False)
                if is_collide:
                    continue
                self.food_setup.add(food)
        return self.food_setup


class Level2():
    level_num = 2

    def __init__(self):
        self.info = 'level2'

    def setupWalls(self, wall_color):
        self.wall_setup = pygame.sprite.Group()
        wall_positions = [[0, 0, 6, 536], [0, 0, 536, 6], [
            0, 530, 536, 6], [530, 0, 6, 536], [0, 66, 110, 6], [215, 66, 104, 6], [422, 66, 104, 6], [110, 132, 104, 6], [318, 132, 104, 6],
            [0, 198, 110, 6], [215, 198, 104, 6], [422, 198, 104, 6], [110, 198, 6, 66], [
                422, 198, 6, 66], [0, 258, 58, 6], [478, 258, 58, 6], [215, 258, 104, 6],
            [58, 330, 157, 6], [318, 330, 157, 6], [
                58, 336, 6, 66], [469, 336, 6, 66],
            [110, 396, 104, 6], [318, 396, 104, 6],
            [0, 462, 110, 6], [215, 462, 104, 6], [422, 462, 104, 6], [267, 336, 6, 66]]
        for wall_position in wall_positions:
            wall = Wall(*wall_position, wall_color)
            self.wall_setup.add(wall)
        return self.wall_setup

    def setupPlayers(self, hero_image_path, ghost_images_path):
        self.hero_sprites = pygame.sprite.Group()
        self.ghost_sprites = pygame.sprite.Group()
        self.hero_sprites.add(Player(255, 480, hero_image_path))

        player = Player(10, 25, ghost_images_path)

        player.tracks = [[0.5, 0, 13], [0, 0.5, 6], [0.5, 0, 10], [0, 0.5, 6], [-0.5, 0, 10], [0, 0.5, 10],
                         [0.5, 0, 13],  [0, 0.5, 13], [0.5, 0,
                                                       10], [0, 0.5, 6], [-0.5, 0, 32],
                         [0.5, 0, 10], [0, -0.5, 7], [-0.5, 0, 15], [0,
                                                                     -0.5, 13], [0.5, 0, 30], [0, -0.5, 10], [0.5, 0, 10],
                         [0, -0.5, 8], [-0.5, 0, 10], [0, -0.5, 6], [-0.5, 0, 25]]
        self.ghost_sprites.add(player)

        return self.hero_sprites, self.ghost_sprites

    def setupFood(self, food_color):
        self.food_setup = pygame.sprite.Group()
        for row in range(8):
            for col in range(10):
                if (row == 4) and (col == 4 or col == 5):
                    continue
                food = Food(50*col+35, 67*row+22, 15,
                            15, food_color)
                is_collide = pygame.sprite.spritecollide(
                    food, self.wall_setup, False)
                if is_collide:
                    continue
                is_collide = pygame.sprite.spritecollide(
                    food, self.hero_sprites, False)
                if is_collide:
                    continue
                self.food_setup.add(food)
        return self.food_setup


class Level3():
    level_num = 3  # test level

    def __init__(self):
        self.info = 'level2'

    def setupWalls(self, wall_color):
        self.wall_setup = pygame.sprite.Group()
        wall_positions = [[0, 0, 6, 536], [0, 0, 536, 6],
                          [0, 530, 536, 6], [530, 0, 6, 536], [
                              134, 134, 268, 6], [134, 134, 6, 268],
                          [396, 134, 6, 268], [
                              134, 396, 268, 6]]
        for wall_position in wall_positions:
            wall = Wall(*wall_position, wall_color)
            self.wall_setup.add(wall)
        return self.wall_setup

    def setupPlayers(self, hero_image_path, ghost_images_path):
        self.hero_sprites = pygame.sprite.Group()
        self.ghost_sprites = pygame.sprite.Group()
        self.hero_sprites.add(Player(255, 465, hero_image_path))

        player = Player(-200, -200, ghost_images_path)

        player.tracks = [[0, 0, 23]]
        self.ghost_sprites.add(player)

        return self.hero_sprites, self.ghost_sprites

    def setupFood(self, food_color):
        self.food_setup = pygame.sprite.Group()
        for row in range(5):
            for col in range(10):
                if (row == 4) and (col == 4 or col == 5):
                    continue
                if (row == 1 or row == 2 or row == 3) and (col == 2 or col == 3 or col == 4 or col == 5 or col == 6):
                    continue
                if (row == 3):
                    food = Food(50*col+35, 100*row+70, 15,
                                15, food_color)
                if (row == 4):
                    food = Food(50*col+35, 100*row+70, 15,
                                15, food_color)
                else:
                    food = Food(50*col+35, 100*row+56, 15,
                                15, food_color)
                is_collide = pygame.sprite.spritecollide(
                    food, self.wall_setup, False)
                if is_collide:
                    continue
                is_collide = pygame.sprite.spritecollide(
                    food, self.hero_sprites, False)
                if is_collide:
                    continue
                self.food_setup.add(food)
        return self.food_setup
