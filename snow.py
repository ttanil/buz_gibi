import pygame,random

pygame.init()

class Snow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_snow1 = pygame.image.load("kar_taneleri1.png").convert_alpha()
        self.image_snow2 = pygame.image.load("kar_taneleri2.png").convert_alpha()
        self.image_snow3 = pygame.image.load("kar_taneleri3.png").convert_alpha()
        self.image_snow4 = pygame.image.load("kar_taneleri4.png").convert_alpha()
        self.image_snow5 = pygame.image.load("kar_taneleri5.png").convert_alpha()
        self.image_snow6 = pygame.image.load("kar_taneleri6.png").convert_alpha()
        self.image_snow7 = pygame.image.load("kar_taneleri7.png").convert_alpha()
        self.image_snow8 = pygame.image.load("kar_taneleri8.png").convert_alpha()

        self.shape="belirsiz"
        self.definingSnow()                                                                                             # kar tanesinin şekli belirlenir
        self.definingArea()                                                                                             # ekranda alacağı konumun x ve y değerleri belirlenir

        self.status = "start_to_snow"
        self.counter =0

    def update(self):
        if self.status=="start_to_snow":
            if self.shape=="big":
                if self.counter%9==0:
                    self.rect.centery+=1                                                                                #ekranda karlar yağmaya başlayacak
            else:
                if self.counter % 4 == 0:
                    self.rect.centery += 1
            if self.rect.centery>=720:
                self.kill()
            self.counter+=1

    def definingSnow(self):
        snow_list=["big","big","big","big","small","small","small","small","small","small","small"]
        self.shape=random.choice(snow_list)
        if self.shape=="big":
            self.image=random.choice([self.image_snow1,self.image_snow3,self.image_snow5,self.image_snow7])
        else:
            self.image = random.choice([self.image_snow2, self.image_snow4, self.image_snow6, self.image_snow8])
        return self.image

    def definingArea(self):
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,1280)
        self.rect.y = -20
        return self.rect