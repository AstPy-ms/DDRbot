import random
import json

# getSongsという関数
# numOfSongs(曲数)、dificultyList(難易度表)を引数に取る。
def getSongs(numOfSongs, difficultyList):

    # 空のListを宣言しておく
    songs = []
    difficultyOfSongs = []

    # for文を使って、曲数回ループする。
    for i in range(0, numOfSongs):
        # randomというものを使って乱数を生成する。
        # 範囲は、0 ~ len(difficultyList) - 1
        num = random.randint(0, len(difficultyList)-1)
        # withコマンドを使ってjsonファイルを読み込む
        with open(f'{difficultyList[num]}.json') as f:
            j = json.load(f)
            # 乱数を生成
            id = random.randint(1, len(j))
            item = next((item for item in j if item['id'] == id), None)
            songs.append(item['曲名'])
            difficultyOfSongs.append(difficultyList[num])


    return(songs, difficultyOfSongs)