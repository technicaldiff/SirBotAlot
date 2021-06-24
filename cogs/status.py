import asyncio
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
        i = 0
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
            embed.set_thumbnail(url="https://media.minecraftforum.net/attachments/300/619/636977108000120237.png")
        the_embed = await ctx.send(embed=embed)
        while True:
            # get new data
            data = requests.get(f"https://eu.mc-api.net/v3/server/ping/{serverdata}").json()
            motdto = requests.get(f"https://api.mcsrvstat.us/2/{serverdata}").json()
            em = discord.Embed(title="Server status", colour=discord.Colour.blurple())
            try:
                em.add_field(name="Status", value=f"{motdto['online']} :green_circle:")
            except:
                em.add_field(name="Status", value="Offline :red_circle:")
            try:
                em.add_field(name="Players online", value=f"{data['players']['online']} / {data['players']['max']}")
            except:
                em.add_field(name="Players online", value="Failed")
            try:
                em.add_field(name="Latency", value=f"{data['took']} ms")
            except:
                em.add_field(name="Latency", value="Failed")

            try:
                em.add_field(name="Version", value=f"{data['version']['name']}")
            except:
                em.add_field(name="Version", value="Failed")

            try:
                em.add_field(name="Motd", value=f"{motdto['motd']['clean']}")
            except:
                em.add_field(name="Motd", value="Failed")

            try:
                em.add_field(name="Player Names", value=f"{motdto['players']['list']}")
            except:
                em.add_field(name="Player Names", value="Failed")

            try:
                em.set_thumbnail(url=f"{data['favicon']}")
            except:
                em.set_thumbnail(url="https://media.minecraftforum.net/attachments/300/619/636977108000120237.png")

            await the_embed.edit(embed=em)
            await asyncio.sleep(180)

def setup(bot):
    bot.add_cog(Mcstatus(bot))
    print("Mcstatus cog loaded Successfully")

