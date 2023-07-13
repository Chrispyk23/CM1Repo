import discord
import langchain

# Initialize the Discord client
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Greet the user with a joke about their name
    joke = f"Why did the {message.author.name} cross the road? To tell you that"
    await message.channel.send(joke)

    # Process the user's question using LangChain
    question = message.content
    answer = await langchain.chain(question)
    await message.channel.send(answer)
# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token
client.run("MTEyODYzNzc1MTg0NDE2MzU5Ng.GR0c_E.bMRpRVRpuj0I28QDOt4TfEsntQx66UUn0FTaYA")
