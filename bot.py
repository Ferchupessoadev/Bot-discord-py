import os

import discord
import requests
from discord.ext import commands

# Reemplaza 'TU_TOKEN_DEL_BOT' con tu token de bot
TOKEN = os.environ.get("TOKEN_DISCORD", default="TU_TOKEN_DEL_BOT")

# Intents necesarios para que el bot funcione
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="-", intents=intents)


@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "-hola" == message.content.lower():
        msj = f"¡Hola! ¿Cómo estás? {message.author.mention}"
        await message.channel.send(msj)
    if "-Help +18" == message.content:
        msj = (
            "**Comando +18**\n"
            "**handjob**:: paja\n"
            "**footjob**:: paja con los pies\n"
            "**fuck**:: cojerse a un compañero\n"
        )
        await message.channel.send(msj)
    if "-Help" == message.content:
        msj = (
            "**Comandos de Fercho Bot**\n"
            "> `-saludar`::Un saludo\n"
            "> `-funciona`::Funcionalidad\n"
            "> `-ping `::Responde pong\n"
            "> `-hola`::Saludo \n"
            "> `-dolar_oficial`::datos del dolar \n"
            "\n"
        )
        await message.channel.send(msj)
    await bot.process_commands(message)


@bot.command()
async def dolar_oficial(ctx):
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
async def funciona(ctx):
    await ctx.send("Pero claro rey funciona gracias a Ferhupesssoadev")


@bot.command()
async def fuck(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("Por favor, menciona a un usuario para usar este comando.")
        return

    if ctx.author == member:
        await ctx.send("No puedes usar este comando contigo mismo.")
        return

    msj = f"😈 {member.mention}, te quiere garchar {ctx.author.mention}"
    await ctx.send(msj)


@bot.command()
async def handjob(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("Por favor, menciona a un usuario para usar este comando.")
        return

    if ctx.author == member:
        await ctx.send("No puedes usar este comando contigo mismo.")
        return

    msj = f"😈 {ctx.author.mention} te quiere hacer una buena paja, {member.mention}"
    await ctx.send(msj)


@bot.command()
async def footjob(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("Por favor, menciona a un usuario para usar este comando.")
        return

    if ctx.author == member:
        await ctx.send("No puedes usar este comando contigo mismo.")
        return

    msj = f"😈 {ctx.author.mention} te quiere hacer una buena paja pero con los pies, {member.mention}"
    await ctx.send(msj)


@bot.command()
async def saludar(ctx):
    await ctx.send("Hola hijo de puta, todo bien")


bot.run(TOKEN)
