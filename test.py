import discord, datetime, asyncio, random
intents = discord.Intents.all()     #설정소스코드
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("성공적으로 봇이 시작되었습니다.")     #시작소스코드
    game = discord.Game("펌킹갈비 봇 활동하는중")
    await client.change_presence(status=discord.Status.online, activitiy=game)


@client.event
async def on_message(message):
    if message.content == "안녕":      
        await message.channel.send("안녕하세요")
    if message.content == "잘가":      
        await message.channel.send("안녕히가세요")
    if message.content == "ㅅㅂ":      
        await message.channel.send("욕하지마세요ㅠㅠ")   
    if message.content == "ㅇㄴ":      
        await message.channel.send("네?")
    if message.content == "닥쳐":      
        await message.channel.send("닥치라니요 ㅠㅠ")
    if message.content == "흠":      
        await message.channel.send("흐음") 
    if message.content == "코로나":      
        await message.channel.send("ㅋㄹㄴ요?") 
    if message.content == "?":      
        await message.channel.send("에?") 
    if message.content == "저게 뭐지":      
        await message.channel.send("모르겠네요 ㅡㅡ.")
    if message.content == "반갑다":      
        await message.channel.send("반가워요.")
    if message.content == "잘가라":      
        await message.channel.send("네..")


    if message.content == "개새끼":      
        await message.channel.send("전 봇이랍니다.")
    if message.content == "ㄲㅈ":      
        await message.channel.send("전 봇이에요 꺼질수가 없어요.")
    if message.content == "ㅄ":      
        await message.channel.send("병신이 무엇인가요?")
    if message.content == "뭐야":      
        await message.channel.send("네?")
    if message.content == "하":      
        await message.channel.send("무슨 걱정 있으신가요?")
    if message.content == "ㅆㅂ":      
        await message.channel.send("욕하지마세요ㅠㅠ")
    if message.content == "미친넘":      
        await message.channel.send("봇은 미치지 않았어요.")
    if message.content == "ㅅㄲ":      
        await message.channel.send("욕하지마세요ㅠㅠ")
    if message.content == "화긴":      
        await message.channel.send("화긴..?")
    if message.content == "꺼져":
        await message.channel.send("봇은 꺼질수가 없어요.")
    if message.content == "확인":
        await message.channel.send("확인..?")
    if message.content == "ㅋ":
        await message.channel.send("무슨 재미있으신일이라도?")

    if message.content == "뒤져":
        await message.channel.send("전 죽지 않아요.")

    
    if message.content == "!도움말":
        embed = discord.Embed(timestamp=message.created_at, colur=discord.Colour.red(), title="```펌킹갈비 봇 도움말```", description="```!도움말 : 여러가지 명령어를 보여줌.``` ```!채널메시지 : !채널메시지 (채널아이디) (보낼말)을 하면 채널에 메시지를 보냄.```  ```!내정보 : !내정보를 하면 자신의 정보를 보여줌.``` ```!청소 : !청소 (글자 개수)를 하면 글자를 삭제함.```")
        await message.channel.send(embed=embed)

    if message.content.startswith(f"!채널메시지"):
        ch = client.get_channel(int(message.content[7:25]))     #대화소스코드
        await ch.send(message.content[26:])

    if message.content == '!내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"```{message.author.mention}의 가입일은 {date.year}년 {date.month}월{date.day}일입니다```")
        await message.channel.send(f"```{message.author.mention}의 이름은 {user.name}, 아이디는 {user.id}, 닉네임은 {user.display_name}입니다```")
        await message.channel.send(message.author.avatar_url)

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"```{number}개의 메시지를 삭제했습니다.```")

    if message.content == "!가위" or message.content == "!바위" or message.content == "!보":
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            if message.content == "!가위":
                await message.channel.send("비겼습니다")
            elif message.content == "!바위":
                await message.channel.send("제가 졌습니다")
            else:
                await message.channel.send("제가 이겼습니다")
        elif bot_response == 2:
            if message.content == "!가위":
                await message.channel.send("제가 이겼습니다")
            elif message.content == "!바위":
                await message.channel.send("비겼습니다")
            else:
                await message.channel.send("제가 졌습니다")
        else:
            if message.content == "!가위":
                await message.channel.send("제가 졌습니다")
            elif message.content == "!바위":
                await message.channel.send("제가 이겼습니다")
            else:
                await message.channel.send("비겼습니다")    
        
client.run("Nzk0NDIxODgyMTUzNTk5MDM2.X-6lCA.g8oPz-V1KXWAgHeuLjoCpWSQbhM")     #실행소스코드    
