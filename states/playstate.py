import pygame
from states.state import State

from components.song import Song

class PlayState(State):
    def __init__(self):
        pass #preload any necessary assets
        
    def start(self, persistent_data): 
        super().__init__() #reset self.done

        #Set our persistent data to the data from our old state
        self.persistent_data = persistent_data

        #Playstate objects
        self.song = Song('Chop Chop Master Onion\'n RAP')

    def handle_event(self, event): 
        pass

    def tick(self, dt): 
        pass

    def draw(self, screen):
        screen.fill((0,0,0))