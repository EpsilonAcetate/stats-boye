import discord
import sqlite3
import re
from queries import *
from administrative import *

async def run_misc_command(message, client):
	await message.add_reaction('⚙️')

	if "set_my_color" in message.content:
		color = re.search('#[0-9a-fA-F]{6}', message.clean_content).group(0)
		success = await change_user_color(message.author, color)
	else:
		success = False

	await message.remove_reaction('⚙️', message.guild.me)
	if success:
		await message.add_reaction("📈")
	else: 
		await message.add_reaction("❌")