import pygame,random,breaking

pygame.init()

class Ice(pygame.sprite.Sprite):
    def __init__(self,queue_number):
        super().__init__()
        self.image_ice1 = pygame.image.load("ice0.png").convert_alpha()
        self.image_ice2 = pygame.image.load("ice01.png").convert_alpha()
        self.image_damaged_ice1 = pygame.image.load("damaged_ice0.png").convert_alpha()
        self.image_damaged_ice2 = pygame.image.load("damaged_ice1.png").convert_alpha()

        self.ice_shape = "belirsiz"
        self.image = self.definingIce()                                                                                 #buz şekillerinden birini rastgele seçerek belirliyor
        self.rect = self.image.get_rect()

        self.queue_number=queue_number
        self.arrangement_xpos_ypos=breaking.destination[self.queue_number]

        self.arrangement_xpos=self.arrangement_xpos_ypos[0]                                                             #ekranda alacağı konumun x değeri (değeri core scriptinden alıyor)
        self.arrangement_ypos=self.arrangement_xpos_ypos[1]                                                             #ekranda alacağı konumun y değeri (değeri core scriptinden alıyor)
        self.breaking_place=self.placeOnBreakingList(self.queue_number)

        self.taraf=self.definingWay()                                                                                   #buzların nihai konumuna ekrandan geleceği ilk yerin tarafını belirliyor
        self.definingArea(self.taraf)                                                                                   #buzların nihai konumuna ekrandan geleceği ilk yeri belirliyor
        self.status="beginning"

        self.health = 50

    def update(self):
        if self.status=="beginning":
            if self.taraf=="sol" and self.rect.centerx!=self.arrangement_xpos:
                self.rect.centerx+=1
            elif self.taraf=="alt" and self.rect.centery!=self.arrangement_ypos:
                self.rect.centery-=1
            elif self.taraf == "sağ" and self.rect.centerx != self.arrangement_xpos:
                self.rect.centerx -= 1
            if self.rect.centerx==self.arrangement_xpos and self.rect.centery==self.arrangement_ypos:
                self.status = "waiting_for_playing"
        elif self.status=="waiting_for_playing":
            pass
        elif self.status=="disappear":
            pass
        if self.health < 20:
            self.damagedIce()


    def definingIce(self):
        randomModule=random.choice(["düz","yan"])
        if randomModule=="düz":
            self.image = self.image_ice1
            self.ice_shape = "düz"
        else:
            self.image = self.image_ice2
            self.ice_shape = "yan"
        return self.image

    def definingWay(self):
        if (0<=self.queue_number<=3 or 7<=self.queue_number<=9 or 14<=self.queue_number<=16 or 21<=self.queue_number<=23
                or self.queue_number==28 or self.queue_number==35 or self.queue_number==42):
            taraf = "sol"
        elif (4<=self.queue_number<=6 or 10<=self.queue_number<=13 or 17<=self.queue_number<=20 or 25<=self.queue_number<=27
              or self.queue_number==34 or self.queue_number==41 or self.queue_number==48):
            taraf = "sağ"
        else:
            taraf = "alt"
        return taraf

    def definingArea(self,taraf):
        if taraf=="sol":
            self.rect.centerx = self.arrangement_xpos-(self.arrangement_xpos+random.randint(180,500))
            self.rect.centery = self.arrangement_ypos
        elif taraf=="alt":
            self.rect.centerx = self.arrangement_xpos
            self.rect.centery = self.arrangement_ypos+(random.randint(710,1000)-self.arrangement_ypos)
        else:
            self.rect.centerx = self.arrangement_xpos+(random.randint(1270,1610)-self.arrangement_xpos)
            self.rect.centery = self.arrangement_ypos
        return self.rect

    def damagedIce(self):
        if self.ice_shape == "düz":
            self.image = self.image_damaged_ice1
        else:
            self.image = self.image_damaged_ice2
        return self.image

    def placeOnBreakingList(self,ice_on_sea_interval_number):
        for i in range(0, len(breaking.single24)):
            if ice_on_sea_interval_number==breaking.single24[i]:
                breaking_place=i
                break
        return breaking_place

    def dispers(self,breaking_place):
        if 0<=breaking_place<=3:
            if 0<=self.breaking_place<=3:
                self.rect.centery=900
        elif 4<=breaking_place<=7:
            if 4<=self.breaking_place<=7:
                self.rect.centery=900
        elif 8<=breaking_place<=10:
            if 8<=self.breaking_place<=10:
                self.rect.centery=900
        elif 11<=breaking_place<=13:
            if 11<=self.breaking_place<=13:
                self.rect.centery=900
        elif 14<=breaking_place<=16:
            if 14<=self.breaking_place<=16:
                self.rect.centery=900
        elif 17<=breaking_place<=18:
            if 17<=self.breaking_place<=18:
                self.rect.centery=900
        elif 19<=breaking_place<=20:
            if 19<=self.breaking_place<=20:
                self.rect.centery=900
        elif 21<=breaking_place<=22:
            if 21<=self.breaking_place<=22:
                self.rect.centery=900
        elif 23<=breaking_place<=24:
            if 23<=self.breaking_place<=24:
                self.rect.centery=900
        else:
            if breaking_place==self.breaking_place:
                self.rect.centery = 900
        if self.rect.centery >= 900:
            self.status ="disappear"