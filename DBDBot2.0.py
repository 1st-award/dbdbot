mport discord
import asyncio
from bs4 import BeautifulSoup
import requests
import time
from discord.ext import commands




bot = commands.Bot(command_prefix='.')
client = discord.Client()

@bot.event
async def on_ready():   
    print('Logged in as \nName: {}\n  ID: {}\n'.format(bot.user.name, bot.user.id))
    channel = bot.get_channel(349182384123674624)
    lastest_perk = 'Null'
    while(True):
    
        headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        r = requests.get('https://gall.dcinside.com/mgallery/board/view/?id=dbd&no=546029&page=1', headers = headers)
        r.encoding = 'euc-kr'
        soup = BeautifulSoup(r.text, 'html.parser')
        main = soup.find(style='overflow:hidden;')
        perk = main.find_all('p')
        today_perk = str(perk[1].text)
        day = today_perk[:10]
    
        if lastest_perk in day:
        	await channel.send('Same...')
        else:
        	lastest_perk = day
        	await channel.send('NEW!! Perk!!\n' + today_perk)
    
        await asyncio.sleep(1.0)

bot.run('NDc2MjIwMzI4MTIxNDY2ODgz.XeI4gA.4HUr2JzUVJo0W6F025sc9r-Uv9I')
