
import aiohttp
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import datetime, time
import os
global vtc_help
global bot_help
vtc_help = ("GARIUM")
bot_help = ("COMMANDS")
client = commands.Bot(command_prefix='/')
Client = discord.Client()
client.remove_command('help')

@client.event
async def on_ready():
    print ("The bot is ready to use.")
    print ("Name: " + client.user.name)
    print ("ID: " + client.user.id)
    counter = 0
    while not counter > 0:
        await client.change_presence(game=discord.Game(name='Garium Transports', type=3))
        await asyncio.sleep(5.5)
        await client.change_presence(game=discord.Game(name="Monitoring the server", type=3))
        await asyncio.sleep(5.5)

@client.command(pass_context=True)
async def ping(ctx):
    '''A ping command'''
    if not ctx.message.author.bot:
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        embed=discord.Embed(title="Pong!", description='This message took around {}ms.'.format(round((t2-t1)*1000)), color=0xffff00)
        await client.say(embed=embed)
    else:
        return False

@client.command(pass_context=True)
async def purge(ctx, amount=301):
    '''Usage: /purge [amount]'''
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '416226732966936577':
        try:
            channel = ctx.message.channel
            messages = []
            async for message in client.logs_from(channel, limit=int(amount) + 1):
                messages.append(message)
            await client.delete_messages(messages)
            await client.say(":white_check_mark: Messages deleted. :thumbsup:")
        except:
            print (Exception)
            await client.say("The number must be between 1 and 300 and the message be maximum 14 days old.:x:")
    else:
        await client.say("You need Admin perms to use this. :x:")

@client.command(pass_context=True, no_pm=True)
async def kick(ctx, user: discord.Member, * ,reason : str = None):
    '''Usage: /kick [member] [reason]'''
    if not ctx.message.author.bot:
        if ctx.message.author.server_permissions.administrator:
            if reason == "None":
                reason = "(No reason logged!)"
            await client.send_message(user, "You're kicked from **{}** server for this: **".format(ctx.message.server.name) + reason + "**")
            await client.say("Bye, {}. You got kicked :D".format(user.mention))
            await client.kick(user)  
        else:
            await client.say("You need Admin prems to use this! :x:")
    else:
        return False

