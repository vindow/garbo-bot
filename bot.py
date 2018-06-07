from discord import Game
from discord.ext import commands
from os import listdir
from os.path import isfile, join

client = commands.Bot(command_prefix="!")
TOKEN_ID = "NDUxNTkxNTQ4MDYxMzUxOTM2.DfECOQ.T1270Rae2W0E8QgM2E3G8-fdeaM"
cogs_dir = "cogs"


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Literal Garbage"))
    print("logged in as " + client.user.name + "#" + client.user.id)


@client.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        client.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await client.say("{} loaded.".format(extension_name))


@client.command()
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
    client.run(TOKEN_ID)
