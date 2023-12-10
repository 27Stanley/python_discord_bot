import discord
import os

#allows code to make http requests to get data for API, returns json
import requests
import json
import pandas as pd

import datetime as dt
import random

# from DiscordBot import t.csv
from discord.ext import commands
from discord.ext.commands import bot


TOKEN = "OTYzMTU2OTk0OTU1NTc1MzE2.YlR_2g.ypyriJB87mAeUo9jCIqcyzDhRd4"
client = discord.Client()


here = os.path.dirname(os.path.abspath(__file__))
# tierlist = pd.read_csv('t.csv')


# bot = commands.Bot(command_prefix="!")
# @bot.command(pass_context = True)

# async def test(ctx):
#   await ctx.send('working', file = discord.File('ahri.jpg'))


@client.event
#on ready event, called when bot is ready to be used 
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("@hello"):
    await message.channel.send("hello")
    
  if message.content.startswith("@hi mom"):
      await message.channel.send("hi mom")

  if message.content.startswith("!martin"):
      await message.channel.send("Martin:\n 1/60 in maths test, two grand for a snog, inflated ego, severe thinking disorder" )
      file = [here + '\images\martin\martin1.jpg', here + '\images\martin\martin2.jpg', here + '\images\martin\martin3.jpg']
      ran = random.randint(0, len(file)-1)
      # await message.channel.send(here)

      with open(file[ran], 'rb') as fp:
        await message.channel.send(file=discord.File(fp, 'new_filename.jpg'))

  if message.content.startswith("!nikhil"):
      await message.channel.send("Nikhil: 5'11 indian" )
      file = [here + '\images\mikhil\mikhil1.jpg', here + '\images\mikhil\mikhil2.jpg', here + '\images\mikhil\mikhil3.jpg', here + '\images\mikhil\mikhil4.jpg', here + '\images\mikhil\mikhil5.jpg']
      ran = random.randint(0, len(file)-1)
      

      with open(file[ran], 'rb') as fp:
        await message.channel.send(file=discord.File(fp, 'new_filename.jpg'))

  if message.content.startswith("!gareth"):
      await message.channel.send("big cow")
  
  if message.content.startswith("!tim"):
      await message.channel.send("sid")

  if message.content.startswith("@time"):
      await message.channel.send(dt.datetime.now())
  
  if message.content.startswith ("!gpu"):
    filename = os.path.join(here, 'gpugraph.png')
    with open(filename, 'rb') as fp:
      await message.channel.send(file=discord.File(fp, 'new_filename.png'))



client.run(TOKEN)



  