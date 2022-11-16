import pygame
from pygame.sprite import Sprite

# 继承类 Sprite
class Bullet(Sprite):
	
	def __init__(self,ai_settings,screen,ship):
		super().__init__()
		self.screen=screen

		# (0,0)处创建一个表示子弹的矩形，再设置正确的位置
		self.rect=pygame.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)# 子弹不是基于图像的，所以必须从空白用pygame.Rect创建一个矩形
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top

		self.y=float(self.rect.y)
		self.color=ai_settings.bullet_color
		self.speed_factor=ai_settings.bullet_speed_factor

	def update(self):
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
