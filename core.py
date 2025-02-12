import pygame,random,breaking,calculator

from waves import Waves
from ice import Ice
from penguin import Penguin
from snow import Snow
from target import Target
from treasure import Treasure
from frame import Frame
from seal import Seal
from seal_2 import Seal_2

pygame.init()
pygame.mixer.init()

class GameCore:
    def __init__(self):
        self.window_width=1280
        self.window_height=720
        self.window=pygame.display.set_mode((self.window_width,self.window_height))
        pygame.display.set_caption("Ice_Breaker with Multiplication Table")
        self.Background0=pygame.image.load("sea.png").convert_alpha()
        self.Clock = pygame.time.Clock()
        #self.Background0 = pygame.transform.scale(self.Background0, (1280, 720))
        self.gameInitials()

    def gameInitials(self):
        self.dispersion_list = breaking.single24                                                        #hangi buz kütlelerinin hangi buz kütleleriyle bağlantılı olduğunu veren liste
        self.queue = breaking.destination                                                               #buzların başlangıçta gideceği konum listesini yapar

        self.makingFrame()
        self.ice_group_list=self.makingIce(self.dispersion_list)                                        #buzları oluşturur
        self.waves_group_list=self.makingWaves(self.dispersion_list)                                    #dalgaları oluşturur ve gideceği yerleri belirler
        self.penguin_group=self.callingPenguin()                                                        #pengueni oluşturur
        self.definningTreasureLocation()
        self.callingSeal()
        self.callingSeal_2()

        self.actual_ice_list=self.dispersion_list[:]                                                    #oyun içerisindeki güncel buz listesini tutar

        self.SNOW_EVENT = pygame.USEREVENT
        pygame.time.set_timer(self.SNOW_EVENT, 1000)
        self.snow_group=pygame.sprite.Group()

        self.music=self.musicChoose("starting-01.mp3",1)
        self.music_change=True
        self.silence_music_control=True
        self.music_counter=0
        self.hey_sound=pygame.mixer.Sound("hey1.mp3")

        self.mouse_posx, self.mouse_posy=0,0
        self.mouse_time=0
        self.hit_control = False                                                                       #mouse ile yapılan vuruşları kontrol eder
        self.penguin_replace_time=0
        self.penguin_on_ice_time=0

        self.definningTargetCursor(self.mouse_posx, self.mouse_posy)                                   #hedef kürsörünü oluşturan fonksiyon
        self.target_control =False
        self.pickaxe_control = False
        self.replace_control = False
        self.how_to_play_control=False
        self.starting_game_control=True
        self.game_quit_control = False

        self.extra_surface = pygame.Surface((0, 0))
        self.Background1 = pygame.image.load("frame0-1.png")

        self.number=""
        self.number_a_b_list =[]
        self.result_locations_list=[480, 620, 760]
        self.result=0
        self.result_a=0
        self.result_b=0
        self.number_a="0"
        self.number_b = "0"
        self.color=(0, 0, 0)
        self.color_a = (0, 0, 0)
        self.color_b = (0, 0, 0)
        self.number_control=True
        self.choosing_result_with_mouse_control = True
        self.number_counter=0

    def makingFrame(self):
        self.frame_group = pygame.sprite.GroupSingle()
        frame = Frame()
        self.frame_group.add(frame)
        return self.frame_group

    def makingIce(self,queue):
        ice_group_list=[]
        for i in range(0,len(queue)):
            ice_group = pygame.sprite.GroupSingle()
            ice = Ice(queue[i])
            ice_group.add(ice)
            ice_group_list.append(ice_group)
        return ice_group_list

    def makingWaves(self,queue):
        waves_group_list=[]
        for i in range(0,len(queue)):
            waves_group = pygame.sprite.GroupSingle()
            wave = Waves(queue[i])
            waves_group.add(wave)
            waves_group_list.append(waves_group)
        return waves_group_list

    def callingPenguin(self):
        penguin_group = pygame.sprite.GroupSingle()
        penguin=Penguin(610, -50)
        penguin_group.add(penguin)
        return penguin_group

    def snowing(self,number):
        snow_group_list=[]
        for i in range(number):
            snow_group = pygame.sprite.GroupSingle()
            snow=Snow()
            snow_group.add(snow)
            snow_group_list.append(snow_group)
        return snow_group_list

    def definningTreasureLocation(self):
        self.treasure_group=pygame.sprite.GroupSingle()
        treasure=Treasure()
        self.treasure_group.add(treasure)
        return self.treasure_group

    def definningTargetCursor(self,mouse_posx,mouse_posy):
        self.target_group = pygame.sprite.GroupSingle()
        target_cursor=Target(mouse_posx,mouse_posy)
        self.target_group.add(target_cursor)
        return self.target_group

    def callingSeal(self):
        self.seal_group = pygame.sprite.GroupSingle()
        seal=Seal()
        self.seal_group.add(seal)
        return self.seal_group

    def callingSeal_2(self):
        self.seal_2_group = pygame.sprite.GroupSingle()
        seal_2=Seal_2()
        self.seal_2_group.add(seal_2)
        return self.seal_2_group

    def musicChoose(self,music,volume):
        pygame.mixer.music.unload()
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(volume)

    def beginningGame(self):
        for i in range(0,len(self.queue)):                                                                              #buz parçalarını yerine gönderir ve yerini alır almaz
            if self.ice_group_list[i].sprite.status=="waiting_for_playing":                                             #sudaki dalgalanmayı başlatır.
                self.waves_group_list[i].sprite.status="start_to_wave"
        waiting_for_playing_ice_list=[]                                                                                 #son buz parçaları da yerlerine gelmeye
        for i in self.ice_group_list:                                                                                   #başladığında bu kod
            if i.sprite.status=="waiting_for_playing":                                                                  #bloğu, penguenin
                waiting_for_playing_ice_list.append(i)                                                                  #hareketini başlatır
                if len(waiting_for_playing_ice_list)==36:
                    self.seal_2_group.sprite.status = "waiting_for_playing"
                elif len(waiting_for_playing_ice_list)==46:                                                             #
                    self.penguin_group.sprite.status="beginning"                                                        #
                    self.seal_group.sprite.status = "waiting_for_playing"                                               # fok'un durumunu "waiting_for_playing" yapar

    def howToPlay(self):
        self.how_to_play_control = True
        self.frame_group.sprite.status = "how_to_play"
        if 587<=self.mouse_posx<=629 and 495<=self.mouse_posy<=532:
            self.frame_group.sprite.status = "waiting_for_playing"
            self.how_to_play_control = False

    def startingGame(self):
        self.penguin_group.sprite.status = "playing"
        self.seal_group.sprite.status = "start_to_playing"                                                              # fok'un durumunu "playing" yapar
        self.seal_2_group.sprite.status = "start_to_playing"
        self.penguin_group.sprite.waiting_mode = "normal"                                                               # başlamaya tıklanınca oyun moduna geçer,ve pengueni normal bekleme moduna geçirir
        self.mouse_time = self.time
        self.penguin_replace_time = self.time                                                                           # penguen başlangıç modundan çıkıp oyun moduna dönerken yer değiştirme sayacını sıfırlıyor.
        self.mouse_posx, self.mouse_posy = 0, 0
        self.frame_group.sprite.status="playing"

    def iceDispersion(self,x_pos_hit_by,y_pos_hit_by,tool):
        for i in self.ice_group_list:                                                                                   # mouse ile tıklanan konumda buz parçası varsa hasar verir
            if ((i.sprite.arrangement_xpos - 30 <= x_pos_hit_by <= i.sprite.arrangement_xpos + 30) and
                    (i.sprite.arrangement_ypos - 10 <= y_pos_hit_by <= i.sprite.arrangement_ypos + 10)):
                i.sprite.health -= random.randint(16, 21)
                if tool=="pickaxe":
                    self.pickaxe_control=True
                else:
                    self.pickaxe_control = False
                if i.sprite.health <= 0:
                    breaking_place=i.sprite.breaking_place
                    for i in self.ice_group_list:
                        i.sprite.dispers(breaking_place)
                for i in range(0, len(self.ice_group_list)):                                                            # buzlardan kalanları gözden geçirir
                    if self.ice_group_list[i].sprite.status == "disappear":                                             # statüleri 'kaybolmuş' olanların dalgalarını ekrandan kaldırır
                        self.waves_group_list[i].sprite.status = "disappear"
                self.mouse_posx, self.mouse_posy = 0, 0

    def iceDispersionByPenguin(self):
        if self.penguin_on_ice_time>=800:
            self.iceDispersion(self.penguin_group.sprite.arrangement_xpos,self.penguin_group.sprite.arrangement_ypos,"penguin")
            self.penguin_on_ice_time = 0

    def actualIceListMaking(self):
        for nesne in self.ice_group_list:
            for numara in self.actual_ice_list:
                if nesne.sprite.status == "disappear" and nesne.sprite.queue_number==numara:
                    self.actual_ice_list.remove(numara)
        return self.actual_ice_list

    def generateNumberForMultiplication(self):
        self.number = ""
        self.number_a_b_list=[calculator.generateNumber_a(),calculator.generateNumber_b()]
        self.result=self.number_a_b_list[0]*self.number_a_b_list[1]
        self.result_a=calculator.generateFakeResult_a(self.result)
        self.result_b = calculator.generateFakeResult_b(self.result,self.result_a)
        self.number_a = str(self.number_a_b_list[0])
        self.number_b = str(self.number_a_b_list[1])
        self.result_locations_list = calculator.generateResultLocation()                                                # sonuçların ekranda yeralacağı konumları belirler
        self.color = (0, 0, 0)
        self.color_a = (0, 0, 0)
        self.color_b = (0, 0, 0)
        self.number_control = False
        self.choosing_result_with_mouse_control=True
        self.number_counter+=1

    def playingGame(self):
        if self.music_change == True and self.silence_music_control==True:
            self.musicChoose("silence.mp3", 1)
            self.music_counter+=1
            if self.music_counter >= 100:
                self.music_change = False
                self.silence_music_control = False
        if self.music_change==False and self.silence_music_control==False:
            self.musicChoose("background_joined.mp3", 1)
            self.music_change=True
        if self.target_group.sprite.status=="beginning" or self.target_group.sprite.status!="disappear":                #hedef kürsörünü oyunda başlatır.
            self.target_control = True                                                                                  #kürsörün kazma ile değişimini kontrol eder
            self.target_group.sprite.status="playing"
        if self.hit_control==True:
            self.iceDispersion(self.mouse_posx,self.mouse_posy,"pickaxe")
            self.penguin_on_ice_time+=90
            self.hit_control = False
        self.actualIceListMaking(),self.iceDispersionByPenguin()
        self.penguin_on_ice_time += 1
        self.seal_group.sprite.actualIceList(self.actual_ice_list)                                                      #ekranda bulunan güncel buz listesini seal scriptine gönderir
        self.seal_group.sprite.defineStatusPlaying(self.penguin_group.sprite.status)
        self.seal_2_group.sprite.seal1Location(self.seal_group.sprite.rect.midbottom)
        self.seal_2_group.sprite.actualIceList(self.actual_ice_list)                                                    # ekranda bulunan güncel buz listesini seal2 scriptine gönderir
        self.seal_2_group.sprite.defineStatusPlaying(self.penguin_group.sprite.status)
        self.seal_group.sprite.penguinLocation(self.penguin_group.sprite.arrangement_ypos)                              # penguenin konumunu birinci fok'a gönderir
        if self.time-self.mouse_time>=32000 and self.penguin_group.sprite.waiting_mode != "replace":                    #eğer oyuna bir süre mouse ile tıklanmassa
            self.penguin_group.sprite.waiting_mode = "waiting_to_move"                                                  #pengueni oyuncudan hamle bekleme moduna alır
            self.hey_sound.play()
            self.penguin_replace_time = self.time                                                                       # penguen çağırma modundan çıkıp oyun moduna dönerken yer değiştirme sayacını sıfırlıyor.
        elif self.penguin_group.sprite.waiting_mode != "replace":
            self.penguin_group.sprite.waiting_mode = "normal"
        if (self.penguin_group.sprite.waiting_mode == "normal" and
                (self.time-self.penguin_replace_time>=110000 or self.replace_control==True)):                           #penguenin yer değiştirme komut bloğu:
            self.penguin_group.sprite.waiting_mode = "replace"
            self.penguin_group.sprite.actualIceAreas(self.actual_ice_list)
            self.seal_2_group.sprite.penguinLocation(self.penguin_group.sprite.arrangement_ypos)                        # penguenin konumunu ikinci fok'a gönderir
            self.penguin_replace_time=self.time
            self.replace_control = False
            self.penguin_on_ice_time = 0
        toplam=0
        for number in self.actual_ice_list:                                                                             #penguenin yeriyle ekranda olan buzların yerlerini eşleştirerek kontrol eder.
            if self.penguin_group.sprite.position!=number:                                                              #eğer penguenin yerinde buz yoksa pengueni game_over durumuna geçirir.
                toplam+=1
                if toplam==len(self.actual_ice_list):
                    self.penguin_group.sprite.status = "game_over"
            elif self.penguin_group.sprite.position==number:
                break
        if self.pickaxe_control==True:
            toplam_treasure = 0
            for number in self.actual_ice_list:                                                                         # hazinenin yeriyle ekranda olan buzların yerlerini eşleştirerek kontrol eder.
                if self.treasure_group.sprite.position != number:                                                       # eğer hazinenin yerinde buz yoksa pengueni game_over_by_treasure durumuna geçirir.
                    toplam_treasure += 1
                    if toplam_treasure == len(self.actual_ice_list):
                        self.treasure_group.sprite.status="existing_on_hiding_location"
                        self.penguin_group.sprite.status = "game_over_by_treasure"
                elif self.penguin_group.sprite.position == number:
                    break
        if self.seal_group.sprite.catch_the_penguin==True or self.seal_2_group.sprite.catch_the_penguin==True:
            self.penguin_group.sprite.status = "game_over_by_seal"
        if (self.penguin_group.sprite.arrangement_xpos-35<=self.seal_group.sprite.seal_x_pos<=self.penguin_group.sprite.arrangement_xpos+35 and
                self.penguin_group.sprite.arrangement_ypos-15<=self.seal_group.sprite.seal_y_pos<=self.penguin_group.sprite.arrangement_ypos+15):
            self.seal_group.sprite.catch_the_penguin=True
            self.seal_group.sprite.status="game_over_by_seal"
        if (self.penguin_group.sprite.arrangement_xpos-35<=self.seal_2_group.sprite.seal2_x_pos<=self.penguin_group.sprite.arrangement_xpos+35 and
                self.penguin_group.sprite.arrangement_ypos-15<=self.seal_2_group.sprite.seal2_y_pos<=self.penguin_group.sprite.arrangement_ypos+15):
            self.seal_2_group.sprite.catch_the_penguin=True
            self.seal_2_group.sprite.status="game_over_by_seal"
        if self.number_control==True:
            self.generateNumberForMultiplication()
        self.choosingResultWithMouse()

    def finishingGameByPenguin(self):
        self.treasure_group.sprite.status="lost"
        self.penguin_group.sprite.status ="game_over"
        self.seal_group.sprite.status = "game_over"
        self.seal_2_group.sprite.status = "game_over"
        self.target_group.sprite.status="game_over"
        self.frame_group.sprite.status="game_over"
        if 1047 <= self.mouse_posx <= 1105 and 564 <= self.mouse_posy <= 607:
            self.game_quit_control = True
        elif 953 <= self.mouse_posx <= 1194 and 441 <= self.mouse_posy <= 519:
            self.gameInitials()

    def finishingGameByTreasure(self):
        self.treasure_group.sprite.status = "game_over"
        self.penguin_group.sprite.status ="game_over_by_treasure"
        self.seal_group.sprite.status="game_over_by_treasure"
        self.seal_2_group.sprite.status = "game_over_by_treasure"
        self.target_group.sprite.status = "game_over"
        self.frame_group.sprite.status = "game_over_by_treasure"
        if 1047<=self.mouse_posx<=1105 and 564<=self.mouse_posy<=607:
            self.game_quit_control=True
        elif 953 <= self.mouse_posx <= 1194 and 441 <= self.mouse_posy <= 519:
            self.gameInitials()

    def finishingGameBySeal(self):
        self.target_group.sprite.status = "game_over"
        self.penguin_group.sprite.status ="game_over_by_seal"
        self.frame_group.sprite.status = "game_over_by_seal"
        if 1047<=self.mouse_posx<=1105 and 564<=self.mouse_posy<=607:
            self.game_quit_control=True
        elif 953 <= self.mouse_posx <= 1194 and 441 <= self.mouse_posy <= 519:
            self.gameInitials()

    def choosingResultWithMouse(self):
        if self.penguin_group.sprite.status =="playing" and self.choosing_result_with_mouse_control==False:
            if 460<=self.mouse_posx<=580 and 565<=self.mouse_posy<=625:
                if self.result_locations_list[0]==480:
                    self.number_control = True
                    self.replace_control = True
                else:
                    if self.result_locations_list[1]==480:
                        self.color_a=(178,34,34)
                    else:
                        self.color_b = (178, 34, 34)
            elif 620<=self.mouse_posx<=700 and 565<=self.mouse_posy<=625:
                if self.result_locations_list[0] == 620:
                    self.number_control = True
                    self.replace_control = True
                else:
                    if self.result_locations_list[1]==620:
                        self.color_a=(178,34,34)
                    else:
                        self.color_b = (178, 34, 34)
            elif 755<=self.mouse_posx<=835 and 565<=self.mouse_posy<=625:
                if self.result_locations_list[0] == 760:
                    self.number_control = True
                    self.replace_control = True
                else:
                    if self.result_locations_list[1] == 760:
                        self.color_a = (178, 34, 34)
                    else:
                        self.color_b = (178, 34, 34)
            self.choosing_result_with_mouse_control = True

    def Draw(self):
        self.window.blit(self.Background0,(0, 0))
        for i in self.waves_group_list:
            i.update()
            i.draw(self.window)
        for i in self.ice_group_list:
            i.update()
            i.draw(self.window)
        self.treasure_group.update()
        self.treasure_group.draw(self.window)
        self.penguin_group.update()
        self.seal_group.update()
        self.seal_2_group.update()
        if(self.penguin_group.sprite.arrangement_ypos>=self.seal_group.sprite.seal_y_pos and self.penguin_group.sprite.arrangement_ypos>=self.seal_2_group.sprite.seal2_y_pos and
                self.seal_group.sprite.seal_y_pos>=self.seal_2_group.sprite.seal2_y_pos and self.penguin_group.sprite.status !="game_over_by_seal" and
                self.penguin_group.sprite.status !="game_over_by_treasure"):
            self.seal_2_group.draw(self.window)
            self.seal_group.draw(self.window)
            self.penguin_group.draw(self.window)
        elif (self.penguin_group.sprite.arrangement_ypos >= self.seal_group.sprite.seal_y_pos and self.penguin_group.sprite.arrangement_ypos >= self.seal_2_group.sprite.seal2_y_pos and
              self.seal_group.sprite.seal_y_pos < self.seal_2_group.sprite.seal2_y_pos and self.penguin_group.sprite.status !="game_over_by_seal" and
              self.penguin_group.sprite.status !="game_over_by_treasure"):
            self.seal_group.draw(self.window)
            self.seal_2_group.draw(self.window)
            self.penguin_group.draw(self.window)
        elif (self.penguin_group.sprite.arrangement_ypos<self.seal_group.sprite.seal_y_pos and self.penguin_group.sprite.arrangement_ypos>=self.seal_2_group.sprite.seal2_y_pos and
              self.penguin_group.sprite.status !="game_over_by_seal" and self.penguin_group.sprite.status !="game_over_by_treasure"):
            self.seal_2_group.draw(self.window)
            self.penguin_group.draw(self.window)
            self.seal_group.draw(self.window)
        elif (self.penguin_group.sprite.arrangement_ypos < self.seal_group.sprite.seal_y_pos and self.penguin_group.sprite.arrangement_ypos < self.seal_2_group.sprite.seal2_y_pos and
              self.seal_group.sprite.seal_y_pos>=self.seal_2_group.sprite.seal2_y_pos and self.penguin_group.sprite.status !="game_over_by_seal" and
              self.penguin_group.sprite.status !="game_over_by_treasure"):
            self.penguin_group.draw(self.window)
            self.seal_2_group.draw(self.window)
            self.seal_group.draw(self.window)
        elif (self.penguin_group.sprite.arrangement_ypos < self.seal_group.sprite.seal_y_pos and self.penguin_group.sprite.arrangement_ypos < self.seal_2_group.sprite.seal2_y_pos and
              self.seal_group.sprite.seal_y_pos<self.seal_2_group.sprite.seal2_y_pos and self.penguin_group.sprite.status !="game_over_by_seal" and
              self.penguin_group.sprite.status !="game_over_by_treasure"):
            self.penguin_group.draw(self.window)
            self.seal_group.draw(self.window)
            self.seal_2_group.draw(self.window)
        elif (self.penguin_group.sprite.arrangement_ypos >= self.seal_group.sprite.seal_y_pos and self.penguin_group.sprite.arrangement_ypos < self.seal_2_group.sprite.seal2_y_pos and
              self.penguin_group.sprite.status !="game_over_by_seal" and self.penguin_group.sprite.status !="game_over_by_treasure"):
            self.seal_group.draw(self.window)
            self.penguin_group.draw(self.window)
            self.seal_2_group.draw(self.window)
        if self.penguin_group.sprite.status =="game_over_by_seal":
            self.seal_2_group.draw(self.window)
            self.seal_group.draw(self.window)
            self.penguin_group.draw(self.window)
        elif self.penguin_group.sprite.status =="game_over_by_treasure":
            self.penguin_group.draw(self.window)
        self.snow_group.update()
        self.snow_group.draw(self.window)
        self.target_group.update()
        self.target_group.draw(self.window)
        self.frame_group.update()
        self.frame_group.draw(self.window)

        if self.penguin_group.sprite.status =="playing":
            self.window.blit(self.Background1, (300, 420))
            self.font = pygame.font.Font(None, 106)
            self.number_surface_number_a = self.font.render(self.number_a, True, (0, 0, 0))
            self.window.blit(self.number_surface_number_a, (520, 450))
            self.font = pygame.font.Font(None, 90)
            self.number_surface_X = self.font.render("X", True, (0, 0, 0))
            self.window.blit(self.number_surface_X, (595, 460))
            self.font = pygame.font.Font(None, 106)
            self.number_surface_number_b = self.font.render(self.number_b, True, (0, 0, 0))
            self.window.blit(self.number_surface_number_b, (670, 450))
            self.number_surface_equal = self.font.render("=", True, (0, 0, 0))
            self.window.blit(self.number_surface_equal, (735, 460))
            self.number_surface = self.font.render(self.number, True, (0, 0, 0))
            self.window.blit(self.number_surface,(790,450))
            self.result_surface = self.font.render(str(self.result), True, self.color)
            self.window.blit(self.result_surface, (self.result_locations_list[0], 540))
            self.result_a_surface = self.font.render(str(self.result_a), True, self.color_a)
            self.window.blit(self.result_a_surface, (self.result_locations_list[1], 540))
            self.result_b_surface = self.font.render(str(self.result_b), True, self.color_b)
            self.window.blit(self.result_b_surface, (self.result_locations_list[2], 540))

        self.Clock.tick(120)
        pygame.display.update()

    def GameLoop(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT or self.game_quit_control==True:
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_posx, self.mouse_posy = pygame.mouse.get_pos()                                               #alınan koordinat değerleri buzların kırılmasında kullanılıyor.
                if not (self.seal_group.sprite.seal_x_pos-25<=self.mouse_posx<=self.seal_group.sprite.seal_x_pos+25 and
                    self.seal_group.sprite.seal_y_pos-40<=self.mouse_posy<=self.seal_group.sprite.seal_y_pos+20):
                    self.hit_control = True
                    self.target_group.sprite.pickaxControl(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],self.penguin_group.sprite.status)   #koordinat değerleri target nesnesine gönderilip kazma grafikleri başlatılıyor.
                    self.mouse_time=pygame.time.get_ticks()                                                                                         #mouse tıklama zamanı penguen bekleme grafikleri için alınıyor.
                if (self.penguin_group.sprite.status == "playing" and self.choosing_result_with_mouse_control == True
                     and 460<=self.mouse_posx<=835 and 565<=self.mouse_posy<=625 and self.number_counter>0):                                       #oyun esnasında işlem sonuçlarına tıklandığında tekrar tıklanabilmesini sağlar
                    self.choosing_result_with_mouse_control = False
                #print(self.mouse_posx, self.mouse_posy)
            if event.type ==self.SNOW_EVENT and self.penguin_group.sprite.status == "playing":
                snow=Snow()
                self.snow_group.add(snow)
            if event.type == pygame.MOUSEMOTION and self.target_control==True and self.target_group.sprite.return_to_playing_game==True:        #kazma grafikleri oynarken mouse konumlarını alıp kazmanın yerini değiştirmememsi için
                self.target_group.sprite.targetCursorMovements(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE and self.replace_control==False:
                self.replace_control = True
            if event.type == pygame.KEYDOWN and self.penguin_group.sprite.status=="playing" and len(self.number)<2:
                if event.key == pygame.K_0 or event.key == pygame.K_KP_0 :
                    self.number+="0"
                elif event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                    self.number+="1"
                elif event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                    self.number+="2"
                elif event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                    self.number+="3"
                elif event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                    self.number+="4"
                elif event.key == pygame.K_5 or event.key == pygame.K_KP_5:
                    self.number+="5"
                elif event.key == pygame.K_6 or event.key == pygame.K_KP_6:
                    self.number+="6"
                elif event.key == pygame.K_7 or event.key == pygame.K_KP_7:
                    self.number+="7"
                elif event.key == pygame.K_8 or event.key == pygame.K_KP_8:
                    self.number+="8"
                elif event.key == pygame.K_9 or event.key == pygame.K_KP_9:
                    self.number+="9"
            if event.type == pygame.KEYDOWN and self.penguin_group.sprite.status == "playing" and len(self.number)>0:
                if (event.key == pygame.KSCAN_DELETE or event.key == pygame.K_BACKSPACE) :
                    self.number=calculator.correctingNumbers(self.number)
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    if calculator.calculate(self.number,self.number_a,self.number_b) and self.number_control==False and self.replace_control == False:
                        self.number_control = True
                        self.replace_control = True
                    elif calculator.calculate(self.number, self.number_a,self.number_b)==False and self.number_control == False and self.replace_control == False:
                        self.number = ""

        self.Key=pygame.key.get_pressed()
        if self.Key[pygame.K_ESCAPE]:
            return "QUIT"

        self.Draw()
        self.time=pygame.time.get_ticks()

        if self.penguin_group.sprite.status == "waiting":
            self.beginningGame()
        elif self.penguin_group.sprite.status == "waiting_for_start":
            if self.how_to_play_control==False and 509<=self.mouse_posx<=751 and 528<=self.mouse_posy<=604:
                self.startingGame()
            elif (607<=self.mouse_posx<=662 and 651<=self.mouse_posy<=695) or self.how_to_play_control==True:
                self.howToPlay()
        elif self.penguin_group.sprite.status == "playing" and self.target_group.sprite.return_to_playing_game==True and self.treasure_group.sprite.status=="playing":                           #kazma grafikleri ekranda oynarken, oyuna dönmemesi için
            self.playingGame()
        elif self.penguin_group.sprite.status == "game_over":
            self.finishingGameByPenguin()
        elif self.penguin_group.sprite.status == "game_over_by_treasure" or self.treasure_group.sprite.status=="exist":
            self.finishingGameByTreasure()
        elif self.penguin_group.sprite.status == "game_over_by_seal":
            self.finishingGameBySeal()

Game=GameCore()

while True:

    Status=Game.GameLoop()

    if Status=="QUIT":
        break

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()