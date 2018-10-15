from discord import Game
from discord import ServerRegion
from discord.ext import commands
from os import listdir
from os.path import isfile, join
from config import token
# from config import test_token
from config import server_id
# from config import test_server_id

client = commands.Bot(command_prefix="!")
cogs_dir = "cogs"
server_regions = [ServerRegion.us_south, ServerRegion.us_west, ServerRegion.us_central, ServerRegion.us_east]


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Literal Garbage"))
    print("logged in as " + client.user.name + "#" + client.user.id)


@client.command(name="dubtrack",
                description="It just gives you the link to the Dubtrack, idiot.",
                brief="Get the link to the Dubtrack.")
async def dubtrack():
    await client.say("The link to the Dubtrack is https://www.dubtrack.fm/join/room123")


@client.command(name="kys",
                description="Why do you need help for this?",
                brief="Guess I'll die. ¯\_(ツ)_/¯")
async def kys():
    await client.say(":robot: :gun:")


@client.command(name="server",
                description="Toggles the server region between US West, US South, US Central, and US East."
                            "Special users only.",
                brief="Switches the server region.",
                pass_context=True,
                no_pm=True)
async def switch_server(context):
    if context.message.author.server_permissions.manage_server:
        server = client.get_server(server_id)
        # server = client.get_server(test_server_id)
        region_index = 0;
        for i in range(0, len(server_regions)):
            if server.region == server_regions[i]:
                region_index = i + 1
        if region_index == len(server_regions):
            region_index = 0
        region_name = str(server_regions[region_index]).split("-")
        region_name[0] = region_name[0].upper()
        region_name[1] = region_name[1].capitalize()
        await client.edit_server(server, region=server_regions[region_index])
        await client.say("Changed the server region to " + " ".join(region_name) + ".")


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
    # client.run(test_token)

