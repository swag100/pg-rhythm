import pygame
from states.state import State

from components.chart import Chart
from components.conductor import Conductor
from components.song import Song
from components.meter import Meter

class PlayState(State):
    def __init__(self):
        pass #preload any necessary assets
        
    def start(self, persistent_data): 
        super().__init__() #reset self.done

        #Set our persistent data to the data from our old state
        self.persistent_data = persistent_data

        song_name = 'stage1' #read this from persistent data later.

        #Gameplay objects
        self.chart = Chart(song_name)
        self.conductor = Conductor(self.chart.bpm)
        self.song = Song(song_name, self.conductor)

        self.meter = Meter(self, 0, 48, [])

        #Preload all song phrases before starting.
        self.song.load_phrases()

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
                
            if event.key == pygame.K_w:
                self.song.play_phrase('parappa', 'block')
            if event.key == pygame.K_s:
                self.song.play_phrase('parappa', 'kick')
            if event.key == pygame.K_a:
                self.song.play_phrase('parappa', 'punch')
            if event.key == pygame.K_d:
                self.song.play_phrase('parappa', 'chop')
        if event.type == pygame.USEREVENT:
            print(event.cur_beat, self.conductor.song_position)

    def tick(self, dt): 
        if self.song.begun:
            self.conductor.tick(dt)

    def draw(self, screen):
        screen.fill((128,)*3)
        
        self.meter.draw(screen)