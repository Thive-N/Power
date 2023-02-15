import requests
from nextcord.ext import commands
import nextcord
import datetime
from lib.embed import default_embed

# basic command to get info about a user on codewars
# just a test for viability


class Katas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('cog loaded [katas]')

    @commands.command()
    async def katas(self, ctx):
        m = ctx.message.content.split(" ")
        if len(m) <= 2:
            await ctx.send("Please provide a username")
            return

        r = requests.get(f'https://www.codewars.com/api/v1/users/{m[2]}')

        if r.status_code != 200:
            await ctx.send("User not found")
            return

        r = r.json()
        embed = default_embed(r['username'])

        embed.add_field(
            name="honor", value=r.get('honor'), inline=False)
        embed.add_field(name="clan", value=r.get(
            "clan", "Not in a clan"), inline=False)
        embed.add_field(name="rank", value=r.get('ranks').get(
            'overall').get('name'), inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Katas(bot))
