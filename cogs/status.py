from mcstatus import MinecraftServer
from discord.ext import commands
import discord




class Mcstatus(commands.Cog):
    """
       Currently works with user input cannot ping servers with lots of players
       still under close watch
    """

    def __init__(self, bot):
        self.bot = bot\

    @commands.command(pass_context=True)
    async def mcstatus(self, ctx, arg):
        server = MinecraftServer.lookup(arg)
        status = server.status()
        em = discord.Embed(title="Minecraft Server status for {0}".format(arg),colour=discord.Colour.blurple())
        em.add_field(name="server status",value="The server has {0} players".format(status.players.online))
        latency = server.ping()
        em.add_field(name="ping",value="server replied in {0} ms".format(latency))
        usersConnected = [user['name'] for user in status.raw['players']['sample']]
        em.add_field(name="Players online", value=usersConnected)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Mcstatus(bot))
    print("Mcstatus cog loaded Successfully")
