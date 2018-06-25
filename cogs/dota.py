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
        self.heroes.append("Gunman")
        self.heroes.append("Gun Guy")

    @commands.command(name='rhero',
                      description="Stop randoming a hero you're losing the draft.",
                      brief="Picks a random Dota 2 hero.",
                      aliases=['randhero','randomhero'],
                      pass_context=True)
    async def random_hero(self, context):
        num_heroes = len(self.heroes)
        hero_index = random.randint(1, num_heroes)
        if self.heroes[hero_index] is "Techies":
            await self.client.say(context.message.author.mention + ", you shouldn't pick Techies")
        else:
            await self.client.say(context.message.author.mention + ', you should pick ' + self.heroes[hero_index])


def setup(bot):
    bot.add_cog(Dota(bot))
