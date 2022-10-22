import disnake
from disnake import Embed
from disnake.ext import commands
botowner = 'elixss#9999'

import datetime

avatarowner = 'https://cdn.discordapp.com/attachments/805865325215088711/839923940427300904/netclipart.com-100-emoji-clipart-2753759.png'
avatarowner2 = 'https://cdn.discordapp.com/attachments/852514932351959061/941840331324932226/ezgif.com-gif-maker_1.png'
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('commands loaded!')

    #Commands start from here

    @commands.slash_command(name="smile")
    async def smile(self, inter):
      """Gives you a smile"""
      embed = Embed(colour=disnake.Colour.from_rgb(254, 231, 92), timestamp=datetime.datetime.utcnow())
      embed.set_author(name=inter.author, icon_url=avatarowner)
      embed.set_footer(text=f'Smile Bot', icon_url=avatarowner)
      embed.set_image(url=avatarowner)
      await inter.response.send_message(embed=embed)
    
    @commands.slash_command(name="sad")
    async def frowning(self, inter):
      """Gives you a sad face."""
      embed = Embed(colour=disnake.Colour.from_rgb(254, 231, 92), timestamp=datetime.datetime.utcnow())
      embed.set_author(name=inter.author, icon_url=avatarowner2)
      embed.set_footer(text=f'Sad Smile Bot', icon_url=avatarowner2)
      embed.set_image(url=avatarowner2)
      await inter.response.send_message(embed=embed)

    @commands.slash_command(name="help")
    async def help(self, inter):
        """Smile Bot help command."""
        embed = Embed(title="Smile bot help :smile:", description="Get started with Smile Bot!", colour=disnake.Colour.yellow())
        embed.add_field(name="Commands that I have.",
        value=f"`/smile` - Gives you a big smile :smile:\n`/invite` - Invite me to your server!\n`/guilds` - Shows the amount of guilds I'm in\n{self.bot.user.mention} - Gives you a big smile :smile:\n`/sad` - Gives you a sad face.\n`/support` - Join the Smile Bot support server.", inline=False)
        await inter.response.send_message(embed=embed)

    @commands.slash_command(name="invite")
    async def invite(self, inter):
        """Invite Smile Bot to your server."""
        view = disnake.ui.View()
        view.add_item(disnake.ui.Button(label="Invite me!", emoji="😄", style=disnake.ButtonStyle.url, url="https://discord.com/api/oauth2/authorize?client_id=843299383134650389&permissions=2147601472&scope=applications.commands%20bot"))
        await inter.response.send_message("Click to invite me! :smile:", view=view)

    @commands.slash_command(name="support")
    async def support(self, inter):
      """Join the Smile Bot server."""
      view = disnake.ui.View()
      view.add_item(disnake.ui.Button(label="Join the support server", emoji="😄", style=disnake.ButtonStyle.url, url="https://discord.gg/JxTpnqx5ZN"))
      await inter.response.send_message("Click to join the Smile Bot support server.", view=view)
  
    @commands.slash_command(name="guilds")
    async def guilds(self, inter):
      """Shows the amount of servers I'm in."""
      await inter.response.send_message(f"I am in {len(self.bot.guilds)} servers.")

#register Cog
def setup(bot):
    bot.add_cog(Commands(bot))
