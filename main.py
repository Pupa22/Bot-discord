#931575013847470132 client
#OTMxNTc1MDEzODQ3NDcwMTMy.YeGa1w.LJC1lIHzYNT1dCOw69tsXWbSHRc Token

import discord

from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

from discord.ext import commands
from datetime import datetime, timedelta

message_lastseen = datetime.now()

bot = commands.Bot(command_prefix='!',help_command=None)



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
@bot.command()
async def test(ctx, * ,par):
    await ctx.channel.send("You typed : {0} ".format(par))
    
@bot.command()
async def send(ctx):
    await ctx.channel.send(str(ctx.author.name))
    
@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="Popo Bot Help", description="All available bot command", color=0xe2cc8d)
    emBed.add_field(name="help", value="Get help command", inline=False)
    emBed.add_field(name="test", value="Respond message that you've send", inline=False)
    emBed.add_field(name="send", value="Send name user", inline=False)
    emBed.add_field(name="play", value="star playing music", inline=False)
    emBed.add_field(name="stop", value="stop playing music", inline=False)
    emBed.add_field(name="pause", value="pause the music", inline=False)
    emBed.add_field(name="resume", value="continue playing the music", inline=False)
    emBed.add_field(name="hi", value="Send your name", inline=False)
    emBed.add_field(name="urname", value="Send name bot", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/rJIztIp.jpeg')
    emBed.set_footer(text='Popo bot',icon_url='https://i.imgur.com/rJIztIp.jpeg')
    await ctx.channel.send(embed=emBed)
   

@bot.event
async def on_message(message):
    global message_lastseen
    if message.content == '!hi' and datetime.now() >= message_lastseen:
        message_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send('Hello ' + str(message.author.name))
    elif message.content == '!urname' :
        await message.channel.send('My name '+ str(bot.user.name))
    elif message.content == '!logout':
        await bot.logout()
    await bot.process_commands(message)


@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_client == None:
        await ctx.channel.send("Joined")
        await channel.connect()
        voice_client = get(bot.voice_clients, guild=ctx.guild)
    
    YDL_OPTION = {'format ': 'bestaudio', 'noplaylist' : 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if not voice_client.is_playing():
        with YoutubeDL(YDL_OPTION) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice_client.play(discord.FFmpegPCMAudio(URL))   
        voice_client.is_playing()
    else : 
        await ctx.channel.send("Already playing song")
        return
        
@bot.command()
async def stop(ctx):
    voice_client = get(bot.voice_clients, guild= ctx.guild)
    if voice_client == None:
        await ctx.channel.send ("Bot is not connected to vc")
        return
    
    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("The bot is currently connected to {0} ".format(voice_client.channel))
        return
    
    voice_client.stop()
    
@bot.command()
async def pause(ctx):
    voice_client = get(bot.voice_clients, guild= ctx.guild)
    if voice_client == None:
        await ctx.channel.send ("Bot is not connected to vc")
        return
    
    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("The bot is currently connected to {0} ".format(voice_client.channel))
        return
    
    voice_client.pause()
    
@bot.command()
async def resume(ctx):
    voice_client = get(bot.voice_clients, guild= ctx.guild)
    if voice_client == None:
        await ctx.channel.send ("Bot is not connected to vc")
        return
    
    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("The bot is currently connected to {0} ".format(voice_client.channel))
        return
    
    voice_client.resume()
        
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.channel.send("Bot has disconnected!") 
        
        

bot.run('OTMxNTc1MDEzODQ3NDcwMTMy.YeGa1w.LJC1lIHzYNT1dCOw69tsXWbSHRc')