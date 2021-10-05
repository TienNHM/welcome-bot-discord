import os
import datetime
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MESSAGE = os.getenv('MESSAGE')
CHANNEL_ID = os.getenv('CHANNEL_ID')
THUMBNAIL = os.getenv('THUMBNAIL')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_member_join(self, member):
        # guild = member.guild 
        await member.create_dm()
        
        msg = f"🥰 Để có thể truy cập vào tất cả các channel của discord, các bạn vui lòng đổi biệt danh theo định dạng:\n" + \
            "```\n" + \
            "Họ tên - MSSV - Lớp \n" + \
            "``` \n" + \
            "👉 Sau đó, nhớ điền form: https://tinyurl.com/Discord-K21-FITUTE để được set role nhé. \n " + \
            "💥 Và đừng quên đọc nội quy tại đây:"
            
        msg = msg if MESSAGE is None else MESSAGE
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(),
                                color=discord.Color.blue())
        # embed.set_author(name=member.recipient, icon_url=member.avatar_url)
        embed.add_field(name="🌟🌟🌟", value=f"\n💥 Chào mừng {member.mention} đến với Server {member.guild.name} nhé! \n\n{msg} <#{CHANNEL_ID}>")
        embed.set_thumbnail(url=THUMBNAIL)

        await member.dm_channel.send(embed=embed)
        # await guild.system_channel.send(embed=embed)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
