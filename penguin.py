import pygame,random,breaking

pygame.init()

class Penguin(pygame.sprite.Sprite):
    def __init__(self,arrangement_xpos,arrangement_ypos):
        super().__init__()
        self.image_penguin1 = pygame.image.load("new_penguin_hazır0.png").convert_alpha()
        self.image_penguin_hand_wave0 = pygame.image.load("new_penguin_elsalla0.png").convert_alpha()
        self.image_penguin_hand_wave1 = pygame.image.load("new_penguin_elsalla1.png").convert_alpha()
        self.image_penguin_hand_wave2 = pygame.image.load("new_penguin_elsalla2.png").convert_alpha()
        self.image_penguin_hand_wave3 = pygame.image.load("new_penguin_elsalla3.png").convert_alpha()
        self.image_penguin_hand_wave4 = pygame.image.load("new_penguin_elsalla4.png").convert_alpha()
        self.image_penguin_waiting_normal0 = pygame.image.load("new_penguin_hazır0.png").convert_alpha()
        self.image_penguin_waiting_normal1 = pygame.image.load("new_penguin_hazır1.png").convert_alpha()
        self.image_penguin_waiting_normal2 = pygame.image.load("new_penguin_hazır2.png").convert_alpha()
        self.image_penguin_waiting_normal3 = pygame.image.load("new_penguin_hazır3.png").convert_alpha()
        self.image_penguin_waiting_normal4 = pygame.image.load("new_penguin_hazır4.png").convert_alpha()
        self.image_penguin_waiting_normal5 = pygame.image.load("new_penguin_hazır5.png").convert_alpha()
        self.image_penguin_waiting_normal6 = pygame.image.load("new_penguin_hazır6.png").convert_alpha()
        self.image_penguin_turning_round0 = pygame.image.load("penguin_dönme0.png").convert_alpha()
        self.image_penguin_turning_round1 = pygame.image.load("penguin_dönme1.png").convert_alpha()
        self.image_penguin_turning_round2 = pygame.image.load("penguin_dönme2.png").convert_alpha()
        self.image_penguin_turning_round3 = pygame.image.load("penguin_dönme3.png").convert_alpha()
        self.image_penguin_back = pygame.image.load("penguin_arka.png").convert_alpha()
        self.image_penguin_on_sea = pygame.image.load("penguin_on_sea0.png").convert_alpha()
        self.image_penguin_blood = pygame.image.load("penguin_blood.png").convert_alpha()

        self.image = self.image_penguin1
        self.rect = self.image.get_rect()

        self.arrangement_xpos=arrangement_xpos                          #ekranda alacağı konumun x değeri (değeri core scriptinden alıyor)
        self.arrangement_ypos=arrangement_ypos                          #ekranda alacağı konumun y değeri (değeri core scriptinden alıyor)

        self.position=24

        self.new_xpos=0                                                 #zıplamadan sonra gideceği yeni x_konumu
        self.new_ypos=0                                                 #zıplamadan sonra gideceği yeni y_konumu

        self.taraf="üst"                                                #penguenin nihai konumuna ekrandan geleceği ilk yerin tarafını belirliyor
        self.definingArea(self.taraf)                                   #buzların nihai konumuna ekrandan geleceği ilk yeri belirliyor
        self.status="waiting"
        self.waiting_mode="normal"

        self.rect.midbottom = (self.arrangement_xpos, self.arrangement_ypos)        #pengueni buz üstünde konumlandırırken oluşturulan nesnenin alt orta noktasının koordinatlarının kullanılmasını sağlar (init içinde ön tanımlamasının yapıldığı bu yer önemli)

        self.waiting_normal_counter = 0                                 #penguenin normal modda beklediği sırada yapacaklarını belirleyen sayaç
        self.hand_wave_counter = 0                                      #penguenin el sallama modunda yapacaklarını belirleyen sayaç
        self.turning_round_counter=0                                    #penguenin normal modda beklerken zıpladığında yapacaklarını belirleyen sayaç
        self.rounding_counter=0                                         #penguenin normal modda beklerken ne kadar zamanda zıplayacağını belirleyen sayaç
        self.turn_round_control = True

        self.replacement_area=0                                         #zıplama ile yeni gideceği yerin tablo numarası

        self.game_over_by_seal = False
        self.game_over_by_seal_counter = 0

    def update(self):
        if self.status=="beginning":
            self.asagi()
            if self.arrangement_ypos==330:
                self.status = "waiting_for_start"
        elif self.status=="playing":
            if self.waiting_mode=="normal":
                self.waitingNormal()
                self.hand_wave_counter =0
                self.waiting_normal_counter += 1
                if self.rounding_counter==5:
                    self.turnRound()
            elif self.waiting_mode=="waiting_to_move":
                self.handWaving()
                self.rounding_counter = 0
                self.turning_round_counter=0
                self.hand_wave_counter += 1
            elif self.waiting_mode=="replace":
                self.turnRound()
                if self.turn_round_control == False:
                    self.choosingReplacementArea()
        elif self.status == "game_over":
            self.gameOver()
        elif self.status=="game_over_by_treasure":
            self.gameOverByTreasure()
        elif self.status=="game_over_by_seal":
            self.gameOverBySeal()
        self.definingPosition()


    def definingPosition(self):
        for i in range(0,len(breaking.destination)):
            if self.arrangement_xpos==breaking.destination[i][0] and self.arrangement_ypos==breaking.destination[i][1]:
                self.position=i
                break
        return self.position

    def asagi(self):
        self.arrangement_ypos+=1
        self.rect.midbottom = (self.arrangement_xpos, self.arrangement_ypos)
        return self.rect.midbottom

    def definingArea(self,taraf):
        if taraf=="üst":
            self.rect.midbottom= self.arrangement_xpos,self.arrangement_ypos
        return self.rect.midbottom

    def handWaving(self):
        self.rect.midbottom = (self.arrangement_xpos, self.arrangement_ypos)
        if 0<=self.hand_wave_counter <100 :
            self.image = self.image_penguin_hand_wave0
        elif 100<=self.hand_wave_counter<105 or 130<=self.hand_wave_counter<135 or 160<=self.hand_wave_counter<165 :
            self.image = self.image_penguin_hand_wave1
        elif 105<=self.hand_wave_counter<110 or 125<=self.hand_wave_counter<130 or 135<=self.hand_wave_counter<140 or 155<=self.hand_wave_counter<160:
            self.image = self.image_penguin_hand_wave2
        elif 110<=self.hand_wave_counter<115 or 120<=self.hand_wave_counter<125 or 140<=self.hand_wave_counter<145 or 150<=self.hand_wave_counter<155:
            self.image = self.image_penguin_hand_wave3
        elif 115<=self.hand_wave_counter<120 or 145<=self.hand_wave_counter<150:
            self.image = self.image_penguin_hand_wave4
        if self.hand_wave_counter>165:
            self.hand_wave_counter =0
        return self.image

    def waitingNormal(self):
        self.rect.midbottom = (self.arrangement_xpos, self.arrangement_ypos)
        if 0<=self.waiting_normal_counter <100 :
            self.image = self.image_penguin_waiting_normal0
        elif 100<=self.waiting_normal_counter<102:
            self.image = self.image_penguin_waiting_normal1
        elif 102<=self.waiting_normal_counter<104 or 118<=self.waiting_normal_counter<120 or 134<=self.waiting_normal_counter<136:
            self.image = self.image_penguin_waiting_normal2
        elif 104<=self.waiting_normal_counter<106 or 116<=self.waiting_normal_counter<118 or 120<=self.waiting_normal_counter<122 or 132<=self.waiting_normal_counter<134:
            self.image = self.image_penguin_waiting_normal3
        elif 106<=self.waiting_normal_counter<108 or 114<=self.waiting_normal_counter<116 or 122<=self.waiting_normal_counter<124 or 130<=self.waiting_normal_counter<132:
            self.image = self.image_penguin_waiting_normal4
        elif 108<=self.waiting_normal_counter<110 or 112<=self.waiting_normal_counter<114 or 124<=self.waiting_normal_counter<126 or 128<=self.waiting_normal_counter<130:
            self.image = self.image_penguin_waiting_normal5
        elif 110<=self.waiting_normal_counter<112 or 126<=self.waiting_normal_counter<128:
            self.image = self.image_penguin_waiting_normal6
        if self.waiting_normal_counter>=136:
            self.waiting_normal_counter =0
            self.rounding_counter += 1
        return self.image

    def turnRound(self):
        self.turn_round_control = True
        self.rect.midbottom = (self.arrangement_xpos+5, self.arrangement_ypos-30)                                       #değişmiş olan zıplayan png imaj'ın tam olarak konumda zıplaması için gerekli düzeltmeler.
        self.turning_round_counter += 1
        if 0<=self.turning_round_counter <30 or 65<=self.turning_round_counter<90:
            self.image = self.image_penguin_turning_round0
        elif 30<=self.turning_round_counter<35 or 60<=self.turning_round_counter<65:
            self.image = self.image_penguin_turning_round1
        elif 35<=self.turning_round_counter<40 or 55<=self.turning_round_counter<60:
            self.image = self.image_penguin_turning_round2
        elif 40<=self.turning_round_counter<45 or 50<=self.turning_round_counter<55:
            self.image = self.image_penguin_turning_round3
        elif 45<=self.turning_round_counter<50:
            self.image = self.image_penguin_back
        if self.turning_round_counter >= 90:
            self.turning_round_counter = 0
            self.rounding_counter=0
            self.waiting_normal_counter = 0
            self.turn_round_control=False
        return self.image

    def actualIceAreas(self,actual_ice_list):
        self.replacement_area = random.choice(actual_ice_list)
        return self.replacement_area

    def choosingReplacementArea(self):
        self.new_xpos, self.new_ypos = breaking.destination[self.replacement_area][0],breaking.destination[self.replacement_area][1]
        while (self.new_xpos==self.rect.centerx and self.new_xpos==self.rect.centery):
            self.new_xpos, self.new_ypos = breaking.destination[self.replacement_area][0],breaking.destination[self.replacement_area][1]
        self.arrangement_xpos, self.arrangement_ypos=self.new_xpos,self.new_ypos
        self.waiting_mode = "normal"

    def gameOver(self):
        self.image=self.image_penguin_on_sea
        self.rect.center = (self.arrangement_xpos, self.arrangement_ypos)

    def gameOverByTreasure(self):
        self.image = self.image_penguin_hand_wave1

    def gameOverBySeal(self):
        if self.game_over_by_seal==False:
            self.game_over_by_seal=True
            self.game_over_by_seal_counter=0
        if self.game_over_by_seal == True:
            self.game_over_by_seal_counter += 1
        if self.game_over_by_seal==True and self.game_over_by_seal_counter>=100:
            self.image = self.image_penguin_blood
            self.arrangement_xpos, self.arrangement_ypos=300,200
            self.rect.midbottom = (self.arrangement_xpos, self.arrangement_ypos)