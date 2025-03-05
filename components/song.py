import os
import pygame

class Song:
    def __init__(self, name, conductor):
        self.name = name
        self.conductor = conductor

        self.begun = False

    def load_phrases(self):
        self.phrases = {
            'instructor': {},
            'parappa': {}
        }

        song_path = f'assets/songs/{self.name}/phrases/'

        for character in ['instructor', 'parappa']:
            for filename in os.listdir(os.path.join(song_path, character)):
                sound = pygame.Sound(os.path.join(song_path, character, filename))

                phrase = filename.split('.')[0]

                self.phrases[character][phrase] = sound
        
        print(self.phrases)
    
    def play_phrase(self, character, phrase):
        self.phrases[character][phrase].play()

    def start(self, rating = 'good'):
        pygame.mixer.music.load(f'assets/songs/{self.name}/instrumentals/{rating}.mp3')
        pygame.mixer.music.play(start=self.conductor.song_position)

        self.begun = True