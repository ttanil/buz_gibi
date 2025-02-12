import pygame,random,breaking

pygame.init()

class Treasure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_treasure = pygame.image.load("treasure0.png").convert_alpha()
        self.image_treasure_big = pygame.image.load("treasure_big.png").convert_alpha()

        self.image = self.image_treasure
        self.rect = self.image.get_rect()
        self.rect.midbottom = -100, -100

        self.status="playing"
        self.game_over_counter=0

        self.defineHidingLocation()

    def update(self):
        if self.status=="playing":
            pass
        elif self.status=="existing_on_hiding_location":
            self.existingOnScreen()
        elif self.status=="game_over":
            self.game_over_counter+=1
            if self.game_over_counter==100:
                self.finnishingScreen()


    def defineHidingLocation(self):
        self.position=random.randint(0,48)
        print(self.position)
        return self.position

    def existingOnScreen(self):
        self.rect.center = breaking.destination[self.position][0], breaking.destination[self.position][1]-10
        return self.rect.center

    def finnishingScreen(self):
        self.image=self.image_treasure_big
        self.rect.center = 40,360