from discord.ext import commands
import discord


def setup_commands(bot):
    @bot.command()
    async def ping(ctx: commands.Context):
        await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

    @bot.command()
    async def testembed(ctx: discord.ext.commands.Context):
        embed = discord.Embed(
            title="Título del Embed",
            description="Descripción del Embed",
            color=discord.Color.blue()
        )

        embed.add_field(
            name="Campo 1", value=f"tengo miedo {ctx.author.mention}", inline=False)
        embed.add_field(
            name="Campo 2", value="tengo miedo 2", inline=False)

        embed.set_image(
            url="https://avatars.githubusercontent.com/u/107710139?v=4")
        embed.set_footer(text="probando embeds")

        await ctx.send(embed=embed)
