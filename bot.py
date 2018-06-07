from discord import Game
from discord.ext import commands

client = commands.Bot(command_prefix="!")
TOKEN_ID = "NDUxNTkxNTQ4MDYxMzUxOTM2.DfECOQ.T1270Rae2W0E8QgM2E3G8-fdeaM"
startup_extensions = ["rng", "dota"]


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Literal Garbage"))
    print("logged in as " + client.user.name + "#" + client.user.id)


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


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if "brad sucks" in message.content.lower():
        await client.send_message(message.channel, "I concur.")


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    client.run(TOKEN_ID)
