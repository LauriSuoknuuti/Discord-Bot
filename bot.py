import discord

token = "NTYyMzYxMTMyNjY1Mjc0Mzcx.XKJuvw.Nyn-SaliCD6S_IbR6lqfSrLOwYk"

client = discord.Client()
id = client.get_guild(330741882147700736)


@client.event
async def on_message(message):
    if message.content.find("hi") != -1:
        await message.channel.send("hello")

client.run(token)
