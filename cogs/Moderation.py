import discord
from discord.ext import commands


class Moderation(commands.Cog):
    """
    Moderation part of the bot
    """
    def __init__(self, bot):
        self.author = None
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.User = None, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself")
            return
        if reason is None:
            reason = "For being a jerk!"
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member} is banned! by {ctx.author.name}")


def setup(bot):
    bot.add_cog(Moderation(bot))
    print("Mod cog loaded Successfully")
