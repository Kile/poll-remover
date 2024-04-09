import discord
from discord.ext import commands

from bot.__init__ import Bot

class Events(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is ready as {self.bot.user}")
        await self.bot.change_presence(
            activity=discord.Game(name="imagine polls 💀"),
        )

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot: return

        # Delete message if it contains a poll and the author is not a moderator (manage server perms)
        if message.guild and message.poll and not message.author.guild_permissions.manage_guild:
            await message.delete()

Cog = Events