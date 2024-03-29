import discord
from discord.ext import commands
from datetime import datetime, timedelta
from discord_components import *
import asyncio


class colc(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command()
  async def help(self,ctx):
    kk=discord.Embed(title= 'Help page/Click me for updates <:rdannythinking:759935024123871283> ' \
        ,url='https://discord.gg/5HktqCkYHY ' ,description="Bot prefix = [`,`] \n \
        \n `,invite` invite my bot to your server.\n \n `,fun` for games.\n \n `,gen` general commands.\n\
        \n `,math` for math cmds. \n\
        \n `,mod` for moderation cmds.", color=0x00d6e6,timestamp=ctx.message.created_at)
    #embed.set_footer(name=f"Requested by {ctx.author.display_name}!", icon_url=ctx.author.avatar_url)
    em2= self.client.get_emoji(865978943055462440)
    server='https://discord.gg/5HktqCkYHY'
    components = [
            Button(label = "Support Server", custom_id = "server", style = 5,url=f"{server}",emoji=em2)
         ]
      
   
    await ctx.send(embed=kk, components=components)
    interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id == "server")
    await interaction.send(components)
   



  @commands.Cog.listener()
  async def on_message(self, message):
    if message.mentions:
        if message.mentions[0].id == self.client.user.id:
            embed=discord.Embed(title= 'Help page/Click me for updates <:rdannythinking:759935024123871283> ' ,url='https://discord.gg/VnWBqX3Pjs ' ,description="Bot prefix = [`,`] \n \n `,invite` invite my bot to your server.\n \n `,fun` for games.\n \n `,gen` general commands.\n \n `,math` for math cmds. \n \n `,mod` for moderation cmds.", color=0x00d6e6)
            await message.reply(embed=embed)


  @commands.command(aliases=['inv'])
  async def invite(self,ctx):
    link='https://discord.com/oauth2/authorize?client_id=841300946973622303&permissions=0&scope=bot%20applications.commands'
    support_server='https://discord.gg/5HktqCkYHY'
    invite=discord.Embed(description="Made by `akhil.daSimpツ#0002` feel free to dm me! https://discord.com/users/476120200153137154 ", color=0x00ff7b)
    em1= self.client.get_emoji(891101245769658389)
    em2= self.client.get_emoji(865978943055462440)
    components = [[
            Button(label = "Invite Me!", custom_id = "invite", style = 5, url=f"{link}",emoji=em1),
            Button(label = "Support Server", custom_id = "server", style = 5,url=f"{support_server}",emoji=em2)
         ]]
      

    await ctx.send(embed=invite, components=components)
    interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id == "invite")
    interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id == "server")
    await interaction.send(components)

    


  @commands.group()
  async def fun(self,ctx):
    if ctx.invoked_subcommand is None:
      embed=discord.Embed(name=ctx.author.display_name,title=' :video_game: type `,fun + cmd` to learn more about a cmd ex `,fun ttt`', description="```yaml\n\
 > `,ttt` how to play tictactoe: \n\
           \n > `,8ball` 8ball cmd: \n\
           \n > `,rnum` random number generator: \n\
           \n > `,rolldice` roll dice cmd: \n\
           \n > `,memes` Memessssss: \n\
           \n > `,yjokes` yo mama jokes: \n\
           \n > `,googleit` search up stuff on google and get results: \n\
           \n > `,youtube` search up stuff on youtube and get results: \n\
           \n > `,insta` search up stuff on instagram and get results: \n\
           \n > `,urban` search up stuff on the urban dictonary and get results: ```", color=0x00ff33)
      await ctx.reply(embed=embed)

  @fun.command() 
  async def rnum(self, ctx):
    embed=discord.Embed(description="`,rnum` to get a random number from 1-101",color=0x00ff33)
    await ctx.send(embed=embed)


  @fun.command()
  async def yjokes(self,ctx):
    embed=discord.Embed(description="`,ymjokes` then your mom will get roasted!",color=0x00ff33)
    await ctx.reply(embed=embed)


  @fun.command()
  async def rolldice(self,ctx):
    embed=discord.Embed(description="`,rdice` then your dice is rolled!",color=0x00ff33)
    await ctx.reply(embed=embed)


  @fun.command()
  async def memes(self,ctx):
    embed=discord.Embed(description="`,meme`for memes!",color=0x00ff33)
    await ctx.reply(embed=embed)


  @fun.command()
  async def memez(self,ctx):
    embed=discord.Embed(description="`,ogmemes` all the og memes!",color=0x00ff33)
    await ctx.reply(embed=embed)


  @fun.command()
  async def googleit(self,ctx):
    embed=discord.Embed(description="`,google` type what you wanna search",color=0x00ff33)
    await ctx.reply(embed=embed)


  @fun.command()
  async def youtube(self,ctx):
    embed=discord.Embed(description="`,yt` type what you wanna search",color=0x00ff33)
    await ctx.reply(embed=embed)


  @fun.command()
  async def insta(self,ctx):
    embed=discord.Embed(description="`,ig` what you wanna search",color=0x00ff33)
    await ctx.reply(embed=embed)
    

  @fun.command()
  async def ttt(self, ctx):
    embed=discord.Embed(title='tictactoe!', description="`,ttt`= tictactoe" , color=0x00ff33)
    embed.add_field(name="`,pe` Places an X or O in square, 1 starts at top left to 9 at bottom right ", value="The board goes \n 1 2 3 \n 4 5 6 \n 7 8 9 ex `,pe #`")
    await ctx.reply(embed=embed)


  @fun.command(aliases=['8ball'])
  async def fun_8ball(self,ctx):
    embed=discord.Embed(title='8ball cmd! :8ball: ', description="`,8ball` + your question" , color=0x00ff33)
    embed.add_field(name="`,8ball your question here?`", value="done!")
    await ctx.reply(embed=embed)



