#!/usr/bin/env python3

import discord
from discord import Intents

# Define your bot token
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Define your forum channel ID
FORUM_CHANNEL_ID = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Define intents
intents = Intents.default()
intents.messages = True

# Create a new client instance with intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

    # Iterate over all guilds the bot is in
    for guild in client.guilds:
        print(f'Guild: {guild.name} (ID: {guild.id})')

        # Iterate over all text channels in the guild
        for channel in guild.text_channels:
            print(f'Text Channel: {channel.name} (ID: {channel.id})')
	
    threads = guild.threads
    print(f'{threads}')
    for thread in threads:
        print(f'{thread.id}')
        print(f'{thread.category}')
        if str(thread.category) == 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' or str(thread.category) == 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' or str(thread.category) == 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX':
            await thread.send(content="Don't worry! I'm just silently waking up the forum. 🙂",
                                       delete_after=10,  	# Set delete_after parameter to 10 seconds
                                       silent=True)  		# Set silent parameter to True

# Run the bot with the token
client.run(TOKEN)
