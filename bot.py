from discord import Game
from discord.ext import commands
from os import listdir
from os.path import isfile, join
from config import token

client = commands.Bot(command_prefix="!")
cogs_dir = "cogs"


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Literal Garbage"))
    print("logged in as " + client.user.name + "#" + client.user.id)


@client.command(name="dubtrack",
                description="It just gives you the link to the Dubtrack, idiot.",
                brief="Get the link to the Dubtrack.")
async def dubtrack():
    await client.say("The link to the Dubtrack is https://www.dubtrack.fm/join/room123")


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if "brad sucks" in message.content.lower():
        await client.send_message(message.channel, "I concur.")
    await client.process_commands(message)


@client.command(hidden=True)
async def load(extension_name : str):
    """Loads an extension."""
    try:
        client.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await client.say("{} loaded.".format(extension_name))


@client.command(hidden=True)
async def unload(extension_name : str):
    """Unloads an extension."""
    client.unload_extension(extension_name)
    await client.say("{} unloaded.".format(extension_name))


if __name__ == "__main__":
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            client.load_extension(cogs_dir + "." + extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.')
    client.run(token)
