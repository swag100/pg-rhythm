import json

class Chart:
    def __init__(self, name):
        self.path = f'assets/data/songs/{name}.json'

        with open(self.path) as file:
            chart = json.load(file)
        file.close()

        self.song_title = chart['songName']
        self.song_bpm = chart['bpm']

        turns = chart['turns']
        
        for a in turns:
            print(a)