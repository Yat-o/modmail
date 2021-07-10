import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class Incognito(commands.Cog):
    """Commands related to Incognito Advertising"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def addstaff(self, ctx: commands.Context, member: discord.Member):
        """Command for adding staff members to the Incognito Advertising Staff Team"""
        admin =  ctx.guild.get_role(695051576552718416)
        tmod = ctx.guild.get_role(736717979609464872)
        await member.add_roles(tmod, admin)
        await ctx.send(f"Added T-Mod and Admin Base Role to {member}")
        await ctx.send("Creating Staff Announcement now in <#736780095855001662>")
        chan = ctx.guild.get_channel(736780095855001662)
        await chan.send(
            embed=discord.Embed(
                title="**__Staff 7 day trial__**",
                description=f"Welcome {member.mention} thanks for taking the time to apply for staff, you have passed the application. Now you will have 1 week to prove that you are a good fit for this position, at the end of the week you will be either removed or promoted based on your performance. Good luck!",
                color=0xff0000
            ).set_footer(text="INCOGNITO Advertising (c) |  https://discord.gg/NP4TXsZ")
        )




def setup(bot):
    bot.add_cog(Incognito(bot))