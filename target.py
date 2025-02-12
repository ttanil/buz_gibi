import pygame,breaking

pygame.init()
pygame.mixer.init()

class Target(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.image_target = pygame.image.load("target1.png").convert_alpha()
        self.image_pickax = pygame.image.load("pickax.png").convert_alpha()
        self.image_pickax1 = pygame.image.load("pickax1.png").convert_alpha()
        self.image_pickax2 = pygame.image.load("pickax2.png").convert_alpha()
        self.image_pickax3 = pygame.image.load("pickax3.png").convert_alpha()
        self.image_pickax4 = pygame.image.load("pickax4.png").convert_alpha()

        self.pickaxe_sound = pygame.mixer.Sound("Pickaxe.wav")

        self.image = self.image_target
        self.rect = self.image.get_rect()

        self.arrangement_xpos=x_pos                                                                      #ekranda alacağı konumun x değeri (değeri core scriptinden alıyor)
        self.arrangement_ypos=y_pos                                                                      #ekranda alacağı konumun y değeri (değeri core scriptinden alıyor)

        self.shape="target_cursor"
        self.status="beginning"

        self.digging_counter = 0
        self.return_to_playing_game=True

    def update(self):
        if self.status=="beginning":
            self.rect.center=-100,-100
        elif self.status=="playing":                                                                    #oyun oynanırken ekranda mouse yerine hedef cursorünün çıkmasını sağlar
            pass
        elif self.status=="disappear":                                                                  #tıklandığında kazma grafiklerini yapar
            self.digging_counter += 1
            self.pickaxMovements()


    def targetCursorMovements(self,x_pos,y_pos):
        if self.status=="playing":
            pygame.mouse.set_visible(False)
            self.image=self.image_target
            self.rect.center=x_pos,y_pos
        elif self.status=="game_over":
            self.rect.center =-100,-100
            pygame.mouse.set_visible(True)

    def pickaxControl(self,x_pos,y_pos,status):
        if self.return_to_playing_game==True and status=="playing":
            pygame.mouse.set_visible(False)
            for konum in breaking.ice_on_sea_list:
                if konum[0]<=x_pos <=konum[1] and konum[2]<=y_pos <=konum[3]:
                    self.status = "disappear"
                    self.image = self.image_pickax
                    self.rect.center = x_pos - 15, y_pos - 100

    def pickaxMovements(self):
        self.return_to_playing_game=False
        if 0 <= self.digging_counter < 30 or 65 <= self.digging_counter < 90:
            self.image = self.image_pickax
            if self.digging_counter>65:
                self.pickaxe_sound.play()
        elif 30 <= self.digging_counter < 35 or 60 <= self.digging_counter < 65:
            self.image =self.image_pickax1
        elif 35 <= self.digging_counter < 40 or 55 <= self.digging_counter < 60:
            self.image =self.image_pickax2
        elif 40 <= self.digging_counter < 45 or 50 <= self.digging_counter < 55:
            self.image =self.image_pickax3
        elif 45 <= self.digging_counter < 50:
            self.image =self.image_pickax4
        if self.digging_counter >= 90:
            self.digging_counter = 0
            self.status = "playing"
            self.return_to_playing_game=True
        return self.image

    def sealPosForPickaxe(self,posx,posy):
        if posx-10<=self.rect.centerx<=posx+10 and posy-10<=self.rect.centery<=posy+10:
            pass
        else:
            self.status = "playing"