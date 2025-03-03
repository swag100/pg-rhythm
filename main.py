import pygame
from constants import *

from states.playstate import PlayState

class Game:
    def __init__(self):
        pygame.init()

        self.done = False

        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.screen = pygame.surface.Surface(SCREEN_SIZE)

        self.clock = pygame.time.Clock()

        #States logic
        self.states = {
            'PlayState': PlayState(),
        }

        self.state_name = 'PlayState' #initial state
        self.state = self.states[self.state_name]

        #Start state and give it access to this object
        self.state.start({'game': self})

        #NOW BEGIN THE LOOP!
        self.begin()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

            self.state.handle_event(event)

    def tick(self, dt):
        if self.state.done: 
            self.set_state()

        self.state.tick(dt)

    def draw(self):
        self.state.draw(self.screen)

    def set_state(self):
        next_state = self.state.next_state
        persistent_data = self.state.persistent_data

        #Set new state, pass persistent data
        if next_state in self.states.keys():
            self.state_name = next_state
            self.state = self.states[self.state_name]
        else:
            print('Failed to find', next_state)
            
        self.state.start(persistent_data)

    def begin(self):
        while not self.done:
            dt = self.clock.tick(FRAMERATE) / 1000

            self.handle_events()
            self.tick(dt)
            self.draw()

            self.window.blit(
                pygame.transform.scale_by(self.screen, PIXEL_SIZE)
            )
            pygame.display.flip()

Game()