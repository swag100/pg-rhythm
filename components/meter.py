import pygame

class Meter:
    def __init__(self, playstate, start_beat, length, pattern):
        self.chart = playstate.chart
        self.conductor = playstate.conductor

        self.length = length
        self.pattern = pattern
        self.start_beat = start_beat

        self.images = []

        #Parse spritesheet
        spritesheet = pygame.image.load('assets/images/meter.png').convert_alpha()
        for i in range(4):
            sprite = pygame.Surface((16, 16), pygame.SRCALPHA)
            sprite.blit(spritesheet, (-(i * 16), 0))

            self.images.append(sprite)

        self.image = pygame.Surface((length * 16, max(16, (length // 16) * 16)), pygame.SRCALPHA)
        row = 0
        for i in range(length):
            #Stars on beat
            sprite_index = 0
            if i % 4 == 0:
                sprite_index += 2

            #Meter wrapping
            if i >= 16:
                i-=16
                row = (i // 16) + 1

            self.image.blit(self.images[sprite_index], (i*16, row*16))
        
    def tick(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.image, (16, 16))