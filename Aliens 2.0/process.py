import pygame
from pygame import colordict as clr
from classes import *
from process import *
import random

PLAYERSHOT = 25
GAMEOVER = 26
ENEMYSHOT = 27

def game_loop(screen_base, clock, FPS):

	PLAYER_RATE = 12
	ALIEN_RATE = 36
 	running = True
 	totalframes = 0
 	screen = pygame.Surface((500, 650))

	list_spacecraft = ["images/nave1.png","images/nave2.png"]
	list_invader = ["images/alien1.png","images/alien2.png"]
	list_friend = ["images/health/life0.png", "images/health/life1.png", "images/health/life2.png", "images/health/life3.png",
					"images/health/life4.png", "images/health/life5.png", "images/health/life6.png", "images/health/life7.png",
					"images/health/life8.png", "images/health/life9.png", "images/health/life10.png"]

	spacecraft = Player(screen.get_width()/2, 400, "images/nave1.png")
	bullets = pygame.sprite.Group()
	bullets2 = pygame.sprite.Group()
	enemies = pygame.sprite.Group()
	player = pygame.sprite.GroupSingle(spacecraft)
	friend = pygame.sprite.GroupSingle(FriendPlayer(250, screen.get_height() - 100, "images/friend.png", bullets2, list_friend))
	screen_base.fill(clr.THECOLORS['midnightblue'])

	while running:
		#Logic
		time = clock.tick(FPS)
		running = handle_game_events(player, FPS, totalframes, bullets, bullets2, enemies)
		bullets.update(time, screen.get_height())
		bullets2.update(time, screen.get_height())
		enemies.update(screen.get_height(), time)
		friend.update(time)
		player.update(list_spacecraft, True, screen.get_width(), time)
		##############staticmethods
		#Enemy.movement(screen.get_height(), enemies)
		totalframes += 1
		#Draw
		screen.fill(clr.THECOLORS['midnightblue'])  
		enemies.draw(screen)
		friend.draw(screen)
		bullets.draw(screen)
		bullets2.draw(screen)
		player.draw(screen)
		friend.sprite.draw_health(screen) # se puede crear una clase para obviar esto con class.draw
		player.sprite.draw_score(screen)
		#update
		screen_base.fill(clr.THECOLORS['midnightblue'])
		screen_base.blit(screen, friend.sprite.pos_screen_shake())
		pygame.display.flip()

def handle_game_events(p, FPS, totalframes, b1, b2, e):
	for event in pygame.event.get():
				if (event.type == pygame.QUIT): #or \
					#(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					Enemy.list_enemy.empty()
					return False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_s:
						p.sprite.special_shot = True
					elif event.key == pygame.K_LEFT:
						p.sprite.move_left = True
					elif event.key == pygame.K_RIGHT:
						p.sprite.move_right = True
					elif event.key == pygame.K_UP:
						p.sprite.move_up = True
					elif event.key == pygame.K_DOWN:
						p.sprite.move_down = True
					elif event.key == pygame.K_SPACE:
						p.sprite.shooting = True
					elif event.key == pygame.K_ESCAPE:
						Enemy.list_enemy.empty()
						return False
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT:
						p.sprite.move_left = False
					elif event.key == pygame.K_RIGHT:
						p.sprite.move_right = False
					elif event.key == pygame.K_UP:
						p.sprite.move_up = False
					elif event.key == pygame.K_DOWN:
						p.sprite.move_down = False
					elif event.key == pygame.K_SPACE:
						p.sprite.shooting = False
				elif event.type == PLAYERSHOT:
					b1.add(Fire(event.dict["pos"][0], event.dict["pos"][1]
						,"images/fire.png", e, p, b2, (0,-1), True, 3))
				elif event.type == ENEMYSHOT:
					b2.add(Fire(event.dict["pos"][0], event.dict["pos"][1]
						,"images/alienfire.png", e, p, b1, (0,1), False, 6))
				elif event.type == GAMEOVER:
					Enemy.list_enemy.empty()
					return False

	spawn(FPS, totalframes, e, p )
	return True


def spawn(FPS, totalframes, e, p):
	some_seconds = FPS * 3
	if totalframes % some_seconds == 0:
		x = random.randint(10, 450)
		e.add(Enemy(x, 10, "images/alien1.png", p))

def draw_title(screen):
    screen.fill(clr.THECOLORS['darkseagreen4'])
    spacing = 10
    screen_width = screen.get_width()

    title = pygame.font.SysFont("arcade classic", 40)
    instruction = pygame.font.SysFont("arcade classic", 16)
    combined_height = title.get_height() + instruction.get_height() + spacing

    top = (screen.get_height() - combined_height) / 2
    newline = title.render("Spacecraft", True, (255, 255, 255))
    left = (screen_width - newline.get_width()) / 2
    screen.blit(newline, (left, top))

    top += newline.get_height() + spacing
    newline = instruction.render("Press Enter to Begin", True, (255, 255, 255))
    left = (screen_width - newline.get_width()) / 2
    screen.blit(newline, (left, top))
    pygame.display.flip()