import datetime
import discord
from src.command import Commande
from src.help import Help
from src.show import Show


class MyClient(discord.Client, Commande, Help, Show):
    def __init__(self, default_intents):
        discord.Client.__init__(self, intents=default_intents)
        Help.__init__(self)

    async def on_member_join(self, member):
        """
        event when member join a guild

        Parameters:
            discord.Client : self
            discord.Member : member

        Return:
            None
        """
        if member.guild.id == 799370166097412116:
            welcome = member.guild.get_channel(799371570933923880)
            rules = member.guild.get_channel(799666237801758741)
            message = "{}\n Welcome in Tierlist suport server check {}".format(
                member.mention,
                rules.mention)
            role = member.guild.get_role(802607681629716550)
            await member.add_roles(role)
            await welcome.send(message)

    async def on_resumed(self):
        """
        event when the bot was reconected

        Parameters:
            discord.Client : self

        Return:
            None
        """
        suport = self.get_guild(799370166097412116)
        channel = suport.get_channel(799372448998490122)
        date = datetime.datetime.now()
        embedVar = discord.Embed(title="Resume",
                                 description="Logged as {}".format(self.user),
                                 color=0x0000ff,
                                 timestamp=date)
        await channel.send(embed=embedVar)

    async def on_ready(self):
        """
        event when the bot is ready

        Parameters:
            discord.Client : self

        Return:
            None
        """
        data = self.load("src/prefix.json")
        for element in self.guilds:
            if element not in data:
                data[str(element)] = "tl?"
        suport = self.get_guild(799370166097412116)
        channel = suport.get_channel(799372448998490122)
        date = datetime.datetime.now()
        embedVar = discord.Embed(title="Ready",
                                 description="Logged as {}".format(self.user),
                                 color=0x00ff00,
                                 timestamp=date)
        await channel.send(embed=embedVar)
        await self.change_presence(activity=discord.Game(
            name="tl?help for doc"))

    async def on_guild_join(self, guild):
        """
        event when the bot join a guild

        Paramters:
            discord.MyClient : self
            discord.Guild : guild

        Retrun :
            None
        """
        suport = self.get_guild(799370166097412116)
        channel = suport.get_channel(802700172320178227)
        name = "servers {}".format(len(self.guilds))
        await channel.edit(name=name)
        date = datetime.datetime.now()
        embedVar = discord.Embed(title="Good News",
                                 description="New guild : {}".format(
                                     guild.name),
                                 color=0x00ff00,
                                 timestamp=date)
        await channel.send(embed=embedVar)
        self.createfolder("tierList/{}.json".format(guild.id))
        data = self.load("src/prefix.json")
        data[str(guild.id)] = "tl?"
        self.save("src/prefix.json", data)
        f = open("message/welcome.txt", "r")
        lignes = f.readlines()
        message = "".join(lignes)
        try:
            await guild.system_channel.send(message)
        except Exception:
            pass

    async def on_guild_remove(self, guild):
        """
        event when the bot is removed a guild

        Paramters:
            discord.MyClient : self
            discord.Guild : guild

        Retrun :
            None
        """
        suport = self.get_guild(799370166097412116)
        channel = suport.get_channel(802700172320178227)
        name = "servers {}".format(len(self.guilds))
        await channel.edit(name=name)
        date = datetime.datetime.now()
        embedVar = discord.Embed(title="Bad News",
                                 description="guild delte : {}".format(
                                     guild.name),
                                 color=0xff0000,
                                 timestamp=date)
        await channel.send(embed=embedVar)
        self.deletFolder("tierList/{}.json".format(guild.id))
        data = self.load("src/prefix.json")
        del data[str(guild.id)]
        self.save("src/prefix.json", data)

    async def on_message(self, message):
        """
        event when the message send in the chat

        Parameters:
            discord.Client : self
            Message : message

        Return :
            None
        """
        if message.author.id == self.user.id:
            return

        prefixs = self.load("src/prefix.json")
        if message.content.startswith(
                prefixs[str(message.guild.id)] + "help"):
            await self.helpTraitment(message, prefixs[str(message.guild.id)])
        elif message.content.startswith(
                prefixs[str(message.guild.id)] + "show"):
            await self.showTrait(message, prefixs[str(message.guild.id)])
        elif message.content.startswith(
                prefixs[str(message.guild.id)]):
            reponse = self.traitment(message, prefixs[str(message.guild.id)])
            await message.channel.send(reponse)
