#!/usr/bin/python3.9
import discord
from src.MyClient import MyClient
import os
from dotenv import load_dotenv

default_intents = discord.Intents()
default_intents = discord.Intents.default()
default_intents.members = True
client = MyClient(default_intents)
load_dotenv()
client.run(os.getenv("TOKEN"))
