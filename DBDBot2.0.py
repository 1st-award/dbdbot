import discord
import asyncio
from bs4 import BeautifulSoup
import requests
import time
import os
from discord.ext import commands




bot = commands.Bot(command_prefix='.')
client = discord.Client()

@bot.event
async def on_ready():   
    print('Logged in as \nName: {}\n  ID: {}\n'.format(bot.user.name, bot.user.id))
    channel = bot.get_channel(349182384123674624)
    lastest_perk = 'Null'
    while(True):
    
           r = requests.get('https://cafe.naver.com/ArticleList.nhn?search.clubid=28631521&search.menuid=93&search.boardtype=L')
           soup = BeautifulSoup(r.text, 'html.parser')
           main = soup.find(class_="article-board m-tcol-c")
           perk = main.find_all('td')
           today_perk = str(perk[1].text)
           day = str(perk[0].get_text())
           link = 'https://cafe.naver.com/deadbydaylight/' + day[1:]

           if lastest_perk in day:
               await channel.send('Same...')
           else:
                lastest_perk = day
                await channel.send('NEW!! Perk!!\n' + link)

           await asyncio.sleep(30000)

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
