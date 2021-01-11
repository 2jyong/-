import discord, asyncio, json, random
import os
from random import *

client = discord.Client()

access_token = os.environ['BOT_TOKEN']
token = access_token

person = []
personmoney = {}


@client.event
async def on_ready():
    print("봇이 실행되었습니다.")

@client.event
async def on_message(message):
    global person
    global personmoney

    if message.content.startswith("무스비회원"):
        await message.channel.send(person)
        await message.channel.send(personmoney)
    if message.content.startswith("무스비가입"):
        user = message.author.name
        if user in person:
            await message.channel.send(f"{message.author.mention}님은 이미 가입이 되어 있습니다.")
        else:
            person.append(user)
            once = person.index(user)
            personmoney[once] = 3000
            await message.channel.send(f"{message.author.mention}님의 가입이 완료되었습니다.")
            await message.channel.send(person)

    if message.content.startswith("무스비지갑"):
        user = message.author.name
        if user in person:
            once = person.index(user)
            twice = personmoney[once]
            await message.channel.send(f"{message.author.mention}의 지갑엔 {twice}원 있습니다.")
    
    '''
    if message.content.startswith("무스비거래"):
        user = message.author.name
        trd = message.content.replace("무스비거래 ", "")
        trdmaker = trd.index(".")
        trdname = trd[:trdmaker]
        trdnum = int(trd[trdmaker + 1:])
        once = person.index(user)
        twice = personmoney[once]
        third = person.index(trdname)
        forth = personmoney[third]
        await message.channel.send(twice - trdnum)
        trds = twice - trdnum
        await message.channel.send(forth + trds)
    '''
    if message.content.startswith("무스비거래"):
        user = message.author.name
        trd = message.content.replace("무스비거래 ", "")
        trdmarker = trd.index(".")
        trdname = trd[:trdmarker]
        trdnum = int(trd[trdmarker + 1:])
        once = person.index(user)
        twice = personmoney[once]
        third = person.index(trdname)
        forth = personmoney[third]
        if user in person:
            if trdname in person:
                if trdnum <= twice:
                    trds1 = twice - trdnum
                    trds2 = twice - trds1
                    trds3 = forth + trds2
                    personmoney[once]=trds1
                    personmoney[third]=trds3
                    await message.channel.send(f"{message.author.mention}께서 {trdname}님에게 {trdnum}원을 이체하셨습니다.")
                elif trdnum > twice:
                    await message.channel.send("잔고부족")
       
        else:
            await message.channel.send("가입되지 않은 사용자 입니다.")

        

    if message.content.startswith("무스비로또"):
        if(message.author.guild_permissions.administrator):
            lotto = randint(0,45)
            await message.channel.send(lotto)
            lotto = randint(0,45)
            await message.channel.send(lotto)
            lotto = randint(0,45)
            await message.channel.send(lotto)
            lotto = randint(0,45)
            await message.channel.send(lotto)
            lotto = randint(0,45)
            await message.channel.send(lotto)
            lotto = randint(0,45)
            await message.channel.send(lotto)

    if message.content.startswith("로또상금"):
        if(message.author.guild_permissions.administrator):
            user = message.author
            moneygive = message.content.replace("로또상금 ", "")
            givemarker = moneygive.index(".")
            getname = moneygive[:givemarker]
            getmoney = int(moneygive[givemarker + 1:])
            once = person.index(getname)
            twice = personmoney[once]
            give1 = twice + getmoney
            personmoney[once] = give1
            await message.channel.send(f"{message.author.mention}님이 로또 상금 {getmoney}원을 {getname}님의 지갑으로 이체하였습니다.")



client.run(access_token) 
