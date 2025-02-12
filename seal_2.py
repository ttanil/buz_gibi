import pygame,random,breaking

pygame.init()

class Seal_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_seal_in_the_sea1 = pygame.image.load("seal_in_the_sea1.png").convert_alpha()
        self.image_seal_in_the_sea2 = pygame.image.load("seal_in_the_sea2.png").convert_alpha()
        self.image_seal_in_the_sea_empty = pygame.image.load("seal_in_the_sea_empty.png").convert_alpha()
        self.image_on_the_ice_left0 = pygame.image.load("seal_movement_left0.png").convert_alpha()
        self.image_on_the_ice_left1 = pygame.image.load("seal_movement_left1.png").convert_alpha()
        self.image_on_the_ice_right0 = pygame.image.load("seal_movement_right0.png").convert_alpha()
        self.image_on_the_ice_right1 = pygame.image.load("seal_movement_right1.png").convert_alpha()
        self.image_seal_right_diving0 = pygame.image.load("seal_right_diving0.png").convert_alpha()
        self.image_seal_right_diving1 = pygame.image.load("seal_right_diving1.png").convert_alpha()
        self.image_seal_right_diving2 = pygame.image.load("seal_right_diving2.png").convert_alpha()
        self.image_seal_right_diving3 = pygame.image.load("seal_right_diving3.png").convert_alpha()
        self.image_seal_right_diving4 = pygame.image.load("seal_right_diving4.png").convert_alpha()
        self.image_seal_left_diving0 = pygame.image.load("seal_left_diving0.png").convert_alpha()
        self.image_seal_left_diving1 = pygame.image.load("seal_left_diving1.png").convert_alpha()
        self.image_seal_left_diving2 = pygame.image.load("seal_left_diving2.png").convert_alpha()
        self.image_seal_left_diving3 = pygame.image.load("seal_left_diving3.png").convert_alpha()
        self.image_seal_left_diving4 = pygame.image.load("seal_left_diving4.png").convert_alpha()

        self.image = self.image_seal_in_the_sea1
        self.rect = self.image.get_rect()
        self.seal2_x_pos=950                                                                                            #fokun x konumu
        self.seal2_y_pos=240                                                                                            #fokun y konumu
        self.rect.midbottom=(self.seal2_x_pos,self.seal2_y_pos)
        self.penguin_last_posy_list=[]
        self.seal1_posy = 330

        self.actual_ice_list=list(range(0,len(breaking.destination)))
        self.ice_on_sea_number=self.ice_on_sea(self.actual_ice_list)

        self.status = "beginning"                                                                                       #akan oyuna göre fokun durumu
        self.face="none"
        self.direction="none"                                                                                           #fokun oyun içindeki pozisyonuna göre sonraki hareketinin ne olacağına kumanda eden değişken
        self.seal_up_to_the_water_point=0
        self.definningSealLocation(850,950,240)
        self.counter=0                                                                                                  #oyun sayacı

        self.seal_diving_counter = 0                                                                                    #dalış işinde yapılacakların ayarlandığı sayaç
        self.seal_diving_control = False                                                                                #dalış işinin başlamasını kontrol eden boolean değişken

        self.chilling = False

        self.seal_sea_movements_control = False                                                                         #fokun su içindeki yüze hareketinin başlamasını kontrol eden boolean değişken

        self.seal_step_counter = 0                                                                                      #fok buzlara geldiğinde üstüne çıkma işini kontrol eden sayaç
        self.back_to_the_water_counter = 0                                                                              #
        self.seal_aim_number =0
        self.back_to_the_water_number =0
        self.seal_sea_movements_counter = 0

        self.penguin_posx=610                                                                                           #penguenin x konumu
        self.penguin_posy=330                                                                                           #penguenin y konumu

        self.correcting_pos_on_the_ice=0
        self.catching_pos_y=0

        self.catch_the_penguin=False


    def update(self):
        if self.status == "beginning":
            if self.counter%3==0:
                self.beginning()
        elif self.status == "waiting_for_playing":
            self.waitingForPlaying()
        elif self.status == "waiting_for_playing":
            self.waitingForPlaying()
        elif self.status =="start_to_playing":
            self.sealDiving("dive")
        elif self.status=="playing" and self.counter%3==0 and (self.status !="game_over_by_treasure" or self.status !="game_over"):
            if self.direction!="up_to_the_ice" and self.direction!="down_from_ice":
                self.sealSeaMovements()
            elif self.direction=="up_to_the_ice":
                self.sealStepsOnIce()
            elif self.direction=="down_from_ice":
                self.sealDiving("dive")
        elif self.status == "game_over_by_seal":
            self.captureThePenguin()
        self.counter+=1


    def beginning(self):
        self.rect.midbottom = (self.seal2_x_pos-10,self.seal2_y_pos+50)
        self.seal2_x_pos -= 1

    def waitingForPlaying(self):
        if self.counter >= 750:
            self.sealDiving("dive")
            if self.seal_diving_control == False:
                self.counter = 0
                self.chilling = False
        if self.counter == 0 and self.chilling == False and self.seal_diving_control == False:
            self.chilling = True
            self.definningSealLocation(random.randint(850, 1000), 1100, random.randint(230, 245))
        if self.chilling == True and self.counter < 750 and self.seal_diving_control == False:
            if self.counter % 3 == 0:
                self.rect.midbottom = (self.seal2_x_pos - 10, self.seal2_y_pos + 50)
                self.seal2_x_pos -= 1

    def sealDiving(self,command):
        self.positionCorrectionWithFace()
        if self.seal_diving_control==False and command=="dive":
            self.seal_diving_control=True
        if self.seal_diving_control==True and self.seal_diving_counter <= 70:
            if self.face=="right":
                self.image=self.image_seal_in_the_sea1
            else:
                self.image = self.image_seal_in_the_sea2
        elif self.seal_diving_control==True and 70<self.seal_diving_counter<=80:
            if self.face == "right":
                self.image=self.image_seal_right_diving0
            else:
                self.image = self.image_seal_left_diving0
        elif self.seal_diving_control==True and 80<self.seal_diving_counter<=98:
            if self.face == "right":
                self.image=self.image_seal_right_diving1
            else:
                self.image = self.image_seal_left_diving1
        elif self.seal_diving_control==True and 98<self.seal_diving_counter<=105:
            if self.face == "right":
                self.image=self.image_seal_right_diving2
            else:
                self.image = self.image_seal_left_diving2
        elif self.seal_diving_control==True and 105<self.seal_diving_counter<=110:
            if self.face == "right":
                self.image=self.image_seal_right_diving3
            else:
                self.image = self.image_seal_left_diving3
        elif self.seal_diving_control==True and 110<self.seal_diving_counter<=130:
            if self.face == "right":
                self.image = self.image_seal_right_diving4
            else:
                self.image = self.image_seal_left_diving4
        elif self.seal_diving_control==True and 130<self.seal_diving_counter<=150:
            self.image=self.image_seal_in_the_sea_empty
        elif self.seal_diving_control == True and 150<self.seal_diving_counter:
            self.image=self.image_seal_in_the_sea_empty
            self.seal_diving_control=False
            self.seal_sea_movements_control = False
            self.direction = "none"
            self.seal_diving_counter = 0
        self.seal_diving_counter += 1

    def defineStatusPlaying(self,status):                                                                               #core scriptinden "playing" durumunu alır.
        self.status =status

    def ice_on_sea(self,list):                                                                                          # buz parçalarının tüm kütlelerinin kapladığı koordinat aralığını verir
        self.ice_on_sea_number = []
        for i in list:
            self.ice_on_sea_number.extend(
                [[breaking.destination[i][0] - 30, breaking.destination[i][0] + 30, breaking.destination[i][1] - 10, breaking.destination[i][1] + 10]])
        return self.ice_on_sea_number

    def actualIceList(self,list):
        self.actual_ice_list=list
        self.ice_on_sea(self.actual_ice_list)
        return self.actual_ice_list

    def penguinLocation(self,posy):
        self.penguin_posy=posy

    def seal1Location(self,pos):
        self.seal1_posy = pos[1]

    def correctionWithSeal1Location(self,posy):
        while True:
            if posy==self.seal1_posy:
                posy=random.choice([270,290,310,330,350,370,390])
            else:
                break
        return posy

    def positionCorrectionWithFace(self):
        if self.face == "right":
            self.rect.midbottom = (self.seal2_x_pos - 10, self.seal2_y_pos + 50)
        else:
            self.rect.midbottom = (self.seal2_x_pos +10, self.seal2_y_pos + 45)

    def definningSealLocation(self,posx1,posx2,posy):
        self.seal2_x_pos,self.seal2_y_pos =random.randint(posx1,posx2),posy                                             #fok için ekranda yer beliler
        random_control=True
        while random_control:
            toplam=0
            for konum in self.ice_on_sea_number:
                if konum[0] <= self.seal2_x_pos <= konum[1] and konum[2] <= self.seal2_y_pos <= konum[3]:
                    self.seal2_x_pos,self.seal2_y_pos =random.randint(posx1,posx2),posy
                    break
                else:
                    toplam+=1
            if toplam==len(self.ice_on_sea_number):
                random_control=False
        self.correctionWithSeal1Location(posy)
        self.seal_up_to_the_water_point=self.seal2_x_pos
        if self.seal2_x_pos<640:                                                                                        #ekrandaki yerine göre fokun yüzünün döneceği tarafı belirler
            self.face = "right"
            self.image = self.image_seal_in_the_sea1
        else:
            self.face = "left"
            self.image = self.image_seal_in_the_sea2
        self.positionCorrectionWithFace()

    def iceLocations(self):                                                                                             #fok buzlara geldiğinde durur.
        for konum in self.ice_on_sea_number:
            if konum[0] <= self.seal2_x_pos <= konum[1] and konum[2] <= self.seal2_y_pos <= konum[3]:
                self.direction="up_to_the_ice"
                self.seal_step_counter=0
                break
        return self.direction

    def backToTheWater(self):                                                                                           #bu fonksiyon fok'un yüzmesinin bitiminde
        for konum in self.ice_on_sea_number:                                                                            #önünde buz olup olmadığını kontrol eder yoksa
            if konum[0] <= self.seal2_x_pos <= konum[1] and konum[2] <= self.seal2_y_pos <= konum[3]:                   #dalış yaptır.(ardından tekrar yüzer)
                self.direction="back_to_the_water"
                self.seal_diving_counter=0
                break
        return self.direction

    def sealSeaMovements(self):
        self.penguin_last_posy_list.clear()
        for i in range(11):
            self.penguin_last_posy_list.append(self.penguin_posy)
        if self.seal_sea_movements_control==False:
            total_list=breaking.makePosyList()+self.penguin_last_posy_list
            self.definningSealLocation(100, 1000, random.choice(total_list))               #self.definningSealLocation(100, 300, 330)                  # self.definningSealLocation(50,400,self.posy-60,self.posy+60)
            self.seal_aim_number=random.randint(1, 5)
            self.back_to_the_water_number=random.randint(50, 100)
            self.seal_sea_movements_control = True
        self.positionCorrectionWithFace()                                                                               #konumlara yapılan eklemeler ekranda göründüğü yeri düzeltmek için
        if self.seal_aim_number != 5 and self.seal_sea_movements_control == True:
            self.seal_sea_movements_counter += 1
            if self.face == "right" and self.direction != "up_to_the_ice":
                self.seal2_x_pos += 1
            elif self.face == "left" and self.direction != "up_to_the_ice":
                self.seal2_x_pos -= 1
            self.iceLocations()                                                                                         # bu fonksiyondan seal'ın direction değeri döner.
            if self.seal_sea_movements_counter >= 700:
                self.sealDiving("dive")
                if self.seal_diving_control == False:
                    self.seal_sea_movements_control = False
                    self.direction = "none"
                self.seal_sea_movements_counter = 0
            if self.face == "right" and self.direction!="up_to_the_ice":
                self.seal2_x_pos += 1
            elif self.face == "left" and self.direction!="up_to_the_ice":
                self.seal2_x_pos -= 1
            self.iceLocations()                                                                                         #bu fonksiyondan seal'ın direction değeri döner.
        elif self.seal_aim_number == 5 and self.seal_sea_movements_control == True:
            if self.direction!="back_to_the_water":
                self.back_to_the_water_counter+=1
                self.backToTheWater()
            if self.seal_sea_movements_control ==True and self.face == "right" and self.direction!="back_to_the_water":
                self.seal2_x_pos += 1
            elif self.seal_sea_movements_control ==True and self.face == "left" and self.direction!="back_to_the_water":
                self.seal2_x_pos -= 1
            if self.back_to_the_water_counter>=self.back_to_the_water_number and self.direction!="back_to_the_water":
                self.direction = "back_to_the_water"
                self.back_to_the_water_counter=0
                self.seal_diving_counter=0
            if self.direction=="back_to_the_water":
                self.sealDiving("dive")
                if self.seal_diving_control==False:
                    self.seal_sea_movements_control = False
                    self.direction = "none"

    def downFromIce(self):                                                                                              #fok buzların üstünde yürürken
        toplam=0                                                                                                        #bu fonksiyon ile altında buz olup
        for konum in range(0,len(self.ice_on_sea_number)):                                                              #olmadığını kontrol eder, buz olmaması
            if (self.ice_on_sea_number[konum][0] <= self.seal2_x_pos <= self.ice_on_sea_number[konum][1] and             #durumunda dalış durumuna geçirir
                    self.ice_on_sea_number[konum][2] <= self.seal2_y_pos <= self.ice_on_sea_number[konum][3]):           #(tekrar yüzmeye dönmesini sağlar)
                break
            else:
                toplam+=1
        if toplam==len(self.ice_on_sea_number):
            self.direction="down_from_ice"
            self.seal_diving_counter=0
            if self.face=="right":
                self.seal2_x_pos+=40
            else:
                self.seal2_x_pos -= 40
        return self.direction

    def sealStepsOnIce(self):
        self.rect.midbottom = (self.seal2_x_pos - 10, self.seal2_y_pos+3)
        self.seal_step_counter+=1
        if self.seal_step_counter<=40:
            self.positionCorrectionWithFace()
        elif self.seal_step_counter>40 and self.direction!="down_from_ice":
            if self.face == "right" and self.seal_step_counter==45:
                self.image = self.image_on_the_ice_right0
                self.seal2_x_pos+=3
            elif self.face == "right" and self.seal_step_counter==50:
                self.image = self.image_on_the_ice_right1
                self.seal2_x_pos+=3
                self.seal_step_counter =41
                self.downFromIce()                                                                                      #bastığı yerde buz yoksa suya geri döner
            if self.face == "left" and self.seal_step_counter==45:
                self.image = self.image_on_the_ice_left0
                self.seal2_x_pos-=3
            elif self.face == "left" and self.seal_step_counter==50:
                self.image = self.image_on_the_ice_left1
                self.seal2_x_pos-=3
                self.seal_step_counter =41
                self.downFromIce()                                                                                      #bastığı yerde buz yoksa suya geri döner (yazılımda daha az kontrol edilmesi için her 3 adıma bağlandı)

    def captureThePenguin(self):
        pass