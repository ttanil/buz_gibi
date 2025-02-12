import pygame,random,breaking

pygame.init()

class Waves(pygame.sprite.Sprite):
    def __init__(self,queue_number):
        super().__init__()
        self.image_wave0 = pygame.image.load("waveV4-2.png").convert_alpha()
        self.image_wave1 = pygame.image.load("waveV4-2-1.png").convert_alpha()
        self.image_wave2 = pygame.image.load("waveV4-2-2.png").convert_alpha()
        self.image_wave3 = pygame.image.load("waveV4-2-3.png").convert_alpha()
        self.image_wave4 = pygame.image.load("waveV4-2-4.png").convert_alpha()
        self.image_wave5 = pygame.image.load("waveV4-2-5.png").convert_alpha()

        self.image = self.image_wave5
        self.rect = self.image.get_rect()

        self.queue_number = queue_number
        self.arrangement_xpos_ypos = breaking.destination[self.queue_number]

        self.arrangement_xpos=self.arrangement_xpos_ypos[0]                             # ekranda alacağı konumun x değeri (değeri core scriptinden alıyor)
        self.arrangement_ypos=self.arrangement_xpos_ypos[1]                             # ekranda alacağı konumun y değeri (değeri core scriptinden alıyor)

        self.status = "waiting"
        self.counter=0

    def update(self):
        if self.status=="waiting" and self.rect.centerx==self.arrangement_xpos and self.rect.centery==self.arrangement_ypos:
            self.status="start_to_wave"
        elif self.status=="start_to_wave":
            self.counter += 1
            self.definingArea(),self.waving()                                           # ekranda buzların konumunda dalgalanmaya başlayacak
            if self.counter > 640:
                self.counter = 0
        elif self.status=="disappear":
            self.dispers()

    def definingArea(self):
        self.rect.x = self.arrangement_xpos-20
        self.rect.y = self.arrangement_ypos+10
        return self.rect

    def waving(self):
        if 0<=self.counter<100:
            self.image = self.image_wave5
        elif 100<=self.counter<200:
            self.image = self.image_wave4
        elif 200<=self.counter<290:
            self.image = self.image_wave3
        elif 290<=self.counter<370:
            self.image = self.image_wave2
        elif 370<=self.counter<440:
            self.image = self.image_wave1
        elif 440<=self.counter<500:
            self.image = self.image_wave2
        elif 500<=self.counter<550:
            self.image = self.image_wave3
        elif 550 <= self.counter < 640:
            self.image = self.image_wave4
        return self.image

    def dispers(self):
        self.rect.centery = 900