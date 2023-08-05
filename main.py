import discord, asyncio, configreader

activity = discord.Game(name=f"with your server settings")
Intents = discord.Intents.default()
Intents.members = True
bot = discord.Bot(activity=activity, intents=Intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[822123862837690399],description="Command for testing if the commands are working.")
async def testslashcommands(ctx):
    await ctx.respond("Hello!")

cogs = ["cog.systemctl"]

@bot.event
async def on_ready():
	print("The bot is ready!"+bot.user.name)

@bot.event
async def on_application_command_error(ctx, error):
    print(error)
    if isinstance(error, discord.ext.commands.CommandNotFound):
        print()
    elif isinstance(error, discord.ext.commands.CommandOnCooldown):
        message = f"This command is on cooldown. Try again in "+str(round(int(error.retry_after))) +" seconds.".format(error.retry_after)
        await ctx.respond(message)
        print("Cooldown")
    elif isinstance(error, discord.ext.commands.MissingPermissions):
        message = f"I'm sorry, but you do not have permission to perform this command. Please contact server administrators if you believe that this is in error."
        await ctx.respond(message)

print("Loading cogs . . .")               # This again, no actual need, but looks in the terminal
for cog in cogs:                          # Now, we iterate through the "cogs" list we created up there
		try:                                  # we put up a "try" so it doesn't break the loop when one of the cogs return any error
			bot.load_extension(cog)           # and now, we actually just load the extension
			print(cog + " was loaded.")       # and, again, for terminal's appearance sake, also it would tell you if the cogs got loaded successfully
		except Exception as e:                # now, the "except" part, we simply reference a variable "e" as the Exception(error)
			print(e) 

bot.run(configreader.get_bot_token())
