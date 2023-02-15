import nextcord
import datetime


def default_embed(title, url=None, description=None):
    embed = nextcord.Embed(title=title, url=url, description=description)
    embed.set_footer(
        text="Power Bot v1.0.0",
        icon_url="https://cdn.discordapp.com/avatars/1055129676944781443/9ffe3238dbeab228017c9ec815e1c014.png?size=1024")
    embed.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
    embed.color = nextcord.Color.green()
    return embed


def error_embed(title, description=None):
    embed = default_embed(title, description=description)
    embed.color = nextcord.Color.red()
    return embed
