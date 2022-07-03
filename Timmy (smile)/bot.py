import discord
from discord.ext import commands
import random
import sys
import asyncore
from asyncore import loop
import time
from discord.errors import Forbidden


client = commands.Bot(command_prefix = 't!')

@client.event
async def on_ready():
    print ('Timmy has Launched using version 1.0.0')

@client.command
async def emoji(ctx):
    await ctx.send(':purplecheckanim:')



"""
On Message. means will reply with a certain response when a user sends something, 
THIS CONTAINS:
Anti Swear
Auto Response (If someone says Yo Timmy, Timmy will respond in a certain way.)
"""
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'Yo Timmy':
        await message.channel.send('What do u want kid')

    if message.content == 'yo timmy':
        await message.channel.send('What?')
    
    if message.content == 'TIMMY':
        await message.channel.send('Chill with the caps kid')

# ANTI SWEAR


# F WORD
    if  'fuck' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'fUck' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'fUCk' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'fucc' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'fUcK' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'fook' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')


    if 'fuC' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'fUC' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'FUC' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

# D WORD

    if 'dic' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'dick' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'DIck' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'dIcK' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'dIck' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'Dick' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'dicK' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

# S WORD

    if 'shit' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'Shit' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'sHit' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'SHit' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'sHiT' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'ShIt' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'Shiit' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'ShiiT' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

# A WORD

    if 'ass' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'aSs' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'aSS' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'AsS' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'aSss' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'asSs' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

# N WORD ( DO NOT SCROLL DOWN IF U GET OFFENDED EASILY )




















    if 'nigger' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'nIgger' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'Niiger' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'niggeR' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'niggger' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'NIGGER' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'nugger' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')


    if 'Nugger' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if 'NuGger' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')


    if 'Nigg' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    if message.content == 'Nigg':
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

    




    if 'nigga' in message.content:
        await message.delete()
        await message.channel.send('**HEY!** No swearing kid, I will nuke ur house if you do')

"""
Purge Command
Purges amount of messages requested
"""

@commands.command(aliases=['clear', 'prune'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=11):
    amount = amount + 1
    if amount > 101:
        await ctx.send('Can not delete more than 100 messages at once!')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()
"""
Error msg's
Sends the error message if they dont have the required permission
"""
@purge.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")




client.run('NzU5ODk2MzExMTYzMjU2ODMz.GNpPlO.EtZT-GFe3p75DWaQyubQ6wDBFnPjAEAqPsa4OA')