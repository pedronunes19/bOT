import discord
from discord.ext import commands
import time
import random


# google translator API
import googletrans 
translator = googletrans.Translator()

# Token
#from dotenv import load_dotenv       #uncomment if heroku hours run out
#load_dotenv('.env')
import os
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
    await ctx.reply(f'Excelente escolha musical')
    time.sleep(2)
    file = open( "tino.txt", "r")
    for line in file:
        m = await ctx.channel.history(limit = 3).flatten()  # it does come with bugs but it's the best possible for now
        m_out = ctx  # temporary assignment
        for i in m:
            if i.content == 'para por favor':
                out_please = True
                m_out = i
        if out_please:
            await m_out.reply('Acabou o pão')
            break
        line = line.strip()
        if len(line) > 0:
            await ctx.send(line)
            time.sleep(1)
    file.close()


@bot.command(name ='leopoldina')
async def tino(ctx):
    out_please = False
    #await ctx.reply(f'Excelente escolha musical')  ran out of ideas
    #time.sleep(2)
    file = open( "leopoldina.txt", "r")
    for line in file:
        m = await ctx.channel.history(limit = 3).flatten()  # it does come with bugs but it's the best possible for now
        m_out = ctx  # temporary assignment
        for i in m:
            if i.content == 'para por favor':
                out_please = True
                m_out = i
        if out_please:
            await m_out.reply(':(')  # also ran out of ideas but at least is something
            break
        line = line.strip()
        if len(line) > 0:
            await ctx.send(line)
            time.sleep(1)
    file.close()


@bot.command(name ='portugal')
async def portugal(ctx):
    await ctx.send('https://media.giphy.com/media/dASkr4CGxMBYk/giphy.gif')
    time.sleep(2)
    file = open( "portugal.txt", "r")
    out_please = False
    for line in file:
        m = await ctx.channel.history(limit = 3).flatten()  # it does come with bugs but it's the best possible for now
        m_out = ctx  # temporary assignment
        for i in m:
            if i.content == 'para por favor':
                out_please = True
                m_out = i
        if out_please:
            await m_out.reply('*barulhos de patriota triste*')
            break
        line = line.strip()
        if len(line) > 0:
            await ctx.send(line)
            time.sleep(1)
    file.close()
    

@bot.command(name ='pcp')
async def pcp(ctx):
    out_please = False
    
    await ctx.reply(f'Obrigado camarada')
    time.sleep(2)
    file = open( "avante.txt", "r")
    for line in file:
        m = await ctx.channel.history(limit = 3).flatten()  # it does come with bugs but it's the best possible for now
        m_out = ctx  # temporary assignment
        for i in m:
            if i.content == 'para por favor':
                out_please = True
                m_out = i
        if out_please:
            await m_out.reply('foi um prazer camarada')
            break
        line = line.strip()
        if len(line) > 0:
            await ctx.send(line)
            time.sleep(1)
    file.close()


@bot.command(name ='socrates')
async def socrates(ctx):
    out_please = False
    file = open( "sócrates.txt", "r")
    for line in file:
        m = await ctx.channel.history(limit = 3).flatten()  # it does come with bugs but it's the best possible for now
        m_out = ctx  # temporary assignment
        for i in m:
            if i.content == 'para por favor':
                out_please = True
                m_out = i
        if out_please:
            await m_out.reply('foi um prazer amigo')
            break
        line = line.strip()
        if len(line) > 0:
            await ctx.send(line)
            time.sleep(1)
    file.close()


# useless since the picture isn't on github    
"""  
@bot.command(name = 'amen')
async def amen(ctx):
    await ctx.send('Um momento para a palavra do senhor')
    await ctx.send(file=discord.File('amen.jpg'))
"""


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



