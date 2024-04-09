import discord
from discord.ext import commands

from aiohttp import ClientSession
from discord.ext import commands
from logging import basicConfig
from sys import stdout

from . import cogs
from .static.constants import TOKEN, PREFIX

class Bot(commands.AutoShardedBot):
	def __init__(self, *args, **kwargs):
		super().__init__(chunk_guilds_at_startup=False, *args, **kwargs)

		self.session: ClientSession = None

	async def setup_hook(self):
		await self.load_extension("jishaku") # External extension for debugging
		await self.tree.sync() # Sync slash commands

	async def close(self):
		await super().close()
		await self.session.close()


async def main():
	basicConfig(level="INFO", datefmt='%I:%M:%S', format="[%(asctime)s] %(levelname)s: %(message)s", stream=stdout)

	session = ClientSession()
	intents = discord.Intents.default()
	intents.message_content = True 
	# Interestingly, you need this intent
	# To see if a message has a poll or not
	
	# Create the bot instance.
	bot = Bot(
		intents=intents,
		session=session,
		command_prefix=PREFIX,
	)
	bot.session = session

	# Setup cogs.
	for cog in cogs.all_cogs:
		print(f"Loading {cog.__name__}")
		await bot.add_cog(cog(bot))

	await bot.start(TOKEN)