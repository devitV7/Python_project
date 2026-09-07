import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fireworks Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (255, 20, 147), (0, 255, 255)]

# Particle class to represent each firework particle
class Particle:
    def __init__(self, x, y, color, angle, speed):
        self.x = x
        self.y = y
        self.color = color
        self.angle = angle
        self.speed = speed
        self.life = 100  # How long the particle lasts

    def move(self):
        # Update particle position
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
        self.life -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)

# Function to create a firework
def create_firework(x, y):
    particles = []
    color = random.choice(COLORS)
    num_particles = random.randint(50, 100)
    for _ in range(num_particles):
        angle = random.uniform(0, 360)
        speed = random.uniform(1, 5)
        particles.append(Particle(x, y, color, angle, speed))
    return particles

# Main loop to simulate fireworks
def main():
    clock = pygame.time.Clock()
    running = True
    fireworks = []

    while running:
        screen.fill(BLACK)
        
        # Create new firework at random position when a new one should appear
        if random.random() < 0.05:
            x = random.randint(100, width - 100)
            y = random.randint(100, height - 100)
            fireworks.append(create_firework(x, y))

        # Update and draw all fireworks
        for firework in fireworks[:]:
            for particle in firework[:]:
                particle.move()
                particle.draw(screen)
                if particle.life <= 0:
                    firework.remove(particle)
            if not firework:
                fireworks.remove(firework)

        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
