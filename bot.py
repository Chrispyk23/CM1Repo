import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Bot is logged in as {client.user.name} (ID: {client.user.id})")


@client.event
async def on_message(message):
    if message.author != client.user:
        user = message.author
        response = f"Hello {user.name}!"
        await message.channel.send(response)


# Replace 'YOUR_BOT_TOKEN' with the actual bot token obtained from the Discord Developer Portal
client.run('MTEyODkzNzQ4NDgwMjMzNDgzMg.GA9AsK.XW_wmZF94XNOwGdu6t7iRz64vtHxBSshDn_XNU')
