import discord
from discord.ext import commands
import random
from urllib import parse, request
import re


class Fun(commands.Cog):
    """
    Fun commands
    """
    def __init__(self, bot):
        self.bot = bot
        """Fun part with various commands"""
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        """8 ball is mostly right...."""
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def youtube(self, ctx, *, search):
        """Search Youtube from discord!"""
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        search_content = html_content.read().decode()
        search_results = re.findall(r'\/watch\?v=\w+', search_content)
        # print(search_results)
        await ctx.send('https://www.youtube.com' + search_results[0])

    @commands.command()
    async def rickroll(self, ctx):
        """Rickrolls...."""
        await ctx.send("https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825")

    @commands.command()
    async def hello(self, ctx):
        """Placeholder command"""
        await ctx.send("hey")


def setup(bot):
    bot.add_cog(Fun(bot))
    print("Fun cog loaded Successfully")
