import discord
from discord import app_commands
import random
import os
from dotenv import load_dotenv
from commands import fun
from flask import Flask
from threading import Thread

load_dotenv()

TOKEN = os.getenv("TOKEN")


class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)


client = MyClient()


@client.event
async def on_ready():
    fun.setup(client)

    await client.tree.sync()
    print(f"Logged in as {client.user}")


@client.tree.command(name="ping", description="Check if the bot is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")


@client.tree.command(name="hello", description="Say hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hello {interaction.user.mention}! 👋"
    )


@client.tree.command(name="roll", description="Roll a dice")
async def roll(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🎲 You rolled a {random.randint(1,6)}!"
    )


@client.tree.command(name="8ball", description="Ask the magic 8-ball a question")
@app_commands.describe(question="Your question")
async def eightball(interaction: discord.Interaction, question: str):
    answers = [
        "Yes ✅",
        "No ❌",
        "Maybe 🤔",
        "Definitely 🔥",
        "Ask again later ⏳"
    ]

    await interaction.response.send_message(
        f"🎱 {question}\n{random.choice(answers)}"
    )


@client.tree.command(name="choose", description="Choose between options")
@app_commands.describe(options="Separate choices with commas")
async def choose(interaction: discord.Interaction, options: str):
    choices = options.split(",")

    await interaction.response.send_message(
        f"🤔 I choose: {random.choice(choices)}"
    )


@client.tree.command(name="say", description="Make the bot say something")
@app_commands.describe(message="What should I say?")
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)


@client.tree.command(name="reverse", description="Reverse text")
@app_commands.describe(text="Text to reverse")
async def reverse(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text[::-1])

import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=10000)

Thread(target=run).start()

client.run(TOKEN)