import discord
from discord.ext import commands

from bot.__init__ import Bot

class Misc(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @discord.app_commands.command()
    async def invite(self, interaction: discord.Interaction):
        """Get the invite link for the bot."""
        embed = discord.Embed(
            title="Invite Me!",
            description=f"Invite me to get rid of polls for anyone without manage server permissions!",
            color=discord.Color.blurple()
        )

        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label="Invite", 
                url=discord.utils.oauth_url(
                    self.bot.user.id, 
                    permissions=discord.Permissions(manage_messages=True),
                    scopes=["bot", "applications.commands"]
                )
            )
        )

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

Cog = Misc