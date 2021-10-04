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
        guild = member.guild
        if guild.system_channel is not None:
            msg = f"🥰 Để có thể truy cập vào tất cả các channel của discord, các bạn vui lòng đổi biệt danh theo định dạng:\n" + \
                "```\n" + \
                "Họ tên - MSSV - Lớp \n" + \
                "``` \n" + \
                "👉 Sau đó, nhớ điền form: https://tinyurl.com/Discord-K21-FITUTE để được set role nhé. \n " 
                
            msg = msg if MESSAGE is None else MESSAGE
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(),
                                  color=discord.Color.blue())
            # embed.add_field(name="Server created at",
            #                 value=f"{guild.created_at}")
            # embed.add_field(name="Server Owner", value=f"{guild.owner}")
            # embed.add_field(name="Server Region", value=f"{guild.region}")
            # embed.add_field(name="Server ID", value=f"{guild.id}")
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.add_field(name="🌟🌟🌟", value=f"\n💥 Chào mừng {member.mention} đến với Server {guild.name} nhé! \n\n{msg}")
            embed.add_field(name="Lưu ý", value=f"Đừng quên đọc <#{CHANNEL_ID}> nhé!")
            embed.set_thumbnail(url=THUMBNAIL)

            await guild.system_channel.send(embed=embed)

            # await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
