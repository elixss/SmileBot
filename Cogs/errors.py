import disnake
from disnake.ext import commands
from disnake import Embed
import traceback

class Errors(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  

  @commands.Cog.listener()
  async def on_slash_command_error(self, inter, error):
      e = disnake.Embed(
          title='',
          colour=disnake.Colour.from_rgb(254, 231, 92)
      )
      if isinstance(error, commands.CommandError):
          e.add_field(name="Oh no! Smile Bot ran into an error!",
          value=f"```py\n{error}```")
          try:
              await inter.response.send_message(embed=e, ephemeral=True)
          except:
              await inter.followup.send(embed=e, ephemeral=True)
      if isinstance(error, commands.MissingPermissions):
          e.add_field(name=f'Missing permissions!', value=f'{error}')
          try:
              await inter.response.send_message(embed=e, ephemeral=True)
          except:
              await inter.followup.send(embed=e, ephemeral=True)
      if isinstance(error, commands.NotOwner):
          e.add_field(name="You are not the owner!", value=f"Only my developers can run this command.")
          try:
              await inter.response.send_message(embed=e, ephemeral=True)
          except:
              await inter.followup.send(embed=e, ephemeral=True)

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
      if isinstance(error, commands.CommandError):
        print(traceback.print_exception(type(error), error, error.__traceback__))


def setup(bot):
  bot.add_cog(Errors(bot))
