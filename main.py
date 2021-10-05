import os
import datetime
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MESSAGE = os.getenv('MESSAGE')
THUMBNAIL = os.getenv('THUMBNAIL')
RULES = os.getenv('RULES')
RULE_ICON = os.getenv('RULE_ICON')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        
        #### WELCOME
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(),
                                color=discord.Color.blue())
        embed.add_field(name="🌟🌟🌟", value=f"\n💥 Chào mừng {member.mention} đến với Server {member.guild.name} nhé! \n\n{MESSAGE}")
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
