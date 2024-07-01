import discord
import requests
from discord.ext import commands


def setup_commands(bot):
    @bot.command()
    async def dolar_oficial(ctx: commands.Context):
        url = "https://dolarapi.com/v1/dolares/oficial"
        response = requests.get(url)
        data = response.json()
        mensaje = (
            f"💵 **Moneda:** {data['moneda']}\n"
            f"🏠 **Casa:** {data['casa']}\n"
            f"🔖 **Nombre:** {data['nombre']}\n"
            f"📈 **Compra:** {data['compra']}\n"
            f"📉 **Venta:** {data['venta']}\n"
            f"📅 **Fecha de Actualización:** {data['fechaActualizacion']}"
        )
        await ctx.send(mensaje)

    @bot.command()
    async def funciona(ctx: commands.Context):
        await ctx.send("Pero claro rey funciona gracias a Ferhupesssoadev")

    @bot.command()
    async def fuck(ctx: commands.Context, member: discord.Member = None):
        if member is None:
            await ctx.send("Por favor, menciona a un usuario para usar este comando.")
            return

        if ctx.author == member:
            await ctx.send("No puedes usar este comando contigo mismo.")
            return

        msj = f"😈 {member.mention}, te quiere garchar {ctx.author.mention}"
        await ctx.send(msj)

    @bot.command()
    async def handjob(ctx: commands.Context, member: discord.Member = None):
        if member is None:
            await ctx.send("Por favor, menciona a un usuario para usar este comando.")
            return

        if ctx.author == member:
            await ctx.send("No puedes usar este comando contigo mismo.")
            return

        msj = f"😈 {ctx.author.mention} te quiere hacer una buena paja, {member.mention}"
        await ctx.send(msj)

    @bot.command()
    async def footjob(ctx: commands.Context, member: discord.Member = None):
        if member is None:
            await ctx.send("Por favor, menciona a un usuario para usar este comando.")
            return

        if ctx.author == member:
            await ctx.send("No puedes usar este comando contigo mismo.")
            return

        msj = f"😈 {ctx.author.mention} te quiere hacer una buena paja pero con los pies, {member.mention}"
        await ctx.send(msj)

    @bot.command()
    async def saludar(ctx: commands.Context):
        await ctx.send("Hola hijo de puta, todo bien")
