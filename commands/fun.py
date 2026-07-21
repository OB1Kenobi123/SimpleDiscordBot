import discord
from discord import app_commands
import random


def setup(bot):

    @bot.tree.command(name="coinflip", description="Flip a coin")
    async def coinflip(interaction: discord.Interaction):
        await interaction.response.send_message(
            random.choice(["🪙 Heads!", "🪙 Tails!"])
        )


    @bot.tree.command(name="joke", description="Tell a joke")
    async def joke(interaction: discord.Interaction):
        jokes = [
            "Why did the chicken cross the road? 🐔",
            "Why do programmers hate nature? Too many bugs 🐛",
            "My computer caught a virus... it needs a doctor 💻"
        ]
        await interaction.response.send_message(random.choice(jokes))


    @bot.tree.command(name="fact", description="Give a random fact")
    async def fact(interaction: discord.Interaction):
        facts = [
            "🐙 Octopuses have three hearts.",
            "🌳 Sharks are older than trees.",
            "🍯 Honey never expires."
        ]
        await interaction.response.send_message(random.choice(facts))