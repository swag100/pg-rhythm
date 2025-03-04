import os
import pygame

class Song:
    def __init__(self, name, conductor):
        self.name = name
        self.conductor = conductor

    def get_song_files(self):
        self.instrumentals = {}
        self.phrases = {}

        song_path = f'assets/songs/{self.name}/instrumentals'

        for filename in os.listdir(os.path.join(song_path, 'instrumentals')):
            self.instrumentals[filename.split('.')[0]] = pygame.Sound(
                os.path.join(song_path, 'instrumentals', filename)
            )
        
        print(self.instrumentals)

    def start(self, rating = 'good'):
        pygame.mixer.music.load(f'assets/songs/{self.name}/instrumentals/{rating}.mp3')
        pygame.mixer.music.play(start=self.conductor.song_position)