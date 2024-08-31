import discord
from discord.ext import commands
from config import TOKEN
from events import setup_events
from commands import setup_commands
from tasks import setup_tasks

# Intents necesarios para que el bot funcione
intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot: commands.Bot = commands.Bot(command_prefix="-", intents=intents)

# Configurar eventos y comandos
setup_events(bot)
setup_commands(bot)
setup_tasks(bot)


bot.run(TOKEN)
