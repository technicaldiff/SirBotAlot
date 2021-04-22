import requests
from discord.ext import commands
import discord


class Mcstatus(commands.Cog):
    """
       Completed but still in beta bugs inform to Technical_difficulty#6957
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def mcstatus(self, ctx, arg):
        serverdata = arg
        data = requests.get(f"https://eu.mc-api.net/v3/server/ping/{serverdata}").json()
        motdto = requests.get(f"https://api.mcsrvstat.us/2/{serverdata}").json()
        embed = discord.Embed(title="Server status", colour=discord.Colour.blurple())
        try:
            embed.add_field(name="Status", value=f"{motdto['online']} :green_circle:")
        except:
            embed.add_field(name="Status", value="Offline :red_circle:")
        try:
            embed.add_field(name="Players online", value=f"{data['players']['online']} / {data['players']['max']}")
        except:
            embed.add_field(name="Players online", value="Failed")
        try:
            embed.add_field(name="Latency", value=f"{data['took']} ms")
        except:
            embed.add_field(name="Latency", value="Failed")

        try:
            embed.add_field(name="Version", value=f"{data['version']['name']}")
        except:
            embed.add_field(name="Version", value="Failed")

        try:
            embed.add_field(name="Motd", value=f"{motdto['motd']['clean']}")
        except:
            embed.add_field(name="Motd", value="Failed")

        try:
            embed.add_field(name="Player Names", value=f"{motdto['players']['list']}")
        except:
            embed.add_field(name="Player Names", value="Failed")

        try:
            embed.set_thumbnail(url=f"{data['favicon']}")
        except:
            embed.set_thumbnail(value="Failed")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Mcstatus(bot))
    print("Mcstatus cog loaded Successfully")

