import contextlib
import datetime
import io
import json
import os
import textwrap
import time
import disnake
# libraries for the exec command
import requests
from disnake import OptionType
from disnake.ext import commands
import disnake_paginator
colour = disnake.Colour.yellow()
import rich
import aiohttp
from aiohttp import ClientSession

previous_button_text = "<"
next_button_text = ">"
first_button_text = "<<"
last_button_text = ">>"
not_command_owner_text = "You are not the sender of that command!"





def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content

class Execute(commands.Cog, name='Execute'):
    """Execute command."""

    def __init__(self, bot):

        self.bot = bot
        pass
    
    async def patch(self, title, description):
      channel = self.bot.get_channel(941802029758681148)
      embed = disnake.Embed(title=title, description=description, colour=colour)
      message = await channel.send(embed=embed)
      await message.publish()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Exec Cog has been loaded.')

    # post announcements

    @commands.command(name="exec", aliases=["execute"])
    @commands.is_owner()
    async def _eval(self, ctx, *, code):
        """Run code."""
        code = clean_code(code)
        local_variables = {
            "disnake": disnake,
            "commands": commands,
            "bot": self.bot,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message,
            "requests": requests,
            "patch": self.patch,
            "os": os,
            "time": time,
            "json": json,
            "rich": rich,
            "aiohttp": aiohttp,
            "ClientSession": ClientSession
        }

        stdout = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
                )

                await local_variables["func"]()
                result = f"{stdout.getvalue()}\n".replace(self.bot.http.token, "<TOKEN>")
                await ctx.message.add_reaction("<a:yes:890631200476114964>")
        except Exception as e:
            result = "`" + "".join(f"{e}").capitalize() + "`".replace(self.bot.http.token, "<TOKEN>")
            await ctx.message.add_reaction("<a:no:890631116254490745>")

        segments = [result[i: i + 1000] for i in range(0, len(result), 1000)]

        if "#plain" in code:
            pager = disnake_paginator.ButtonPaginator(prefix="", suffix="", color=colour, title="Eval output", segments=segments)
        else:
            pager = disnake_paginator.ButtonPaginator(prefix="```py\n", suffix="```", color=colour, title="Eval output", segments=segments)

        try:
            if len(result) <= 2000:
                if "#python" in code:
                    await ctx.send("```py\n" + result.replace(self.bot.http.token, "<TOKEN>") + "```")
                else:
                    await ctx.send(result.replace(self.bot.http.token, "<TOKEN>"))
            else:
                await pager.start(disnake_paginator.wrappers.MessageInteractionWraper(ctx))

        except Exception as e:
            if "400" in e:
                pass
            else:
                await ctx.send(e)


def setup(bot):
    bot.add_cog(Execute(bot))
