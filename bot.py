import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Il bot è online come {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    # L'utente è entrato in un canale vocale
    if before.channel is None and after.channel is not None:
        voice_channel = after.channel

        # Se è il primo utente nel canale
        if len(voice_channel.members) == 1:
            text_channel = discord.utils.get(member.guild.text_channels, name="froci")
            if text_channel:
                await text_channel.send(
                    f"🔔 **{member.display_name}** ha avviato una chiamata vocale in **{voice_channel.name}**! Unisciti "
                )

bot.run("MTM4NTU5MzM1Mjk2Mjk2OTYxMA.GT4VXM.2xz7bKC0LbhTH7Ok_UBMJNUae3IadyO9yJIpAE")
