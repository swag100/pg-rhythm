import pygame
import math

class Conductor:
    def __init__(self, bpm):
        self.bpm = bpm
        
        #Duration of beat in seconds
        self.crochet = 60 / bpm

        self.song_position = 0

        self.cur_beat = 0
        self.cur_beat_time = 0

    def tick(self, dt):
        self.song_position += dt

        self.cur_beat_time = (self.song_position / self.crochet)
        self.cur_beat = math.floor(self.cur_beat_time)

        if self.old_beat != self.cur_beat: #BEAT HIT
            self.old_beat = self.cur_beat
            pygame.event.post(pygame.Event(pygame.USEREVENT, {'cur_beat': self.cur_beat}))