##################################################################################################################



  @commands.group()
  async def gen(self,ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(name=ctx.author.display_name,title=" `,gen + cmd` to learn more about a cmd ex `,gen poll` " , description="```yaml\n\ \
             \n > `,botinfo` Check bots stats: \n\
             \n > `,uptime` to find out bots uptime/ how long its running: \n\
             \n > `,whois` to get info abt users join date etc: \n\
             \n > `,pfp` how to get a users pfp: \n\
             \n > `serverinfo` how to get server info: \n\
             \n > `,poll` how to make a poll: \n\
             \n > `,embed` for how to create a embed: \n ``` ",color=0xbb00ff)
        await ctx.reply(embed=embed)

  @gen.command()
  async def botinfo(self,ctx):
    embed=discord.Embed(description="`,botinfo` now you can see bot stats.",color=0xbb00ff)
    await ctx.reply(embed=embed)

  @gen.command()
  async def user(self,ctx):
    embed=discord.Embed(description="`whois @user` to get a users info.",color=0xbb00ff)
    await ctx.reply(embed=embed)


  @gen.command()
  async def avatar(self,ctx):
    embed=discord.Embed(description="`,pfp @user` then your set!",color=0xbb00ff)
    await ctx.reply(embed=embed)


  @gen.command()
  async def serverinfo(self,ctx):
    embed=discord.Embed(description="`,server` then your set!",color=0xbb00ff)
    await ctx.reply(embed=embed)


  @gen.command()
  async def poll(self,ctx):
    embed=discord.Embed(description="`,poll` + your keywords",color=0xbb00ff)
    await ctx.reply(embed=embed)


  @gen.command()
  async def embedinfo(self,ctx):
    embed=discord.Embed(description="`,embed` title description .",color = 0xbb00ff)
    await ctx.reply(embed=embed)



##################################################################################################################

  @commands.group() 
  async def mod(self,ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(name=ctx.author.display_name,title=' <:Punished:867002789413519392> Moderation cmds', description="`,mod lock` for how to lock channels. \n \n `,mod unlock` for how to unlock channels. \n \n `,mod purge` for more info on how to purge messages.\n \n `,mod kick` for more info on how to kick members. \n \n `,mod ban` for more info on how to ban members. \n \n `,createrole`for more info on how to create a role. ",color=0xff0000)
        await ctx.reply(embed=embed)


  @mod.command()
  async def lock(self,ctx):
    embed=discord.Embed(description="`,lock <#channel>`",color=0xff0000)
    await ctx.reply(embed=embed)


  @mod.command()
  async def unlock(self,ctx):
    embed=discord.Embed(description="`,unlock <#channel>`",color=0xff0000)
    await ctx.reply(embed=embed)


  @mod.command() 
  async def kick(self,ctx):
    embed=discord.Embed(description = "`,kick <member> [reson]`",color=0xff0000)
    await ctx.reply(embed=embed)


  @mod.command()
  async def ban(self,ctx):
    embed=discord.Embed(description = "`,kick <member> [reson]`",color=0xff0000)
    await ctx.reply(embed=embed)


  @mod.command()
  async def purge(self,ctx):
    embed=discord.Embed(description="`,clear [number]` then your set!",color=0xff0000)
    await ctx.reply(embed=embed)


  @mod.command()
  async def createrole(self,ctx):
    embed=discord.Embed(description="`makerole` <role name>",color=0xff0000)
    await ctx.reply(embed=embed)

##################################################################################################################




  @commands.group()
  async def math(self,ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(name=ctx.author.display_name,title="math cmds!", description="`,math add` for how to use addition cmd \n \n `,math sub` for how to use the subtraction cmd \n \n`,math mult` for how to use the multiplication cmd \n \n `,math div` for how to use the division cmd",color=0xff7b00)
        await ctx.reply(embed=embed)


  @math.command()
  async def add(self,ctx):
    embed=discord.Embed(description="`,add`then type 2 numbers \n EX :arrow_down: \n `,add 5 6` ",color=0xff7b00)
    await ctx.reply(embed=embed)


  @math.command()
  async def sub(self,ctx):
    embed=discord.Embed(description="`,sub` then type 2 numbers \n EX :arrow_down: \n `,sub 6 2` this cmd also outputs results for negative numbers. ",color=0xff7b00)
    await ctx.reply(embed=embed)


  @math.command()
  async def mult(self,ctx):
    embed=discord.Embed(description="`,mult` then type 2 numbers \n EX :arrow_down: \n `,mult 6 6` this cmd also outputs results for negative numbers. ",color=0xff7b00)
    await ctx.reply(embed=embed)


  @math.command()
  async def div(self,ctx):
    embed=discord.Embed(description="`,div` then type 2 numbers \n EX :arrow_down: \n `,div 6 3` this cmd also outputs results for negative numbers.", color=0xff7b00)
    await ctx.reply(embed=embed)


##################################################################################################################


def setup(client):
  client.add_cog((colc(client)))
