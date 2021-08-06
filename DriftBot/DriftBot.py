import discord
import logging
import youtube_dl 
import json
import os
from dotenv import load_dotenv
load_dotenv()
from discord.ext import commands, tasks





bot = commands.Bot(command_prefix="!")

#ping
@bot.command()
async def ping(ctx):
    await ctx.channel.send(f'***Pong!*** Latency: {round(bot.latency *1000)}ms')


#you_suck
@bot.command()
async def you_suck(ctx):
    await ctx.channel.send("https://tenor.com/view/cry-about-it-cry-about-it-meme-gif-20184012")

#delete
@bot.command()
@commands.has_permissions(manage_messages=True)
async def delete(ctx, amount=4):
    await ctx.channel.purge(limit=amount)


#kick
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


#ban
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.send("Banned Member!")


#join vc (not functioning)
@bot.command()
async def join(self, ctx, *, channel: discord.VoiceChannel):
 await channel.connect()
 

#reaction roles
@bot.command()
async def reactrole(ctx, emoji, role: discord.Role,*,message):

    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {
            'role_name':role.name,
            'role_id':role.id,
            'emoji':emoji,
            'message_id':msg.id
        }

        data.append(new_react_role)

    with open('reactrole.json','w') as j:
        json.dump(data,j,indent=4)

@bot.event 
async def on_raw_reaction_add(payload):

    if payload.member.bot:
        pass

    else:

        with open('reactrole.json') as react_file:

            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(bot.get_guild(payload.guild_id.roles).roles, id=x['role_id'])

                    await payload.member.add_roles(role)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(f'Connected as {bot.user.id}!')









































bot.run(os.getenv('TOKEN'))

