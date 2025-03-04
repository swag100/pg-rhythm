import pygame
from states.state import State

from components.conductor import Conductor
from components.song import Song

class PlayState(State):
    def __init__(self):
        pass #preload any necessary assets
        
    def start(self, persistent_data): 
        super().__init__() #reset self.done

        #Set our persistent data to the data from our old state
        self.persistent_data = persistent_data

        #Gameplay objects
        self.conductor = Conductor(110) #read from chart later.
        self.song = Song('stage1', self.conductor)

        self.song.start()

    def handle_event(self, event): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                self.song.start('awful')
            if event.key == pygame.K_1:
                self.song.start('bad')
            if event.key == pygame.K_2:
                self.song.start('good')
            if event.key == pygame.K_3:
                self.song.start('cool')

    def tick(self, dt): 
        self.conductor.tick(dt)

    def draw(self, screen):
        screen.fill((0,0,0))