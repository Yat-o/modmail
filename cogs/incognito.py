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
        roles = []
        admin =  ctx.guild.get_role(695051576552718416)
        tmod = ctx.guild.get_role(736717979609464872)
        roles.append(tmod)
        roles.append(admin)
        await member.add_roles(*roles)
        await member.edit(nick=f"TM | {member.name}")
        await ctx.send(f"Added T-Mod and Base Administrator Role to {member} and renamed them to {member.display_name}")
        await ctx.send("Creating Staff Announcement now in <#736780095855001662>")
        chan = ctx.guild.get_channel(736780095855001662)
        await chan.send(
            embed=discord.Embed(
                title="**__Staff 7 day trial__**",
                description=f"Welcome {member.mention} thanks for taking the time to apply for staff, you have passed the application. Please read <#736727981535264859> for information about your job here. Now you will have 1 week to prove that you are a good fit for this position, at the end of the week you will be either removed or promoted based on your performance. Good luck!",
                color=0xff0000
            ).set_footer(text="INCOGNITO Advertising (c) |  https://discord.gg/NP4TXsZ")
        )

    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def removestaff(self, ctx: commands.Context, member: discord.Member, *, reason = None):
        """Command for removing staff members to the Incognito Advertising Staff Team"""
        roles = []
        admin = ctx.guild.get_role(695051576552718416)
        tmod = ctx.guild.get_role(736717979609464872)
        roles.append(tmod)
        roles.append(admin)
        if reason is None:
            return await ctx.send("Please add a reason to remove this staff member.")

        if not tmod in member.roles or not admin in member.roles:
            return await ctx.send("This member is a not a staff member.")

        else:
            await member.remove_roles(*roles)
            await ctx.send(f"Removed T-Mod and Base Administrator Role from {member}")
            msg = await ctx.send(f"Attempting To DM {member} termination message.")
            try:
                await member.send(
                    embed=discord.Embed(
                        title="You were removed from the Incognito Advertising Staff Team!",
                        description=f"Reason: {reason}",
                        color=0xff0000
                    ).set_footer(text=f"Acting Supervisor: {ctx.author}")
                )
                await msg.add_reaction("\u2705")
            except (discord.Forbidden, discord.HTTPException):
                await msg.add_reaction("\u2049")


def setup(bot):
    bot.add_cog(Incognito(bot))