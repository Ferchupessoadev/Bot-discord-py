from discord.ext import commands, tasks


def setup_tasks(bot: commands.Bot):
    @bot.event
    async def on_ready():
        regards.start()

    @tasks.loop(seconds=10)
    async def regards():
        channel = bot.get_channel(1216026576211152937)
        await channel.send("regards")
