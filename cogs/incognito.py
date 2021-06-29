import discord

from discord.ext import commands
from core import checks
from core.models import PermissionLevel
class Incognito(commands.Cog):
    """Commands related to"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(embed_links=True)
    async def staff_intro(self, ctx, user: discord.User):
        chan = self.bot.get_channel(736780095855001662)
        await chan.send(embed=discord.Embed(
            title="**__Staff 7 day trial__**",
            description=f"Welcome {user.mention} thanks for taking the time to apply for staff, you have passed the application. Now you will have 1 week to prove that you are a good fit for this position, at the end of the week you will be either removed or promoted based on your performance. Good luck!",
            color=0xff0000
        ).set_footer(text="INCOGNITO Advertising (c) |  https://discord.gg/NP4TXsZ")
    )

def setup(bot):
    bot.add_cog(Incognito(bot))