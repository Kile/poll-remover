import discord
from discord.ext import commands

from bot.__init__ import Bot
from bot.static.constants import LANGS

class Misc(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @discord.app_commands.command()
    async def invite(self, interaction: discord.Interaction):
        """Get the invite link for the bot."""
        text = LANGS.get(interaction.locale, LANGS[discord.Locale.british_english])

        embed = discord.Embed(
            title=text["button"],
            description=text["invite_text"],
            color=discord.Color.blurple()
        )

        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label=text["button_short"], 
                url=discord.utils.oauth_url(
                    self.bot.user.id, 
                    permissions=discord.Permissions(manage_messages=True),
                    scopes=["bot", "applications.commands"]
                )
            )
        )

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

Cog = Misc