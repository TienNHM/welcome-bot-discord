import os
import datetime
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MESSAGE = os.getenv('MESSAGE')
# CHANNEL_ID = os.getenv('CHANNEL_ID')
THUMBNAIL = os.getenv('THUMBNAIL')
RULES = os.getenv('RULES')
RULE_ICON = os.getenv('RULE_ICON')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        
        #### WELCOME
        msg = f"🥰 Để có thể truy cập vào tất cả các channel của discord, các bạn vui lòng đổi biệt danh theo định dạng:\n" + \
            "```\n" + \
            "Họ tên - MSSV - Lớp \n" + \
            "``` \n" + \
            "👉 Sau đó, nhớ điền form: https://tinyurl.com/Discord-K21-FITUTE để được set role nhé. \n "
            
        msg = msg if MESSAGE is None else MESSAGE
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(),
                                color=discord.Color.blue())
        embed.add_field(name="🌟🌟🌟", value=f"\n💥 Chào mừng {member.mention} đến với Server {member.guild.name} nhé! \n\n{msg}")
        embed.set_thumbnail(url=THUMBNAIL)

        await member.dm_channel.send(embed=embed)
        
        #### RULES
        rule = discord.Embed(timestamp=datetime.datetime.utcnow(),
                                color=discord.Color.red())
        rule.add_field(name="📌 Nội quy", value=RULES)
        rule.set_thumbnail(url=RULE_ICON)
        await member.dm_channel.send(embed=rule)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
