import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
client = commands.Bot(command_prefix="", intents=intents)

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you..."))

@client.tree.command(name="test", description="Test the bot")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("HOLY SHIT IT FUCKING WORKS!!!")

@client.tree.command(name="test2", description="Test the bot with arguments")
@app_commands.describe(arg="Test argument")
async def test2(interaction: discord.Interaction, arg: str):
    await interaction.response.send_message(f"The argument you typed was \"{arg}\"")

load_dotenv()
client.run(os.getenv("BOT_TOKEN"))