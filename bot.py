import discord
from discord.ext import commands
import time
import random
import os
from dotenv import load_dotenv
load_dotenv()

# Token
token = str(os.environ['TOKEN'])

# Bot
bot = commands.Bot(command_prefix ='--')

# Commands
@bot.command(name ='teste')
async def teste(ctx):
    await ctx.send(f'Obrigado por testares o bOT {ctx.message.author.mention}')

@bot.command(name ='tino')
async def tino(ctx):
    out_please = False
    await ctx.send(f'Excelente escolha musical')
    time.sleep(2)
    file = open( "tinobOT.txt", "r")
    for line in file:
        m = await ctx.channel.history(limit = 3).flatten()
        for i in m:
            if i.content == 'para por favor':
                out_please = True
        if out_please:
            print('Acabou o pão')
            break
        line = line.strip()
        if len(line) > 0:
            await ctx.send(line)
            time.sleep(1)
    file.close()

@bot.command(name ='portugal')
async def portugal(ctx):
    hino_stop = False
    await ctx.send('https://media.giphy.com/media/dASkr4CGxMBYk/giphy.gif')
    time.sleep(2)
    stop = []
    file = open( "tuga.txt", "r")
    for line in file:
        m = await ctx.channel.history(limit = 3).flatten()
        for i in m:
            if i.content == 'para por favor':
                hino_stop = True
                stop.append(i.author)      
        line = line.strip()
        if len(line) > 0:
            await ctx.send(line)
            time.sleep(1)
    file.close()
    stop = list(set(stop))
    if hino_stop:
        for i in stop:
            await ctx.send(f'Não se para o hino {i.mention}')

@bot.command(name ='pcp')
async def pcp(ctx):
    out_please = False
    
    await ctx.send(f'Obrigado camarada')
    time.sleep(2)
    file = open( "avante.txt", "r")
    for line in file:
        m = await ctx.channel.history(limit = 3).flatten()
        for i in m:
            if i.content == 'para por favor':
                out_please = True
        if out_please:
            print('Ok camarada eu paro')
            break
        line = line.strip()
        if len(line) > 0:
            await ctx.send(line)
            time.sleep(1)
    file.close()
    

@bot.command(name = 'amen')
async def amen(ctx):
    await ctx.send('Um momento para a palavra do senhor')
    await ctx.send(file=discord.File('amen.jpeg'))



@bot.command(name = 'sporting')
async def sporting(ctx):
    sporting_lines = [
    'O MEU AMOR É O SPORTING',
    'A MINHA VIDA É O SPORTING',
    'A MINHA PAIXÃO É O SPORTING',
    'A MINHA FAMÍLIA É O SPORTING'
    ]
    sporting_gifs = [
    'https://media.giphy.com/media/RsSXeeB9Y8wiCXXWG0/giphy.gif',
    'https://media.giphy.com/media/FVPwc39ykJXrrjBo43/giphy.gif',
    'https://media.giphy.com/media/pQm0yJGDzdLEhvZWOA/giphy.gif',
    'https://media.giphy.com/media/83jr9c7LaQhgBmOIXu/giphy.gif',
    'https://media.giphy.com/media/BygxgnlLCRoil0qei7/giphy.gif',
    'https://media.giphy.com/media/H7ckUV6Jkrnz9M6w8n/giphy.gif'
    ]
    random_sporting = random.randint(0, len(sporting_lines)-1)
    random_sporting_gif = random.randint(0, len(sporting_gifs)-1)
    await ctx.send(sporting_lines[random_sporting])
    await ctx.send(sporting_gifs[random_sporting_gif])

@bot.command(name = 'comandos')
async def comandos(ctx):
    command_embed = discord.Embed(title = 'Lista de comandos', color = 0xe44a5d )
    command_embed.add_field(name = '--teste', value = 'Teste', inline = False)
    command_embed.add_field(name = '--tino', value = 'Escreve a maravilhosa letra da música "Pão com Manteiga"', inline = False)
    command_embed.add_field(name = '--pcp', value = 'AVANTE CAMARADA', inline = False)
    command_embed.add_field(name = '--portugal', value = 'HERÓIS DO MAAAAAAAAAAR', inline = False)
    command_embed.add_field(name = '--amen', value = 'Pequeno momento para a palavra do senhor', inline = False)
    command_embed.add_field(name = '--sporting', value = 'Se o teu amor é o sporting', inline = False)
    command_embed.add_field(name = '--comandos', value = 'Esta coisa aqui', inline = False)
    command_embed.add_field(name = 'mandar calar o bot', value = 'escreve "para por favor" para parar o spam', inline = False)
    await ctx.send(embed = command_embed)




# On ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    #Set custom status
    activity_list = [discord.Activity(type=discord.ActivityType.listening, name="Pão com Manteiga"),
    discord.Game(name = 'Minecraft'),
    discord.Activity(type=discord.ActivityType.watching, name = "Sporting")
    ]
    random_index = random.randint(0, len(activity_list)-1)
    await bot.change_presence(activity=activity_list[random_index])


# Message event
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
        
    if message.content == 'olá bOT':
        await message.channel.send(f'olá {message.author.mention}')


    
    await bot.process_commands(message) # Run actual commands


bot.run(token) # Run bot on server
