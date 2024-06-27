import os

import discord
import requests
from discord.ext import commands

# Reemplaza 'TU_TOKEN_DEL_BOT' con tu token de bot
TOKEN = os.environ.get("TOKEN_DISCORD", default="TU_TOKEN_DEL_BOT")

# Intents necesarios para que el bot funcione
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="-", intents=intents)


@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msj = f"¡Hola! ¿Cómo estás? {message.author.mention}"
    if "hola" in message.content.lower():
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
    await ctx.send("Pero claro rey funciona gracias a fercho_dev")


@bot.command()
async def saludar(ctx):
    await ctx.send("Hola hijo de puta, todo bien")


@bot.command()
async def Help(ctx):
    message = (
        "> `-saludar`::Un saludo\n"
        "> `-funciona`::Funcionalidad\n"
        "> `-ping `::Responde pong\n"
        "> `-hola`::Saludo \n"
        "> `-dolar_oficial`::datos del dolar \n"
    )
    await ctx.send(message)


bot.run(TOKEN)
