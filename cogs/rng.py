import random
from discord.ext import commands


class RNG:
    def __init__(self, bot):
        self.client = bot

    @commands.command(name='8ball',
                    description="Answers a yes/no question.",
                    brief="Spooky magic answers.",
                    aliases=['eight_ball','eightball', '8-ball'],
                    pass_context=True,
                    no_pm=True)
    async def eight_ball(self, context):
        possible_responses = [
            'It is certain',
            'As I see it, yes',
            'Reply hazy try again',
            "Don't count on it",
            'It is decidedly so',
            'Most likely',
            'Ask again later',
            'My reply is no',
            'Without a doubt',
            'Outlook good',
            'Better not tell you now',
            'My sources say no',
            'Yes definitely',
            'Yes',
            'Cannot predict now',
            'Outlook not so good',
            'You may rely on it',
            'Signs point to yes',
            'Concentrate and ask again',
            'Very doubtful'
        ]
        await self.client.say(random.choice(possible_responses) + ', ' + context.message.author.mention)

    @commands.command(name="roll",
                      description="Rolls a psuedorandom number (default 1-100). "
                                  "Add up to two numbers in your argument to change the range of the roll.",
                      brief="Psuedorandom number generator.",
                      pass_context=True,
                      no_pm=True)
    async def roll(self, context):
        vals = context.message.content.split(' ')
        if len(vals) == 1:
            await self.client.say(context.message.author.mention + ' rolled(1-100): ' + str(random.randint(1, 100)))
        elif len(vals) == 2:
            try:
                x = int(vals[1])
                await self.client.say(context.message.author.mention
                                 + ' rolled(1, '
                                 + str(x)
                                 + '): '
                                 + str(random.randint(1, x)))
            except Exception:
                await self.client.say(context.message.author.mention
                                 + ", please give me an actual number greater than 1 for single arguments.")
        else:
            try:
                x = int(vals[1])
                y = int(vals[2])
                if x <= y:
                    await self.client.say(context.message.author.mention
                                     + ' rolled('
                                     + str(x)
                                     + ', '
                                     + str(y)
                                     + '): '
                                     + str(random.randint(x, y)))
                else:
                    await self.client.say(context.message.author.mention
                                     + ", please make sure the second number is greater or equal to the first.")
            except Exception:
                await self.client.say(context.message.author.mention + ", please give me actual numbers.")


def setup(bot):
    bot.add_cog(RNG(bot))
