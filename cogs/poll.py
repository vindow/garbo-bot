from discord.ext import commands
import requests
import re
import json


class Poll:
    def __init__(self, bot):
        self.client = bot

    @commands.command(name='poll',
                      description="Creates a yes/no poll for a given question. Format should be !poll {question}",
                      brief="Create a basic yes/no poll.",
                      pass_context=True,
                      no_pm=True)
    async def poll(self, context):
        message = context.message.content
        # Check for valid input
        if not re.fullmatch("!poll \{\w+( +\w+)*\}", message):
            await self.client.say("Invalid input for `!poll`. See `!help poll` for help.")
        else:
            start = message.find("{") + 1
            end = message.rfind("}")
            poll_message = await self.client.say(message[start:end])
            await self.client.add_reaction(poll_message, "👍")
            await self.client.add_reaction(poll_message, "👎")

    @commands.command(name="strawpoll",
                      description="Creates a strawpoll based on the given inputs."
                                  "Format should be !strawpoll {title} [option 1] [option 2] [option 3] etc",
                      brief="Create a strawpoll.",
                      pass_context=True,
                      no_pm=True)
    async def strawpoll(self, context):
        message = context.message.content
        if not re.fullmatch("!strawpoll \{\w+( +\w+)*\}( \[\w+( +\w+)*\]){2,}", message):
            await self.client.say("Invalid input for `!strawpoll`. See `!help strawpoll` for help.")
            return
        else:
            title_start = message.find("{") + 1
            title_end = message.find("}")
            title = message[title_start:title_end]
            options_start = title_end + 3
            options_end = len(message) - 1
            options = message[options_start:options_end].split("] [")
            payload = {'title': title, 'options': options}
            headers = {'Content-type': 'application/json'}
            strawpoll_url = "https://www.strawpoll.me/api/v2/polls"
            response = requests.post(strawpoll_url, data=json.dumps(payload), headers=headers).json()
            await self.client.say("Strawpoll: https://www.strawpoll.me/" + str(response['id']))


def setup(bot):
    bot.add_cog(Poll(bot))
