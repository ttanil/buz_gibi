import pygame

pygame.init()

class Frame(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_frame = pygame.image.load("frame1-2.png").convert_alpha()
        self.image_game_over = pygame.image.load("game_over1.png").convert_alpha()
        self.image_you_win = pygame.image.load("you_win1.png").convert_alpha()
        self.image_start = pygame.image.load("start2.png").convert_alpha()
        self.image_how_to_play = pygame.image.load("writing_frame_button.png").convert_alpha()

        self.image = self.image_frame
        self.rect = self.image.get_rect()
        self.rect.center=-150,90

        self.status = "beginning"
        self.counter=0

        self.game_over_control=False

    def update(self):
        if self.status=="beginning" and self.counter%2==0:
            self.rect.centerx+=1
            if self.rect.centerx>1000:
                self.rect.centerx += 2
            if self.rect.centerx>1600:
                self.status = "waiting_for_playing"
        elif self.status == "waiting_for_playing":
            self.image=self.image_start
            self.rect.center=650,550
        elif self.status == "how_to_play":
            self.image = self.image_how_to_play
            self.rect.center = 485, 50
        elif self.status=="beginning":
            self.counter += 1
        elif self.status == "playing":
            self.rect.center = -100, -100
            self.counter=0
        elif self.status=="game_over" or self.status=="game_over_by_seal":
            self.writingToScreen()
        elif self.status=="game_over_by_treasure":
            self.writingToScreen()


    def writingToScreen(self):
        if self.game_over_control == False:
            self.counter = 0
            self.game_over_control = True
        else:
            self.counter += 1
        if self.counter >= 180:
            if self.status=="game_over" or self.status=="game_over_by_seal":
                self.image = self.image_game_over
                self.rect.center = 160, 100
            elif self.status=="game_over_by_treasure":
                self.image = self.image_you_win
                self.rect.center = 160, 100
            self.game_over_control = False
            self.counter = 0