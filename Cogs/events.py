import disnake
from disnake.ext import commands

success_emoji = "<a:yes:890631200476114964>"
error_emoji = "<a:no:890631116254490745>"

class Events(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    channel = self.bot.get_channel(941802084708270090)
    await channel.send(
                f"{success_emoji} | Joined a guild: **{guild.name}** | ID: {guild.id} | Guild count: {len(self.bot.guilds)}", allowed_mentions=disnake.AllowedMentions.none())

  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    channel = self.bot.get_channel(941802087749152880)
    await channel.send(
                f"{error_emoji} | Left a guild: **{guild.name}** | ID: {guild.id} | Guild count: {len(self.bot.guilds)}", allowed_mentions=disnake.AllowedMentions.none())

  @commands.Cog.listener()
  async def on_thread_join(self, thread):
    try:
      await thread.join()
    except disnake.DiscordException:
      pass
  

def setup(bot):
  bot.add_cog(Events(bot))
