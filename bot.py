import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from random import choice

intents = discord.Intents.default()
client = commands.Bot(command_prefix="", intents=intents)

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you..."))

@client.tree.command(name="coinflip", description="Flip a coin!")
async def coinflip(interaction: discord.Interaction):
    coin_result = choice(["heads", "tails"])
    await interaction.response.send_message(f"The coin that {interaction.user.mention} flipped landed on {coin_result}!")

@client.tree.command(name="roll", description="Roll a die!")
@app_commands.describe(sides="The number of sides on your die")
async def roll(interaction: discord.Interaction, sides: int):
    try:
        die_result = choice(range(0, sides - 1))
    except IndexError:
        await interaction.response.send_message(f"Your die must have at least 1 side!", ephemeral = True)
    await interaction.response.send_message(f"{interaction.user.mention} rolled a {die_result} on a {sides}-sided die!")

@client.tree.command(name="8ball", description="Ask the 8 ball a question!")
@app_commands.describe(question="Your question to the 8 ball")
async def eightball(interaction: discord.Interaction, question: str):
    ball_responses = [
        "It is certain.",
        "Without a doubt.",
        "You may rely on it.",
        "Yes, definitely.",
        "Ask again later.",
        "Better not tell you now.",
        "Don't count on it.",
        "Very doubtful."
    ]
    ball_response = choice(ball_responses)
    await interaction.response.send_message(f"{interaction.user.mention} asked the 8 ball: \"{question}\". It responded with: \"{ball_response}\"")

@client.tree.command(name="rps", description="Play rock paper scissors with the bot!")
@app_commands.describe(user_move="Your move")
async def eightball(interaction: discord.Interaction, user_move: str):
    if user_move not in ["rock", "paper", "scissors"]:
        await interaction.response.send_message(f"Invalid move!", ephemeral = True)
        return
    bot_move = choice(["rock", "paper", "scissors"])
    if user_move == "rock" and bot_move == "paper" or user_move == "paper" and bot_move == "scissors":
        winner = "The bot"
    elif user_move == "paper" and bot_move == "rock" or user_move == "rock" and bot_move == "scissors":
        winner = interaction.user.mention
    if user_move != bot_move:
        await interaction.response.send_message(f"{interaction.user.mention} chose {user_move} and the bot chose {bot_move}. {winner} wins!")
    else:
        await interaction.response.send_message(f"{interaction.user.mention} chose {user_move} and the bot chose {bot_move}. It's a draw!")

load_dotenv()
client.run(os.getenv("BOT_TOKEN"))