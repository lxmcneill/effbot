import os, time
import discord
import asyncio
from discord.ext import commands
from random import choice as rndchoice
from datetime import datetime

class LevelsCog():
    """docstring for LevelsCog"""
    def __init__(self, bot):
        
        self.bot = bot
        self.helpers = self.bot.cogs['Helpers']

    # @commands.group(pass_context=True, name="curation")
    # async def curation(self, ctx):
    #     pass

    # @commands.command(pass_context=True, name="quote")
    # @is_curator_or_higher()
    # async def quote(self, ctx, channel: str, message_id: str):
    #     m = ctx.message
    #     g = await self.helpers.get_record('server', m.guild.id)
    #     q = g['config'].chan_quotes
    #     if not q:
    #         await ctx.send('Oops, ask an admin to set up a quotes channel')
    #         return
    #     result = await self.helpers.get_obj(m.guild, 'channel', 'name', channel)
    #     if result and message_id.isdigit():
    #         c = self.bot.get_channel(result)
    #         message = await c.get_message(message_id)
    #         if message:
    #             a = message.author
    #             embed = await self.helpers.build_embed(message.content, a.color)
    #             embed.set_author(name=f'{a.name}#{a.discriminator}', icon_url=a.avatar_url_as(format='jpeg'))
    #             embed.add_field(name="In", value=f'<#{c.id}>')
    #             embed.add_field(name="Author", value=f'<@{a.id}>')
    #             await self.bot.get_channel(q).send(embed=embed)
    #             await ctx.send('Quote added successfully!')
    #         else:
    #             await ctx.send('Did not find that message, sorry!')
    #     else:
    #         await ctx.send('Check you supplied a valid channel name+message id')

    # async def curate_channels(self, message):
    #     if hasattr(message, 'guild'):
    #         m = message
    #         c, guild, a = m.channel, m.guild, m.author
    #         g = await self.helpers.get_record('server', guild.id)
    #         if g and c.id in g['config'].chan_curated:
    #             if not m.embeds and not m.attachments:
    #                 await m.delete()
    #                 await self.bot.get_user(a.id).send(
    #                     (f'Hey {a.name}, <#{c.id}> is a curated channel,'
    #                       ' meaning you can only send links or pictures.')
    #                 )

    async def add_xp(self, message):
        m = message
        if hasattr(m, 'guild') and len(message.content) >= 10:
            u = await self.helpers.get_record('user', m.author.id)
            c = u['config']
            now = datetime.utcnow().timestamp()
            if not c.last_xp or now - c.last_xp >= 10:
                c.last_xp = now
                c.xp += 1


    # async def quote_react(self, reaction, user):
    #     m = reaction.message
    #     if hasattr(m, 'guild') and reaction.emoji == "⭐":
    #         g = await self.helpers.get_record('server', m.guild.id)
    #         u = user
    #         q = g['config'].chan_quotes
    #         u_roles = [a.id for a in u.roles]
    #         is_admin = g['config'].role_admin in u_roles
    #         is_mod = g['config'].role_moderator in u_roles
    #         is_cur = g['config'].role_curator in u_roles
    #         if is_admin or is_mod or is_curator:
    #             a = m.author
    #             c = m.channel
    #             e = await self.helpers.build_embed(m.content, a.color)
    #             e.set_author(name=f'{a.name}#{a.discriminator}', icon_url=a.avatar_url_as(format='jpeg'))
    #             e.add_field(name="In", value=f'<#{c.id}>')
    #             e.add_field(name="Author", value=f'<@{a.id}>')
    #             await self.bot.get_channel(q).send(embed=e)

def setup(bot):
    cog = LevelsCog(bot)
    bot.add_listener(cog.add_xp, "on_message")

# def setup(bot):
#     cog = LevelsCog(bot)
#     bot.add_listener(cog.curate_channels, "on_message")
#     bot.add_listener(cog.quote_react, "on_reaction_add")
#     bot.add_cog(cog)