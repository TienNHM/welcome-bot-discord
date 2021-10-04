import os
import datetime
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            msg = "📌 Để có thể truy cập vào tất cả các channel của discord, các bạn vui lòng đổi biệt danh theo định dạng:\n" + \
                "```\n" + \
                "Họ tên - MSSV - Lớp \n" + \
                "``` \n" + \
                "👉 Sau đó, nhớ điền form: https://tinyurl.com/Discord-K21-FITUTE để được set role nhé. \n\n " + \
                "💥 Và đặc biệt, đừng quên đọc <#887981459749609492> nà. \n\n "
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(),
                                  color=discord.Color.blue())
            # embed.add_field(name="Server created at",
            #                 value=f"{guild.created_at}")
            # embed.add_field(name="Server Owner", value=f"{guild.owner}")
            # embed.add_field(name="Server Region", value=f"{guild.region}")
            # embed.add_field(name="Server ID", value=f"{guild.id}")
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.add_field(name="Lưu ý:", value=f"💥 Chào mừng {member.mention} đến với Server {guild.name} nhé! \n\n{msg}")
            embed.set_thumbnail(
                url=f"https://img.icons8.com/color/64/000000/commercial.png")

            await guild.system_channel.send(embed=embed)

            # await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
