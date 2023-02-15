import nextcord
from nextcord.ext import commands
import os
import json
from typing_extensions import *

intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='pwr ', intents=intents)

config: dict[str, str] = json.load(open('config.json', 'r'))
client._extensions: list[str] = ['utils.ping', 'codewars.katas']
client._dev: str = config['dev']
client._trusted: list[str] = config['trusted']
client._aoc_cookie: str = config['aoc_cookie']


@client.slash_command()
async def ping(interaction: nextcord.Interaction):
    await interaction.response.send_message("Pong!")


@client.event
async def on_ready():
    print(f'logged in as {client.user}')


if __name__ == '__main__':
    (client.load_extension(extension) for extension in client._extensions)

client.run(config['token'])