@client.command(pass_context=True)
async def serverinfo(ctx):
    '''A useful command.'''
    if not ctx.message.author.bot:
        online = 0
        for i in ctx.message.server.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1
        role_count = len(ctx.message.server.roles)
        emoji_count = len(ctx.message.server.emojis)
        embed = discord.Embed(title="Information from this server: {}".format(ctx.message.server.name), description="Here it is:", color=0x00ff00)
        embed.add_field(name="Name: ", value=ctx.message.server.name, inline=True)
        embed.add_field(name="ID: ", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Number of roles: ", value=len(ctx.message.server.roles), inline=True)
        embed.add_field(name="Members: ", value=len(ctx.message.server.members))
        embed.add_field(name='Currently online', value=online)
        embed.add_field(name="Server created at: ", value=ctx.message.server.created_at.__format__('%Y. %m. %d. @ %H:%M:%S'), inline=True)
        embed.add_field(name="Current channel: ",value=ctx.message.channel, inline=True)
        embed.add_field(name="Server owner's name: ",value=ctx.message.server.owner.mention, inline=True)
        embed.add_field(name="Server owner's status: ",value=ctx.message.server.owner.status, inline=True)
        embed.add_field(name="Server region: ",value=ctx.message.server.region, inline=True)
        embed.add_field(name='Moderation level', value=str(ctx.message.server.verification_level))
        embed.add_field(name='Number of emotes', value=str(emoji_count))
        embed.add_field(name='Highest role', value=ctx.message.server.role_hierarchy[0])
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
        await client.say(embed=embed)
    else:
        return False


@client.event
async def on_member_join(member):
    if member.server.name == "Garium Transport":
        channel = discord.Object("530523959301767169")
        embed = discord.Embed(title="New member joined", description="Details: ", color=0x00ffed)
        embed.add_field(name="New user:", value=member.name, inline=True)
        embed.add_field(name='ID', value=member.id, inline=True)
        embed.add_field(name="Status", value=member.status, inline=True)
        embed.add_field(name='Game', value=member.game, inline=True)
        embed.add_field(name='Joined at', value=member.joined_at.__format__('%A, %Y. %m. %d. @ %H:%M:%S', inline=True))
        embed.set_author(name=member, icon_url=member.avatar_url)
        await client.send_message(channel, embed=embed)


@client.command(pass_context=True)
async def inv(ctx):
    await client.say("https://discordapp.com/api/oauth2/authorize?client_id=539875983071641620&permissions=8&scope=bot")

@client.command(aliases=['commands'], pass_context=True)
async def help(ctx):
    await client.send_message(ctx.message.author, "Hello! I'm the own bot of **Garium Transport**! If you want to know more informations about **my commands**, type ``commands``! If you want to know more about **Garium Transports**, type ``garium``! Have a good day! :sun_with_face:")


@client.event
async def on_message(message):
    if message.channel.type == discord.ChannelType.private:
        global vtc_help
        await client.process_commands(message)
        contents = message.content.split(" ")
        for word in contents:    
            if word.upper() in vtc_help:
                try:
                    await client.send_message(message.author, "Garium Transport\nGarium Transport is a Virtual Trucking Company which was founded in October 2018 and offers fun while driving and a good membership. At our company, we are going on big events and we also host our self-made convoys. More information can be given by our staff members.\nApplication Form:\nhttps://goo.gl/forms/QAO2X2fMcPAy95Sx1\nOur Logging Platform:\nhttps://vtlog.net/vtc/3817\nIf you have any questions go ahead and ask some of our team.")
                except:
                    await client.send_message(message.author, "I can't understand that message! Please try using ``commands`` or ``garium``")
            else:
                return
	else:
	    pass

@client.event
async def on_message(message):
    if message.channel.type == discord.ChannelType.private:
        global bot_help
        await client.process_commands(message)
        contents = message.content.split(" ")
        for word in contents:
            if word.upper() in bot_help:
                try:
                    await client.send_message(message.author, ".")
                except:
                    await client.send_message(message.author, "I can't understand that message! Please try ``commands`` or ``garium``!")
            else:
                return
	else:
	    pass
	
@client.command(pass_context=True)
async def shutdown(ctx):
    if ctx.message.author.id == "125196565265514496":
        await client.say("I'm shutting down! Good bye!")
        await client.logout()
    else:
        await client.say("You **don't** have permission to shut down this bot!")


@client.command(pass_context=True)
async def warn(ctx, member: discord.Member, *, reason : str = None):
    if not ctx.message.author.bot:
        await client.delete_message(ctx.message)
        await client.send_message(member, "You received a warn from **{}** from this server: **{}** . Reason: **{}**".format(ctx.message.author , ctx.message.server.name , reason))
        await client.say(":white_check_mark: I sent the warn!! :thumbsup:")
    else:
        return False


@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
    '''Usage: /mute [mention] Need role named "Muted" '''
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '416226732966936577' or ctx.message.author.id == '497797334684401664' or ctx.message.author.id == '125196565265514496':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User muted!", description="**{0}** has been muted by **{1}** . :white_check_mark: ".format(member.mention, ctx.message.author.mention), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Permission denied!", description="You don't have permission to use this command. :x:", color=0xff00f6)
        await client.say(embed=embed)

@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
    '''Usage: /unmute [mention] Need role named "Muted" '''
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '416226732966936577' or ctx.message.author.id == '497797334684401664' or ctx.message.author.id == '125196565265514496':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User unmuted!", description="**{0}** has been unmuted by **{1}** . :white_check_mark: ".format(member.mention, ctx.message.author.mention), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Permission denied!", description="You don't have permission to use this command. :x:", color=0xff00f6)
        await client.say(embed=embed)




client.run(os.environ.get('TOKEN'))
