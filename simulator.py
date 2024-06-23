import random
import pygame
from predator import Predator
from prey import Prey
from food import Food
from obstacle import Obstacle
import constants

class Simulator:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.predators = []
        self.prey = []
        self.foods = []
        self.obstacles = []
        self.selected_agent = None

    def initialize(self):
        self.initialize_obstacles()
        self.initialize_agents()
        self.initialize_food()

    def initialize_obstacles(self):
        self.obstacles = []
        num_obstacles = random.randint(5, 10)
        for _ in range(num_obstacles):
            while True:
                width = random.randint(50, 200)
                height = random.randint(50, 200)
                x = random.randint(constants.CONTROL_PANEL_WIDTH, self.screen_width - width)
                y = random.randint(0, self.screen_height - height)
                new_obstacle = Obstacle(x, y, width, height)

                if not any(new_obstacle.rect.colliderect(obs.rect) for obs in self.obstacles):
                    self.obstacles.append(new_obstacle)
                    break

    def initialize_agents(self):
        self.predators = []
        self.prey = []

        for _ in range(constants.NUM_PREDATORS):
            self.generate_predator()

        for _ in range(constants.NUM_PREY):
            self.generate_prey()

    def initialize_food(self):
        self.foods = []

        for _ in range(constants.NUM_FOOD):
            self.generate_food()

    def breedPrey(self):
        if not self.prey:
            return

        preyHealth = [p.health for p in self.prey]
        
        parent1, parent2 = random.choices(self.prey, weights=preyHealth, k=2)
        child = parent1.crossbreed(parent2)
        if random.random() < constants.MUTATION_CHANCE:
            child.mutate()
        
        self.ensure_no_collision(child)
        self.prey.append(child)
    
    def breedPredator(self):
        if not self.predators:
            return

        predHealth = [p.health for p in self.predators]
        
        parent1, parent2 = random.choices(self.predators, weights=predHealth, k=2)
        child = parent1.crossbreed(parent2)
        if random.random() < constants.MUTATION_CHANCE:
            child.mutate()
        
        self.ensure_no_collision(child)
        self.predators.append(child)

    def applyGeneticAlgorithm(self):
        if random.random() < constants.PREY_REPRODUCTION_CHANCE:
            self.breedPrey()
        if random.random() < constants.PREDATOR_REPRODUCTION_CHANCE:
            self.breedPredator()

    def generate_agent(self):
        self.applyGeneticAlgorithm()

    def generate_prey(self):
        while True:
            x = random.randint(constants.CONTROL_PANEL_WIDTH, self.screen_width - constants.BLOCK_SIZE)
            y = random.randint(0, self.screen_height - constants.BLOCK_SIZE)
            new_prey = Prey(x, y, constants.BLOCK_SIZE)
            if not any(new_prey.rect.colliderect(obs.rect) for obs in self.obstacles):
                self.prey.append(new_prey)
                break

    def generate_predator(self):
        while True:
            x = random.randint(constants.CONTROL_PANEL_WIDTH, self.screen_width - constants.BLOCK_SIZE)
            y = random.randint(0, self.screen_height - constants.BLOCK_SIZE)
            new_predator = Predator(x, y, constants.BLOCK_SIZE)
            if not any(new_predator.rect.colliderect(obs.rect) for obs in self.obstacles):
                self.predators.append(new_predator)
                break

    def generate_food(self):
        while True:
            x = random.randint(constants.CONTROL_PANEL_WIDTH, self.screen_width - constants.FOOD_SIZE)
            y = random.randint(0, self.screen_height - constants.FOOD_SIZE)
            new_food = Food(x, y, constants.FOOD_SIZE)
            if not any(new_food.rect.colliderect(obs.rect) for obs in self.obstacles):
                self.foods.append(new_food)
                break

    def ensure_no_collision(self, agent):
        while any(agent.rect.colliderect(obs.rect) for obs in self.obstacles):
            agent.rect.x = random.randint(constants.CONTROL_PANEL_WIDTH, self.screen_width - agent.rect.width)
            agent.rect.y = random.randint(0, self.screen_height - agent.rect.height)

    def add_food(self):
        current_food_count = len(self.foods)
        if current_food_count < constants.NUM_FOOD:
            self.spawn_food(constants.NUM_FOOD - current_food_count)

    def check_events(self):
        pass

    def remove_dead(self):
        self.predators = [p for p in self.predators if p.health > 0]
        self.prey = [p for p in self.prey if p.health > 0]
    def move_models(self):
        for predator in self.predators:
            predator.set_prey_list(self.prey)
            predator.env_predators = self.predators
            predator.env_prey = self.prey
            predator.env_food = self.foods
            predator.env_obstacles = self.obstacles
            self.move_predator(predator)
        for prey in self.prey:
            prey.env_predators = self.predators
            prey.env_prey = self.prey
            prey.env_food = self.foods
            prey.env_obstacles = self.obstacles
            self.move_prey(prey)

    def move_prey(self, prey):
        prey.move(constants.CONTROL_PANEL_WIDTH, self.screen_width, self.screen_height, self.obstacles)

    def move_predator(self, predator):
        predator.move(constants.CONTROL_PANEL_WIDTH, self.screen_width, self.screen_height, self.obstacles)
    def draw_models(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        for predator in self.predators:
            predator.draw(screen)
        for prey_item in self.prey:
            prey_item.draw(screen)
        for food_item in self.foods:
            food_item.draw(screen)

        if self.selected_agent:
            agent_info = (
                f"{self.selected_agent.__class__.__name__}: "
                f"Position ({self.selected_agent.rect.x}, {self.selected_agent.rect.y}), "
                f"Velocity ({self.selected_agent.velocity[0]}, {self.selected_agent.velocity[1]}), "
                f"Health ({self.selected_agent.health})"
            )
            info_surface = pygame.font.Font(None, 24).render(agent_info, True, (255, 255, 255))
            screen.blit(info_surface, (50, self.screen_height - 100))

    def update_health(self):
        for predator in self.predators:
            predator.update_health()
        for prey_item in self.prey:
            prey_item.update_health()

    def prey_hunt(self):
        for prey_item in self.prey:
            prey_item.eat_food(self.foods)

    def predator_hunt(self):
        for predator in self.predators:
            predator.hunt_prey(self.prey)

    def decrease_health(self):
        self.update_health()
        self.remove_dead()

    def get_agent_info(self, pos):
        for agent in self.predators + self.prey:
            if agent.rect.collidepoint(pos):
                return agent
        return None

    def spawn_food(self, count):
        for _ in range(count):
            self.generate_food()
