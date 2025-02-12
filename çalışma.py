import random
"""for i in self.ice_group_list:
    for j in range(0, len(queue)):
        if i.sprite.rect.center == (queue[j][0], queue[j][1]):
            i.sprite.status = "waiting_for_playing"
for i in self.waves_group_list:
    for j in self.ice_group_list:
        if j.sprite.status == "waiting_for_playing":
            i.sprite.status = "start_to_wave"

# if self.ice_group_list[i].sprite.rect.center==(queue[i][0],queue[i][1]):                                  #sudaki dalgalanmayı başlatır.


for nesne in self.ice_group_list:
    if nesne.sprite.status=="waiting_for_playing":
        #x_pos,y_pos=nesne.sprite.rect.center
        for dalga in self.waves_group_list:
            if dalga.sprite.arrangement_xpos==nesne.sprite.rect.centerx and dalga.sprite.arrangement_ypos==nesne.sprite.rect.centery:
                dalga.sprite.status="start_to_wave"

toplam=0
for i in self.ice_group_list:
    if i.sprite.status=="waiting_for_playing":
        toplam+=1
print(toplam)

if self.ice_group_list[i].sprite.rect.center != (queue[i][0], queue[i][1]):
    print(self.ice_group_list[i].sprite.rect.center, self.ice_group_list[i].sprite.ice_on_sea_interval_number)
    print("statu", self.ice_group_list[i].sprite.status, self.ice_group_list[i].sprite.arrangement_xpos,
          self.ice_group_list[i].sprite.arrangement_ypos)
if self.waves_group_list[i].sprite.status != "start_to_wave":
    pass
    # print("yess",self.waves_group_list[i].sprite.rect.center,self.waves_group_list[i].sprite.ice_on_sea_interval_number)

self.x_variation=self.new_xpos-self.arrangement_xpos
self.y_variation = self.new_xpos - self.arrangement_ypos
self.arrangement_xpos, self.arrangement_ypos=self.new_xpos,self.new_ypos
self.waiting_mode = "normal"
print(self.x_variation,self.y_variation)


def sealMovementsSea(self):
    delay = 1.5 * (self.penguin_posx - self.seal_up_to_the_water_point)
    if delay < self.counter <= delay + 100:
        self.seal_x_pos, self.seal_y_pos = -100, -100
        self.rect.midbottom = (self.seal_x_pos, self.seal_y_pos)
    elif self.counter >= delay + 100:
        self.definningSealLocation(50, 400, 385, 395)  # self.definningSealLocation(50,400,self.posy-60,self.posy+60)
        self.counter = 0
    self.iceLocations()

else:
    print("ilk",self.rect.midbottom)
    self.up_to_the_ice_counter+=1
    if self.up_to_the_ice_counter>=30:
        self.sealStep()
        self.catching_pos_y=self.y_pos+15                                                                        #midbottom'a göre göründüğü yer ile olduğu yer arasındaki farkı gidermek için
        if self.posx-60<=self.x_pos<=self.posx+60 and self.posy-15<=self.catching_pos_y<=self.posy+15:
            self.catch_the_penguin=True
            self.status="game_over_by_seal


def toTheWater(self):
    self.rect.midbottom = (self.x_pos, self.y_pos)
    print(self.posx, self.posy)
    if self.y_pos >= 330:
        self.seal_step_counter += 1
        if self.face == "right" and self.seal_step_counter == 5:
            self.image = self.image_on_the_ice_right0
            self.y_pos += 2
        elif self.face == "right" and self.seal_step_counter == 10:
            self.image = self.image_on_the_ice_right1
            self.y_pos += 2
            self.seal_step_counter = 0
    else:
        self.seal_step_counter += 1
        if self.face == "right" and self.seal_step_counter == 5:
            self.image = self.image_on_the_ice_right0
            self.y_pos -= 2
        elif self.face == "right" and self.seal_step_counter == 10:
            self.image = self.image_on_the_ice_right1
            self.y_pos -= 2
            self.seal_step_counter = 0



    def iceLocations(self):                                                                                             #fok buzlara geldiğinde durur.
        if self.face=="right":
            for konum in self.ice_on_sea_number:
                if konum[0] <= self.seal_x_pos <= konum[1] and konum[2] <= self.seal_y_pos <= konum[3]:
                    self.direction="up_to_the_ice"
                    self.seal_step_counter=0
                    break
        else:
            print("yess")
            for konum in self.ice_on_sea_number:
                if konum[0]+10 <= self.seal_x_pos <= konum[1]+10 and konum[2] <= self.seal_y_pos <= konum[3]:
                    self.direction="up_to_the_ice"
                    self.seal_step_counter=0
                    break
        return self.direction"""

"""if (self.penguin_posx - 60 <= self.seal_x_pos <= self.penguin_posx + 60 and
                    self.penguin_posy - 15 <= self.seal_y_pos <= self.penguin_posy + 15):
                print("fok",self.penguin_posx,self.penguin_posy,self.seal_x_pos,self.seal_y_pos)
                self.catch_the_penguin = True
                self.status = "game_over_by_seal"""

"""posy=270
def correctionWithSeal1Location(posy,seal1_posy):
    while True:
        if posy == seal1_posy:
            posy = random.choice([270, 290])
        else:
            break
    return posy
posy=correctionWithSeal1Location(posy,270)
print(posy)"""

"""liste="ldcndcn"
liste_yeni=[]
for i in liste:
    liste_yeni.append(i)
liste_yeni.pop()
print(liste_yeni)
liste_yeni_str=""
for i in range(0,len(liste_yeni)):
    liste_yeni_str+=liste_yeni[i]
liste=liste_yeni_str
print(liste)
#liste.remove(9)
#print(liste.replace(liste[-1],""))
#print(len(liste))"""

"""def generateFakeResults(result):
    while True:
        if 0<=result<10:
            fake_result=random.randint(0,9)
        elif 10<=result<20:
            fake_result=random.randint(10,19)
        elif 20<=result<30:
            fake_result=random.randint(20,29)
        elif 30<=result<40:
            fake_result=random.randint(30,39)
        elif 40<=result<50:
            fake_result=random.randint(40,49)
        elif 50<=result<60:
            fake_result=random.randint(50,59)
        elif 60<=result<70:
            fake_result=random.randint(60,69)
        elif 70<=result<80:
            fake_result=random.randint(70,79)
        elif 80<=result<90:
            fake_result=random.randint(80,89)
        if fake_result!=result:
            break
    return fake_result

print(generateFakeResults(38))"""

def generateResultLocation():
    location_list = [480, 620, 760]
    location_list_new=[]
    for i in range(3):
        location_list_new.append(random.choice(location_list))
        location_list.remove(location_list_new[i])
    location_list=list(location_list_new)
    return location_list