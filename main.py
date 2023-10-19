import discord
import re
import os

global TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

URLPrefix = "steam://openurl/"
RAGEX = "https://.+steampowered.com.+[0-9]{1,8}.*/"


@client.event
async def on_ready():
    print('Login successfully.')


@client.event
async def on_message(message: discord.Message):
    content = message.content
    result = re.match(RAGEX, content)

    if result:
        convert_text = URLPrefix + content
        print('converted:', convert_text)
        if message.author.bot:
            return

        await message.channel.send(convert_text)


def main():

    TOKEN = os.environ.get('DISCORD_TOKEN')

    client.run(TOKEN)


if __name__ == '__main__':
    main()
