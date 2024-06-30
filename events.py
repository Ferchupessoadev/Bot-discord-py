
def setup_events(bot):
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
