import pygame
from states.state import State

from components.chart import Chart
from components.conductor import Conductor
from components.song import Song

class PlayState(State):
    def __init__(self):
        pass #preload any necessary assets
        
    def start(self, persistent_data): 
        super().__init__() #reset self.done

        #Set our persistent data to the data from our old state
        self.persistent_data = persistent_data

        song_name = 'stage1'

        #Gameplay objects
        self.chart = Chart(song_name)
        self.conductor = Conductor(110) #read from chart later.
        self.song = Song(song_name, self.conductor)

        #PLAY THE SONG!
        self.song.start()

    def handle_event(self, event): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.song.start('awful')
            if event.key == pygame.K_2:
                self.song.start('bad')
            if event.key == pygame.K_3:
                self.song.start('good')
            if event.key == pygame.K_4:
                self.song.start('cool')
        if event.type == pygame.USEREVENT:
            print(event.cur_beat)

    def tick(self, dt): 
        self.conductor.tick(dt)

    def draw(self, screen):
        screen.fill((0,0,0))