import discord
import asyncio
import random
import string
import character
import perk
import scperk
import item
import shutil
#import requests
#from bs4 import BeautifulSoup
from discord.ext import commands
from PIL import Image
 
bot = commands.Bot(command_prefix='.')
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as \nName: {}\n  ID: {}\n'.format(bot.user.name, bot.user.id))
    
    a = bot.guilds
    print('Guild list')
    for i in a:
    	path = '/app/serv/' + format(i) + '.py'
    	print('{}'.format(i))
    	shutil.copy('/app/serv/sample.py', path)
    print('='*10)
    await bot.change_presence(activity=discord.Game(name=".도움말   :D", type=0))

bot.remove_command('help')

@bot.command(pass_context=True)
async def 도움말(ctx):
    embed = discord.Embed(title="데바데 친죽 봇", description=".으로 명령을 내릴 수 있습니다.", color=0xffffff)

    embed.add_field(name=".랜덤숫자", value="**1**부터 **10**까지의 숫자중 하나를 출력합니다.", inline=False)
    embed.add_field(name=".살인마", value="살인마(DLC포함) 중 **2**명을 랜덤으로 출력합니다.", inline=False)
    embed.add_field(name=".생존자", value="생존자(DLC포함) 중 **2**명을 랜덤으로 출력합니다.", inline=False)
    embed.add_field(name=".아이템", value="아이템 모드를 ON/OFF합니다. (이벤트 아이템 포함)", inline=False)
    embed.add_field(name=".살인마 퍽", value="살인마 퍽 **4**개를 랜덤으로 출력합니다.", inline=False)
    embed.add_field(name=".생존자 퍽", value="생존자 퍽 **4**개를 랜덤으로 출력합니다.", inline=False)
    embed.add_field(name=".오퍼링 n(숫자 최대 5개)", value="오퍼링 n개만큼 랜덤으로 출력합니다.", inline=False)
    embed.add_field(name=".컨셉퍽", value="생존자 컨셉퍽을 출력합니다.", inline=False)
    embed.add_field(name=".퍽 이름   (ex: .퍽 유연함)", value="이 퍽에대한 설명을 출력합니다.", inline=False)
    embed.add_field(name=".리", value="게임을 다시하도록 경계선을 그어줍니다.", inline=False)
    embed.add_field(name=".도움말", value="이 메세지를 출력합니다.", inline=False)

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def 랜덤숫자(ctx):
        id = (ctx.message.author.mention)
        a = random.randint(1, 10)
        await ctx.send(format(id) + '님의 숫자는 **' + format(a) +'**입니다.')

