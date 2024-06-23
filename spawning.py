import random
import pygame
from predator import Predator
from prey import Prey
from food import Food
import constants
#这里简单的测试一下
def spawn_predator(obstacles, screen_width, screen_height):
    while True:
        x = random.randint(constants.CONTROL_PANEL_WIDTH, screen_width - constants.BLOCK_SIZE)
        y = random.randint(0, screen_height - constants.BLOCK_SIZE)
        agent_rect = pygame.Rect(x, y, constants.BLOCK_SIZE, constants.BLOCK_SIZE)
        if not any(agent_rect.colliderect(obs.rect) for obs in obstacles):
            return Predator(x, y, constants.BLOCK_SIZE)

def spawn_prey(obstacles, screen_width, screen_height):
    while True:
        x = random.randint(constants.CONTROL_PANEL_WIDTH, screen_width - constants.BLOCK_SIZE)
        y = random.randint(0, screen_height - constants.BLOCK_SIZE)
        agent_rect = pygame.Rect(x, y, constants.BLOCK_SIZE, constants.BLOCK_SIZE)
        if not any(agent_rect.colliderect(obs.rect) for obs in obstacles):
            return Prey(x, y, constants.BLOCK_SIZE)

def spawn_food(obstacles, screen_width, screen_height):
    while True:
        x = random.randint(constants.CONTROL_PANEL_WIDTH, screen_width - constants.FOOD_SIZE)
        y = random.randint(0, screen_height - constants.FOOD_SIZE)
        food_rect = pygame.Rect(x, y, constants.FOOD_SIZE, constants.FOOD_SIZE)
        if not any(food_rect.colliderect(obs.rect) for obs in obstacles):
            return Food(x, y, constants.FOOD_SIZE)
