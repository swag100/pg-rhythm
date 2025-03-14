import pygame

class Meter:
    def __init__(self, playstate, start_beat, length, pattern):
        self.chart = playstate.chart
        self.conductor = playstate.conductor

        self.length = length
        self.pattern = pattern
        self.start_beat = start_beat

        #Parse spritesheet
        self.sprites = []
        spritesheet = pygame.image.load('assets/images/meter.png').convert_alpha()
        for i in range(4):
            sprite = pygame.Surface((16, 16), pygame.SRCALPHA)
            sprite.blit(spritesheet, (-(i * 16), 0))

            self.sprites.append(sprite)

        TIME_NUMERATOR = 4 #How many beats in a measure?
        TIME_DENOMINATOR = 4 #How many steps in a beat?

        line_count = length // (TIME_NUMERATOR * TIME_DENOMINATOR)
        step_count = length // line_count

        self.line_images = []

        #Create rows
        for _ in range(line_count):

            line_image = pygame.Surface((step_count * 16, 16), pygame.SRCALPHA)

            for step_marker in range(step_count):
                sprite_index = 0
                if step_marker % TIME_DENOMINATOR == 0: 
                    sprite_index += 2

                line_image.blit(self.sprites[sprite_index], (step_marker * 16, 0))
            
            self.line_images.append(line_image)

        print(len(self.line_images))
        
    def tick(self, dt):
        pass

    def draw(self, screen):
        for i in range(len(self.line_images)):
            screen.blit(self.line_images[i], (16, i * 16))