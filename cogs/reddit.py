import aiohttp
import discord
import random2
from discord.ext import commands


class Reddit(commands.Cog):
    """
    Gets images of r/dankmemes or r/aww or r/wholesomememes
                """
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def dankmeme(self, ctx):
        """The dankest of memes"""
        pymeme = discord.Embed(title="Meme", description="**Meme Request**", color=0xe91e63)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                pymeme.set_image(url=res['data']['children'][random2.randint(0, 25)]['data']['url'])
                await ctx.send(embed=pymeme)

    @commands.command()
    async def aww(self, ctx):
        """Cute animals"""
        pymeme = discord.Embed(title="Awww", description="**CUTE DOGGO AND CAT**", color=0xe91e63)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/aww/new.json?sort=hot') as r:
                res = await r.json()
                pymeme.set_image(url=res['data']['children'][random2.randint(0, 25)]['data']['url'])
                await ctx.send(embed=pymeme)

    @commands.command(aliases=["wholesome", "wm"])
    async def Wholesome(self, ctx):
        """Wholesome memes"""
        pymeme = discord.Embed(title="wholesomememes", description="**a great command when you feel down**",
                               color=0xe91e63)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/wholesomememes/new.json?sort=hot') as r:
                res = await r.json()
                pymeme.set_image(url=res['data']['children'][random2.randint(0, 25)]['data']['url'])
                await ctx.send(embed=pymeme)


def setup(bot):
    bot.add_cog(Reddit(bot))
    print("Reddit cog loaded Successfully")