@bot.command(pass_context=True)
async def 살인마(ctx):
        id = (ctx.message.author.mention)
        msg = ctx.message.content
        msg = msg.replace(".살인마 ", "")
        channel = format(ctx.message.guild)
        path = 'serv/'+channel + '.py'
        kpath = '/app/kadon/'
        size = (128, 128)
        size2 = (64, 64)
        size3 = (192, 128)
 
        
        
        if msg in '퍽':
        	out = str(random.sample(perk.killer, 4))
        	out = out.strip('[]')
        	out = out.replace("'", "", 8)
        	await ctx.send(format(id)  + "님의 살인마 퍽은 " + "**```cs\n" + str(out) + "입니다.\n```**")
        
        else:
        	out = random.sample(character.killer, 2)
        	killer = out
        	out = str(out).strip('[]')
        	out = out.replace("'", "", 4)
        	await ctx.send( format(id) + "님의 살인마는 " + "**```cs\n" + str(out)  +"입니다.\n```**")
        	
        	if '아이템 = 1' in open(path).read():
        		for i in killer:
        			
        			if i in '덫구':
        				kpath = kpath + '덫구/t'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '종구':
        				kpath = kpath + '종구/w'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '톱구':
        				kpath = kpath + '톱구/h'
        				a2 = random.sample(range(1, 19), 2)
        			elif i in '너스':
        				kpath = kpath + '너스/n'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '헤그':
        				kpath = kpath + '헤그/he'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '전구':
        				kpath = kpath + '전구/d'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '토구':
        				kpath = kpath + '토구/t'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '빵구':
        				kpath = kpath + '빵구/c'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '식구':
        				kpath = kpath + '식구/sh'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '준구':
        				kpath = kpath + '준구/ca'
        				a2 = random.sample(range(1, 19), 2)
        			elif i in '몽구':
        				kpath = kpath + '몽구/n'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '직구':
        				kpath = kpath + '직구/p'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '스피릿':
        				kpath = kpath + '스피릿/sp'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '군단':
        				kpath = kpath + '군단/l'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '역병':
        				kpath = kpath + '역병/p'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '고스트':
        				kpath = kpath + '고스트/go'
        				a2 = random.sample(range(1, 20), 2)
        			elif i in '데모고르곤':
        				kpath = kpath + '데모고르곤/de'
        				a2 = random.sample(range(1, 20), 2)
        			
        			bg = Image.open('/app/kadon/bg.jpg')
        			img_item = Image.open(kpath +".jpg")
        			img_add_on = Image.open(kpath+str(a2[0])+".jpg")
        			img_add_on2 = Image.open(kpath+str(a2[1])+".jpg")
        			img_item = img_item.convert("RGB")
        			img_add_on = img_add_on.convert("RGB")
        			bg = bg.convert("RGB")
        			
        			bg.thumbnail(size3)
        			img_item.thumbnail(size)
        			img_add_on.thumbnail(size2)
        			img_add_on2.thumbnail(size2)
        			
        			bg.paste(img_item, (0, 0))
        			bg.paste(img_add_on, (128, 0))
        			bg.paste(img_add_on2, (128, 64))
        			bg.save("/app/kadon/perk.jpg")
        			result = "/app/kadon/perk.jpg"
        			
        			await ctx.send(file=discord.File(result))
        			kpath = '/app/kadon/'

        
@bot.command(pass_context=True)
async def 생존자(ctx):
        id = (ctx.message.author.mention)
        msg = ctx.message.content
        msg = msg.replace(".생존자 ", "")
        
        if msg in "퍽":
        	out = str(random.sample(perk.surviver, 4))
        	out = out.strip('[]')
        	out = out.replace("'", "", 8)
        	await ctx.send(format(id) + "님의 생존자 퍽은 " + "**```cs\n" + str(out) +"입니다.\n```**") 
        	
        else:
        	out = str(random.sample(character.surviver, 2))
        	out = out.strip('[]')
        	out = out.replace("'", "", 4)
        	await ctx.send( format(id) + "님의 생존자는 " + "**```cs\n" + str(out)  +"입니다.\n```**") 
        
@bot.command(pass_context=True)
async def 리(ctx):
        await ctx.send("==========================================")
@bot.command(pass_context=True)
async def 퍽(ctx):
	try:
		msg = ctx.message.content
		msg = msg.replace(".퍽 ", "")
		id = (ctx.message.author.mention)
		
		msg1 = msg + ' ' + '1'
		pn = msg1.split(' ')
		
		if pn[1] in '1':
			path = '/app/killerimg/' + pn[0] + '.png'
		elif pn[2] in '1':
			path = '/app/killerimg/' + pn[0] + pn[1] + '.png'
		elif pn[3] in '1':
			path = '/app/killerimg/' + pn[0] + pn[1] + pn[2] + '.png'
		elif pn[4] in '1':
			path = '/app/killerimg/' + pn[0] + pn[1] + pn[2] + pn[3] + '.png'
			
		await ctx.send(file=discord.File(path))
	
	except FileNotFoundError:
		await ctx.send(format(id) + '\n ' +msg+'퍽을 찾을 수 없습니다.')

@bot.command(pass_context=True)
async def 살인마퍽(ctx):
        id = (ctx.message.author.mention)
             
        out = str(random.sample(perk.killer, 4))
        out = out.strip('[]')
        out = out.replace("'", "", 8)
        await ctx.send(format(id)  + "님의 살인마는 " + "**```cs\n" + str(out) +"입니다.\n```**")       
        
