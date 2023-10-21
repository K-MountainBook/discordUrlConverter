import discord
import re
import os
import urllib.parse as parse

global TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

URL_PREFIX = "steam://"
OPEN_STORE_PAGE = "store/"
OPEN_USER_PROFILE = "SteamIDPage/"
API_URL = 'https://api.deile.net/locationRedirect'
API_PARAMETER = '?steamurl='
# store.steampowered.com,help.steampowered.com,steamcommunity.com
RAGEX = "https://.+[steampowered|steamcommunity].com/"


@client.event
async def on_ready():
    print('Login successfully.')


@client.event
async def on_message(message: discord.Message):
    content = message.content
    result = re.match(RAGEX, content)

    # open store page
    # ex) steam://advertise/990080/ ホグワーツ・レガシー
    # open profile page
    # ex ) steam://SteamIDPage/76561198030992956/ でいるちゃんのプロフィール

    if result:
        # URLがsteampowered or steamcommunityだった場合の処理
        if message.author.bot:
            # メッセージのauthorがbotだった場合は反応しない
            return

        parsed_url = parse.urlparse(content)
        # ['', 'app', '990080', '_', '']
        split_path = str(parsed_url.path).split("/")

        # URLの作成を始める
        returl_url = API_URL + API_PARAMETER + URL_PREFIX

        match split_path[1]:
            case 'app':
                returl_url = returl_url + OPEN_STORE_PAGE + split_path[2]
            case 'profiles':
                returl_url.join(OPEN_USER_PROFILE).join(split_path[2])

        print(returl_url)

        await message.channel.send(returl_url)


def main():

    TOKEN = os.environ.get('DISCORD_TOKEN')

    client.run(TOKEN)


if __name__ == '__main__':
    main()
