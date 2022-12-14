import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		super().__init__()
		"""初始化飞船并设置其初始位置"""
		self.screen=screen
		self.ai_settings=ai_settings

		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect() # 获取屏幕的矩形

		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

		self.center=float(self.rect.centerx)

		self.moving_right=False
		self.moving_left=False

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update(self):
		# 更新飞船的center值，而不是 rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and  self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		# 根据 center 更新 rect 对象
		self.rect.centerx=self.center


	def center_ship(self):
		self.center=self.screen_rect.centerx

	
