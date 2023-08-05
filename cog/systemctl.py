import io, base64, json, configreader
from urllib.parse import urlparse
import discord, asyncio, re, random, subprocess
from discord.ext import commands
from discord.commands import SlashCommandGroup
from discord import option

class systemctl(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    systemctl = SlashCommandGroup("systemctl", "Run systemctl commands in discord, and have the effects on your server")

    @systemctl.command()
    @option("App", description="The name of the service that you want to see the status of")
    async def status(self, ctx, app: str):
        if not configreader.check_access(ctx.author.id): 
            await ctx.respond("You dont have access to this server, if you beleve this is a error, please conntact the system admininstator!")
            return False
        await ctx.response.defer()
        statusinfo = subprocess.check_output(['systemctl', 'status', app]).decode('utf-8')
        embed = discord.Embed(title=f"Status of {app} from systemctl", description=statusinfo)
        await ctx.followup.send(embed=embed)

    @systemctl.command()
    @option("App", description="The name of the service that you want to stop")
    async def stop(self, ctx, app: str):
        if not configreader.check_access(ctx.author.id): 
            await ctx.respond("You dont have access to this server, if you beleve this is a error, please conntact the system admininstator!")
            return False
        await ctx.response.defer()
        statusinfo = subprocess.run(['systemctl', 'stop', app])
        if statusinfo.returncode == 0: embed = discord.Embed(title=f"Service stopped!", description=f"The service {app} was successfully stopped")
        elif statusinfo.returncode == 5: embed = discord.Embed(title=f"Error", description="That service doesnt exist.")
        await ctx.followup.send(embed=embed)

def setup(bot):
    bot.add_cog(systemctl(bot))