#!/usr/bin/python3
import discord
from src.MyClient import MyClient
import os
from dotenv import load_dotenv

default_intents = discord.Intents()
default_intents = discord.Intents.default()
default_intents.members = True
load_dotenv()
client = MyClient(default_intents, os.getenv("TOPGG"))
client.run(os.getenv("TOKEN"))