@bot.command(pass_context=True)
async def 생존자퍽(ctx):
        id = (ctx.message.author.mention)        
        channel = format(ctx.message.guild)
        path = '/app/serv/' + channel + '.py'
        
        out = str(random.sample(perk.surviver, 4))
        out = out.strip('[]')
        out = out.replace("'", "", 8)
        await ctx.send(format(id) + "님의 생존자는 " + "**```cs\n" + str(out) +"입니다.\n```**")
        
        if '아이템 = 1' in open(path).read():
        	path = "/app/item/"
        	size = (128, 128)
        	size2 = (64, 64)
        	size3 = (192, 128)
        	
        	a1 = random.choice(item.item)
        	temp = a1[:1]
        	
        	if temp in 't':
        		a2 = random.sample(item.ta, 2)
        	elif temp in 'l':
        		a2 = random.sample(item.la, 2)
        	elif temp in 'h':
        		a2 = random.sample(item.ha, 2)
        	elif temp in 'm':
        		a2 = random.sample(item.ma, 2)
        	elif temp in 'k':
        		a2 = random.sample(item.ka, 2)
        	elif temp in 'f':
        		a2 = "bg", "bg"
        	bg = Image.open(path+'bg.jpg')
        	img_item = Image.open(path+a1+".jpg")
        	img_add_on = Image.open(path+a2[0]+".jpg")
        	img_add_on2 = Image.open(path+a2[1]+".jpg")
        	img_item = img_item.convert("RGB")
        	img_add_on = img_add_on.convert("RGB")
        	bg = bg.convert("RGB")
        	
        	bg.thumbnail(size3)
        	img_item.thumbnail(size)
        	img_add_on.thumbnail(size2)
        	img_add_on2.thumbnail(size2)
        	
        	bg.paste(img_item, (0, 0))
        	bg.paste(img_add_on, (128, 0))
        	bg.paste(img_add_on2, (128, 64))
        	bg.save(path+"perk.jpg")
        	result = path+"perk.jpg"
		
        	await ctx.send(file=discord.File(result))

@bot.command(pass_context=True)
async def 아이템(ctx):
	channel = format(ctx.message.guild)
	path = '/app/serv/' + channel + '.py'
	output = []
	if '아이템 = 1' in open(path).read():
		  f=open(path)
		  
		  for line in f:
		  	if not '아이템 = 1' in line:
		  		output.append(line)
		  f.close()
		  f = open(path, 'w')
		  f.writelines(output)
		  f.write('아이템 = 0')
		  f.close()
		  
		  await ctx.send('아이템 모드가 꺼졌습니다.')
	elif '아이템 = 0' in open(path).read():
		f = open(path)
		
		for line in f:
			if not '아이템 = 0' in line:
				output.append(line)
		f.close()
		f = open(path, 'w')
		f.writelines(output)
		f.write('아이템 = 1')
		f.close()
		
		await ctx.send('아이템 모드가 켜졌습니다.')
		
@bot.command(pass_context=True)
async def 오퍼링(ctx):
	id = (ctx.message.author.mention)
	msg = ctx.message.content
	msg = msg.replace(".오퍼링 ", "")
	
	if msg in ".오퍼링":
		await ctx.send(file=discord.File("/app/offering/o" + str(random.randint(1, 16)) + ".jpg"))
	else:
		if int(msg) > 5:
			await ctx.send(format(id) + '오퍼링은 최대 5개 까지 가능합니다.')
		else:
			for i in range(0, int(msg)):
				await asyncio.sleep(0.3)
				await ctx.send(file=discord.File("/app/offering/o" + str(random.randint(1, 16)) + ".jpg"))
			
@bot.command(pass_context=True)
async def 컨셉퍽(ctx):
	id = (ctx.message.author.mention)
	a = random.randrange(0, 9)
	
	await ctx.send( format(id) + "님의 컨셉퍽은 " + "**```cs\n" +  scperk.scperk[a] +"입니다.\n```**")

@bot.command(pass_context=True)
async def 지연시간(ctx):
	ping = (int)(bot.latency*1000)
	await ctx.send(str(ping) + "ms")

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
