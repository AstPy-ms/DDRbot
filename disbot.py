import discord
import getsongs
import gosh

# 接続に使うオブジェクト / starting
client = discord.Client()

# 起動した確認 / confirm starting
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



# こっから処理 / processing
@client.event
async def on_message(message):

    # 課題曲 曲数 難易度範囲 / ex. 課題曲 3 17-19) 
    if message.content.startswith("課題"):
        if client.user != message.author.name:
            currentMessage = message.content
            sentMessage = currentMessage.split()
            numOfSongs = int(sentMessage[1])
            rangeOfDifficulty = sentMessage[2].split("-")
            difficulty = []
            for i in range(int(rangeOfDifficulty[0]), int(rangeOfDifficulty[1])+1 ):
                difficulty.append(i)
            
            songs, difficultyOfSongs = getsongs.getSongs(numOfSongs, difficulty)
            sendMessage = ""
            for i in range(len(songs)):
                sendMessage = sendMessage + f'{songs[i]} 足{difficultyOfSongs[i]}\n'
            channel = message.channel
            await channel.send(sendMessage)

    if message.content.startswith("消去"):
        if client.user != message.author.name:
            await message.channel.purge()

    if message.content.startswith("help"):
        if client.user != message.author.name:
            channel = message.channel
            await channel.send("課題 {曲数} {難易度の範囲} と送信してください。\n1つの難易度の場合は15-15のように入力してください。\nex.\) 課題 3 15-18\n")

# ここにはdiscordのbotのトークンを入れる / fill in "token"
TOKEN = gosh.requestsToken()
client.run(TOKEN)