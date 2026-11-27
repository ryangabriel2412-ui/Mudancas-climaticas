#Código base
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carregando variáveis de ambiente
load_dotenv()

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# Evento de inicialização
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}!")
    print("Bot ambiental iniciado com sucesso!")

# Primeiro comando
@bot.command()
async def ola(ctx):
    await ctx.send(
        "Olá! 🌱 Sou um bot de conscientização ambiental!"
    )

# Inicializando o bot
bot.run("DISCORD_TOKEN")
