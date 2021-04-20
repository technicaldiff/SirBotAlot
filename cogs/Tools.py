import random
import discord
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.members = True


class Tools(commands.Cog):
    """
    Useful tools
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calculate(self, ctx, operation, *nums):
        """Calculate stuff"""
        if operation not in ['+', '-', '*', '/']:
            await ctx.send('Please type a valid operation type.')
        var = f' {operation} '.join(nums)
        await ctx.send(f'{var} = {eval(var)}')

    @commands.command()
    async def info(self, ctx):
        """Gives info about the guild"""
        embed = discord.Embed(title=f"{ctx.guild.name}", description="yt another guild",
                              timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
        embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        # embed.set_thumbnail(url=f"{ctx.guild.icon}")
        embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        """Latency between discord and the bot"""
        await ctx.send('Pong!   `{0} seconds`'.format(round(self.bot.latency, 1)))

    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
            pfp = member.avatar_url

        embed = discord.Embed(colour=discord.Colour(random.randint(1, 16777215)), timestamp=ctx.message.created_at,
                              title=f"User Info - {member}")
        embed.set_thumbnail(url=pfp)
        embed.add_field(name="Name", value=member.name)
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Nickname:", value=member.display_name)
        embed.add_field(name="Status", value=member.status)
        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M  UTC"))
        embed.add_field(name="Joined Server On:", value=(member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")))

        # Fixed part
        roles = [role.mention for role in member.roles[1:]]

        if len(member.roles[1:]) < 1:
            embed.add_field(name=f"Roles:", value="None", inline=False)
            embed.add_field(name="Highest Role:", value="None")
        elif roles != None:
            embed.add_field(name=f"Roles({len(roles)}):", value=",".join(roles), inline=False)
            embed.add_field(name="Highest Role:", value=member.top_role.mention)
        # End of fix

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Tools(bot))
    print("Tools cog loaded successfully")
