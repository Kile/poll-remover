import discord
from discord.ext import commands

from bot.__init__ import Bot
from bot.static.constants import LANGS

from typing import Dict

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

            # Send dm
            dm: Dict[str, str] = LANGS.get(message.guild.preferred_locale,LANGS[discord.Locale.british_english])

            embed = discord.Embed(
                title=dm["title"],
                description=dm["description"].format(user=message.author.mention, server=message.guild.name),
                color=discord.Color.red()
            )
            view = discord.ui.View()
            view.add_item(
                discord.ui.Button(
                    label=dm["button"], 
                    url=discord.utils.oauth_url(
                        self.bot.user.id, 
                        permissions=discord.Permissions(manage_messages=True),
                        scopes=["bot", "applications.commands"]
                    )
                )
            )
            try:
                await message.author.send(embed=embed, view=view)
            except discord.HTTPException: # Blocked/Closed dms
                pass

            await message.delete()

Cog = Events