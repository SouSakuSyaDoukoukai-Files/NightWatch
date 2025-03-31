import discord
from datetime import datetime
from zoneinfo import ZoneInfo

intents = discord.Intents.all()
client = discord.Client(intents = intents)

@client.event
async def on_message(msg):
    if "<@&1330415261345644676>" in msg.content and msg.guild.id == 1326412691925106748:
        now = datetime.now(ZoneInfo("Asia/Tokyo"))
        hour = now.hour
        if hour >= 22 or hour <= 6:
            await msg.reply(f"【警告】<@{msg.author.id}>\n日中用メンションの利用はは7時~21時用の間のみ許可されています")
            await msg.delete()
    return

client.run("Insert Token Here")
