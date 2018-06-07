import requests
import random
from discord.ext import commands


class Dota:
    def __init__(self, bot):
        self.client = bot
        heroes_url = "https://api.opendota.com/api/heroes"
        response = requests.get(heroes_url)
        hero_data = response.json()
        self.heroes = []
        for hero in hero_data:
            self.heroes.append(hero['localized_name'])

    @commands.command(name='randomhero',
                      description="Stop randoming a hero you're losing the draft.",
                      brief="Picks a random Dota 2 hero.",
                      aliases=['randhero','rhero'],
                      pass_context=True,
                      no_pm=True)
    async def random_hero(self, context):
        num_heroes = len(self.heroes)
        hero_index = random.randint(1, num_heroes)
        await self.client.say(context.message.author.mention + ', you should pick ' + self.heroes[hero_index])


def setup(bot):
    bot.add_cog(Dota(bot))
