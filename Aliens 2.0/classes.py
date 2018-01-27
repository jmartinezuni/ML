import pygame
from random import randint, choice
import math
import sys

PLAYERSHOT = 25
GAMEOVER = 26
ENEMYSHOT = 27

class BaseClass(pygame.sprite.Sprite):
	allSprites = pygame.sprite.Group()
	def __init__(self, x, y, image_str):
		pygame.sprite.Sprite.__init__(self)
		BaseClass.allSprites.add(self)
		self.image = pygame.image.load(image_str)
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		self.width = self.rect.width
		self.height = self.rect.height


class Player(BaseClass):
	
	def __init__(self, x, y, image_str):
		BaseClass.__init__(self, x, y, image_str)
		self.velx = 3
		self.vely = 3
		self.shooting = False
		self.special_shot = False
		self.wait = 0
		self.animation_rate = 200
		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False
		self.score = 0

	def draw_score(self, screen):
		font = pygame.font.SysFont("arcade classic", 30)
		score = font.render("SCORE  "+ str(self.score), True, (255, 255, 255))
		screen.blit(score, (300, 10))

	def update(self, list_image_animation, action, SCREENWIDTH, time):
		if self.move_right:
			self.rect.x += self.velx 
		if self.move_left:
			self.rect.x -= self.velx 
		if self.move_up:
			self.rect.y -= self.vely 
		if self.move_down:
			self.rect.y += self.vely 
		if action:
			if self.animation_rate > 0:
				self.image = pygame.image.load(list_image_animation[0])
				self.animation_rate -= 1 * time
			if self.animation_rate < 0:
				self.image = pygame.image.load(list_image_animation[1])
				self.animation_rate = 190
		if self.rect.x < 0:
			self.rect.x = 0
		if self.rect.x > SCREENWIDTH - self.width:
			self.rect.x = SCREENWIDTH - self.width

		if self.shooting and not self.wait and not self.special_shot:
			shot = pygame.event.Event(PLAYERSHOT, {"pos": self.rect.midtop})
			pygame.event.post(shot)
			self.wait = 250
		if self.shooting and not self.wait and self.special_shot:
			shot = pygame.event.Event(PLAYERSHOT, {"pos": self.rect.midtop})
			pygame.event.post(shot)
			self.wait = 80
		if self.wait:
			self.wait += -1 * time
			self.wait = 0 if self.wait <0 else self.wait

class Enemy(BaseClass):
	list_enemy = pygame.sprite.Group()
	def __init__(self, x, y, image_str, player):
		BaseClass.__init__(self, x, y, image_str)
		Enemy.list_enemy.add(self)
		self.x = x
		self.velx = 0
		self.vely = 1
		self.player = player
		self.amplitude = randint(20,80)
		self.period = randint(2,8)/50.
		self.wait = 0
		self.limit = False

	def update(self, SCREENHEIGHT, time):
		self.rect.x += self.velx
		self.rect.y += self.vely
		self.rect.x = self.amplitude * math.cos(self.period * self.rect.y) + self.x
		if self.rect.midtop[1] > SCREENHEIGHT:
			self.kill()
		if self.rect.midbottom[1] > 400: 
			self.limit = True
		if not self.wait and not self.limit:
			shot = pygame.event.Event(ENEMYSHOT,{"pos": self.rect.midbottom})
			pygame.event.post(shot)
			if self.player.sprite.score == 500:
				self.wait = 1593/2
			elif self.player.sprite.score > 1000:
				self.wait = 1593/4
			elif self.player.sprite.score > 2000:
				self.wait = 1593/8
			else :
				self.wait = 1593
		self.wait = 0 if self.wait < 0 else self.wait - time 

		if pygame.sprite.collide_mask(self, self.player.sprite):
			gameover = pygame.event.Event(GAMEOVER)
			pygame.event.post(gameover)

	#@staticmethod
	#def movement(SCREENHEIGHT, list_enemies):
		#for enemy in list_enemies:
			#enemy.motion(SCREENHEIGHT)


class Fire(BaseClass):

	def __init__(self, x, y, image_str, enemies, player, bullets_enemy, vector, friendly, ratio):
		BaseClass.__init__(self, x, y, image_str)
		self.velx = 0
		self.vely = 0
		self.direction = vector
		self.midbottom = (x, y)
		self.enemies = enemies
		self.player = player
		self.bullets_enemy = bullets_enemy
		self.friendly = friendly
		self.ratio = ratio

	def update(self, time, SCREENHEIGHT):
		self.rect.y += self.direction[1] * time / self.ratio
		if self.friendly:
			if pygame.sprite.spritecollide(self, self.enemies, True):
				self.player.sprite.score += 100
				self.kill()
			elif pygame.sprite.spritecollide(self, self.bullets_enemy, True):
				self.kill()
		else:
			if pygame.sprite.collide_mask(self, self.player.sprite):
				gameover = pygame.event.Event(GAMEOVER)
				pygame.event.post(gameover)

		if self.rect.midbottom[1] < 0  or self.rect.midtop[1] > SCREENHEIGHT:
			self.kill()

	#@staticmethod
	#def movement(list_fire):
		#for fire in list_fire:
			#fire.rect.y += fire.vely * FirePlayer.velfire

class FriendPlayer(BaseClass):

	def __init__(self, x, y, image_str, enemies, list_animation):
		BaseClass.__init__(self, x, y, image_str)
		self.health = 100
		self.enemies = enemies
		self.attack = False
		self.danger = 0
		self.count = 0
		self.y = y
		self.list = list_animation
		self.amplitude = randint(10, 40)

	def motion(self, time):
		self.count += time
		self.rect.y = self.amplitude * math.cos(2/50. * self.count/16) + self.y

	def draw_health(self, screen):
		image = pygame.image.load(self.list[self.health/10])
		screen.blit(image, (10, 10))

	def pos_screen_shake(self):
		self.intensity = randint(10, 30)
		self.offsets = [0, 0]
		if self.attack:
			for axis in (0, 1):
				self.offsets[axis] += choice([1*self.intensity, -1*self.intensity])
				return list(self.offsets) 
		else:
				return list(self.offsets)

	def update(self, time):
		for enemy in self.enemies:
			if pygame.sprite.collide_mask(self, enemy):
				self.health -= 10
				self.attack = True
				self.danger = 200
				enemy.kill()
			if self.attack and self.danger:
				self.image = pygame.image.load("images/friend2.png")
				self.danger -= time
			if self.danger < 0:
				self.danger = 0
				self.image = pygame.image.load("images/friend.png")
				self.attack = False
		if self.health == 0:
			gameover = pygame.event.Event(GAMEOVER)
			pygame.event.post(gameover)
		self.motion(time)








