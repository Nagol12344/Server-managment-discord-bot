import io, base64, json, configreader
from urllib.parse import urlparse
import discord, asyncio, re, random, subprocess
from discord.ext import commands
from discord.commands import SlashCommandGroup
from discord import option

class misc(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @discord.command()
    @option("Command", description="The command to execute")
    async def eval(self, ctx, command: str):
        if not configreader.check_access(ctx.author.id): 
            await ctx.respond("You dont have access to this server, if you beleve this is a error, please conntact the system admininstator!")
            return False
        await ctx.response.defer()

        statusinfo = subprocess.check_output(command.split()).decode('utf-8')
        embed = discord.Embed(title=f"Result", description=statusinfo)
        await ctx.followup.send(embed=embed)


def setup(bot):
    bot.add_cog(misc(bot))