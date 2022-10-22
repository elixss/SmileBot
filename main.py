import os
import datetime
import disnake
from disnake.ext import commands
os.environ["bot_token"] = "some_token"


from Cogs.commands import avatarowner
import traceback

from disnake import Embed

bot = commands.Bot(command_prefix=commands.when_mentioned, sync_commands=True)
ownerid = [469870741165441034]
botowner = 'elixss#9999'
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(status=disnake.Status.idle,
        activity=disnake.Activity(type=disnake.ActivityType.watching, name='😄 | /smile'))
    print('😄 Smile Bot is here!')



for filename in os.listdir('./Cogs'):
    if filename.endswith('.py') and not filename.startswith('_'):
        try:
            bot.load_extension(f'Cogs.{filename[:-3]}')
        except Exception:
            raise Exception

@bot.event
async def on_message_edit(before, after):
    await bot.process_commands(after)


@bot.event
async def on_message(message):
    # Ignore messages sent by yourself
    if message.author.id == bot.user.id:
      return
    if message.author.bot:
      return

    if bot.user.mention == message.content or message.guild.me.mention == message.content:        
        embed = disnake.Embed(colour=disnake.Colour.from_rgb(254, 231, 92), timestamp=datetime.datetime.utcnow())
        embed.set_author(name=message.author, icon_url=avatarowner)
        embed.set_footer(text=f'Type / to use my commands.', icon_url=avatarowner)
        embed.set_image(url=avatarowner)
        
        await message.reply(embed=embed, mention_author=False)
        await message.add_reaction('😄')

    await bot.process_commands(message)

bot_token = os.environ['bot_token']

bot.run(bot_token)
