import os
import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
client = discord.Client(intents=intents)

load_dotenv()
client.run(os.getenv("BOT_TOKEN"))