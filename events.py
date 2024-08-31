import discord
from discord.ext import commands


def setup_events(bot: commands.Bot):
    @bot.event
    async def on_ready():
        print(f"Conectado como {bot.user}")

    @bot.event
    async def on_member_join(member: discord.Member):
        print(f"{member} se ha unido al servidor")

    @bot.event
    async def on_member_remove(member: discord.Member):
        print(f"{member} se ha ido del servidor, hasta pronto")

    @bot.event
    async def on_member_update(before: discord.Member, after: discord.Member):
        channel = bot.get_channel(1274468614593839247)
        if before.nick != after.nick:
            await channel.send(f"'{before.nick}' ha cambiado de apodo a '{after.nick}'")
