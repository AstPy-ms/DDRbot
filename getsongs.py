import random
import json

def getSongs(numOfSongs, difficultyList):

    songs = []
    difficultyOfSongs = []

    for i in range(0, numOfSongs):
        num = random.randint(0, len(difficultyList)-1)
        with open(f'{difficultyList[num]}.json') as f:
            j = json.load(f)
            id = random.randint(1, len(j))
            item = next((item for item in j if item['id'] == id), None)
            songs.append(item['曲名'])
            difficultyOfSongs.append(difficultyList[num])


    return(songs, difficultyOfSongs)