import requests
import discord
import os
from keep_alive import keep_alive

def on_console():
  url = "https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"

  headers = {
      'x-rapidapi-host': "facts-by-api-ninjas.p.rapidapi.com",
      'x-rapidapi-key': "16b942388fmsh8bacc56acb981a1p14618djsn23feffeb4013"
      }

  response = requests.request("GET", url, headers=headers)

  print(response.text.split("\"")[3])


def get_fact():
  url = "https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"

  headers = {
      'x-rapidapi-host': "facts-by-api-ninjas.p.rapidapi.com",
      'x-rapidapi-key': "16b942388fmsh8bacc56acb981a1p14618djsn23feffeb4013"
      }

  response = requests.request("GET", url, headers=headers)

  return(response.text.split("\"")[3])

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    #Code for Mentioned Bot to send a message to channel
    if '<@!941974940251455488>' in message.content:
      await message.channel.send(get_fact())
      return

keep_alive()
client.run(os.environ['BotToken'])