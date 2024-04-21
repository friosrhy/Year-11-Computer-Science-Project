import pygame, sys, os
from settings import *
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gary the Dog's Adventures!")

class Platformer:
	def __init__(self, screen, width, height):
		self.screen = screen
		self.clock = pygame.time.Clock()
		self.player_event = False

		self.bg_img = pygame.image.load('assets/terrain/bg.jpg')
		self.bg_img = pygame.transform.scale(self.bg_img, (width, height))

	def main(self):
		world = World(world_map, self.screen)
		running = False
		while not running:
			self.screen.blit(self.bg_img, (0, 0))

			for event in pygame.event.get():
				keys = pygame.key.get_pressed()
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
					self.player_event = 'left'
						
				elif keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
						self.player_event = 'space'

				elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
					self.player_event = 'right'

				elif event.type == pygame.KEYUP:
					self.player_event = False
				
				elif keys[pygame.K_ESCAPE]:
					running = True

			world.update(self.player_event)
			pygame.display.update()
			self.clock.tick(60)


if __name__ == "__main__":
	play = Platformer(screen, WIDTH, HEIGHT)
	play.main()