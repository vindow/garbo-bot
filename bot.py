from discord import Game
from discord import VoiceRegion
from discord.ext import commands
import random
from config import token
#from config import test_token
from config import server_id
#from config import test_server_id

client = commands.Bot(command_prefix="!")
server_regions = [VoiceRegion.us_south, VoiceRegion.us_west, VoiceRegion.us_central, VoiceRegion.us_east]
startup_extensions = ["dota", "rng", "poll"]


@client.event
async def on_ready():
    game = Game("Literal Garbage")
    await client.change_presence(activity=game)
    print("logged in as " + client.user.name + "#" + str(client.user.id))


@client.command(name="dubtrack",
                description="It just gives you the link to the Dubtrack, idiot.",
                brief="Get the link to the Dubtrack.")
async def dubtrack(ctx):
    await ctx.send("The link to the Dubtrack is https://www.dubtrack.fm/join/room123")


@client.command(name="kys",
                description="Why do you need help for this?",
                brief="Guess I'll die. ¯\_(ツ)_/¯")
async def kys(ctx):
    if random.randint(1, 10) == 1:
        await ctx.send("Not this time. :dizzy_face: :gun: :robot: :dagger: :dizzy_face:")
    else:
        await ctx.send(":robot: :gun:")


@client.command(name="server",
                description="Toggles the server region between US West, US South, US Central, and US East."
                            " Special users only.",
                brief="Switches the server region.",
                pass_context=True,
                no_pm=True)
async def switch_server(ctx):
    server = client.get_guild(server_id)
    #server = client.get_guild(test_server_id)
    region_index = 0
    for i in range(0, len(server_regions)):
        if server.region == server_regions[i]:
            region_index = i + 1
    if region_index == len(server_regions):
        region_index = 0
    region_name = str(server_regions[region_index]).split("-")
    region_name[0] = region_name[0].upper()
    region_name[1] = region_name[1].capitalize()
    await server.edit(region=server_regions[region_index])
    await ctx.send("Changed the server region to " + " ".join(region_name) + ".")


@client.command(hidden=True)
async def load(extension_name: str, ctx):
    """Loads an extension."""
    try:
        client.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))


@client.command(hidden=True)
async def unload(extension_name: str, ctx):
    """Unloads an extension."""
    client.unload_extension(extension_name)
    await ctx.send("{} unloaded.".format(extension_name))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    client.run(token)
    #client.run(test_token)
