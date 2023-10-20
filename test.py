import re
import urllib.parse as parse
import os
import discord


URL_PREFIX = "steam://"
OPEN_STORE_PAGE = "store/"
API_URL = 'https://api.deile.net/locationRedirect'
# store.steampowered.com,help.steampowered.com,steamcommunity.com
RAGEX = "https://.+[steampowered|steamcommunity].com/"


def test(content):

    result = re.match(RAGEX, content)

  # open store page
  # ex) steam://store/990080/ ホグワーツ・レガシー
  # open profile page
  # ex ) steam://SteamIDPage/76561198030992956/ でいるちゃんのプロフィール

    if result:

        parsed_url = parse.urlparse(content)
        # ['', 'app', '990080', '_', '']
        split_path = str(parsed_url.path).split("/")
        print(split_path)

        match split_path[1]:
            case 'app':
                print(split_path[1])
            case 'profiles':
                print(split_path[1])


if __name__ == '__main__':
    test("https://steamcommunity.com/profiles/76561198030992956/")
    test("https://store.steampowered.com/app/990080/_/?l=japanese")