@bot.command(name = 'translate')
async def translate(ctx, lang= None ,*words):
    validLangs0 = googletrans.LANGUAGES.keys()
    validLangs1 = googletrans.LANGUAGES.values()
    if (lang == None or len(words) == 0):
        await ctx.reply('Falta alguma coisa')
    else:
        if (lang not in validLangs0 and lang not in validLangs1):
            await ctx.reply('Essa língua não existe')
        else:
            await ctx.reply(translator.translate(' '.join(words), dest = lang).text)


@bot.command(name = 'repo')
async def repo(ctx):
    await ctx.reply('https://github.com/pedronunes19/bOT')

@bot.command(name = 'java')
async def java(ctx):
    if (ctx.channel.id != 879426936756113408):
        await ctx.message.delete()
        return
    lang = ["Assembly", "C#", "C++", "C", "Cobol","Go", "Haskell", "HTML", "Java", "Javascript", "Kotlin", "Lisp", "Lua", "PHP", "Perl", "Prolog", "Python", "R", "Ruby", "Rust", "Scala", "Shell", "Smalltalk", "SQL", "Swift", "Pascal", "Typescript", "WebAssembly"]
    
    l1 = random.randint(0, len(lang)-1)
    while(True):
        l2 = random.randint(0, len(lang)-1)
        if (l1 != l2):
            break
    while(True):
        l3 = random.randint(0, len(lang)-1)
        if (l1 != l3 and l2!=l3):
            break
    final = f'"{lang[l1]} é {lang[l2]} só que {lang[l3]}"'
    if (l1 == "Java" and l2 == "Python" and l3 == "C++"):
        final.upper()
    await ctx.send(final)
   


@bot.command(name = 'comandos')
async def comandos(ctx):
    command_embed = discord.Embed(title = 'Lista de comandos', color = 0xe44a5d )
    command_embed.add_field(name = '--teste', value = 'Teste', inline = False)
    command_embed.add_field(name = '--tino', value = 'Escreve a maravilhosa letra da música "Pão com Manteiga"', inline = False)
    command_embed.add_field(name = '--leopoldina', value = 'são 4 da manhã não sei o que escrever', inline = False)
    command_embed.add_field(name = '--pcp', value = 'AVANTE CAMARADA', inline = False)
    command_embed.add_field(name = '--portugal', value = 'Hino de Portugal', inline = False)
    command_embed.add_field(name = '--socrates', value = 'uma homenagem ao nosso grande amigo', inline = False)
    #command_embed.add_field(name = '--amen', value = 'Pequeno momento para a palavra do senhor', inline = False)
    command_embed.add_field(name = '--sporting', value = 'Se o teu amor é o Sporting', inline = False)
    command_embed.add_field(name = '--translate', value = '"--translate <lang> <text>" para traduzir texto', inline = False)
    command_embed.add_field(name = '--repo', value = 'Link para o repositório do github', inline = False)
    command_embed.add_field(name = '--comandos', value = 'Esta coisa aqui', inline = False)
    command_embed.add_field(name = 'mandar calar o bot', value = 'escreve "para por favor" para parar o spam', inline = False)
    await ctx.send(embed = command_embed)



@bot.command(name = 'voto')
async def voto(ctx, *stuff):
    m = stuff
    msg = ctx.message
    if '|' not in m:
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
    else:
        poll_count = 1
        poll_react = {1: '🇦', 2: '🇧', 3: '🇨', 4: '🇩', 5: '🇪', 6: '🇫', 7: '🇬', 8: '🇭', 9: '🇮', 10: '🇯'}
        for poll_sep in m:
            if poll_sep == '|':
                poll_count = poll_count + 1
        for poll_v in range(1, poll_count + 1):
            await msg.add_reaction(poll_react[poll_v])


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
    """" In case you don't like Pedro Piadas (olá Cisco)
    if message.author == await bot.fetch_user(808416499664158790):
        await message.channel.send("Não gosto do Pedro Piadas")
        await message.delete()
    """
    if message.content == 'olá bOT':
        await message.channel.send(f'olá {message.author.mention}')


    
    await bot.process_commands(message) # Run actual commands


bot.run(token) # Run bot on server
