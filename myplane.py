import pygame


class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        # 调用父类的构造方法
        pygame.sprite.Sprite.__init__(self)

        # 加载飞机图片，并去除周围透明部分
        self.image1 = pygame.image.load("images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("images/me2.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/me_destroy_1.png").convert_alpha(),
            pygame.image.load("images/me_destroy_2.png").convert_alpha(),
            pygame.image.load("images/me_destroy_3.png").convert_alpha(),
            pygame.image.load("images/me_destroy_4.png").convert_alpha()
            ])

        # 获取图片矩形区域
        self.rect = self.image1.get_rect()
        # 获取背景的长和高
        self.width, self.height = bg_size[0], bg_size[1]

        # 设置飞机的位置（水平居中，底部靠上）,注意：self.rect为飞机的矩形，self.width/height为背景（边框）的矩形
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height - 60

        # 设置飞机速度
        self.speed = 10
        self.active = True
        # 无敌状态
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        # 如果飞机的上边缘大于0，则说明在屏幕内
        if self.rect.top > 0:
            # -speed则向上移动
            self.rect.top -= self.speed
        # 否则，飞机的上边缘等于0（无法飞出屏幕）
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height - 60
        self.active = True
        # 无敌状态
        self.invincible = True
