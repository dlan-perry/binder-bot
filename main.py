import discord
from fastapi import Depends
from discord.ext import commands
import mongo
from sqlalchemy.orm import Session
import typing
from typing import Literal
from decouple import config
from qualities import Qualities
BINDERS = ["trading", "looking", "have","selling"]

intents = discord.Intents.default()

intents.message_content= True


bot = commands.Bot(intents=discord.Intents.all(), command_prefix="mtg ")


@bot.command(name="start", help="initialize the user as a member of the DylBot service.")
async def start(ctx):
    print("here")
    resp = mongo.add_user(ctx.author.id)

    if resp:
        await ctx.send("You now have a DylBot account!")
    else:
        await ctx.send("You already have a DylBot account! enter the help command to get started.")

@bot.command(name="decks")
async def decks(ctx, member: discord.Member):
    cnt, resp = mongo.find_decks(ctx.author.id)
    if cnt == 0:
        await ctx.send(member.mention + " has no decks stored")
    else:
        for item in resp:
            await ctx.send(item["cards"])


@bot.command(name="add deck")
async def add_deck(ctx):
    if ctx.message:
        pass

    
@bot.command(name="deckcheck")
async def deckcheck(ctx, member: discord.Member):
    
    pass
'''
@bot.command(name="decks")
async def decks_2(ctx):
    cnt, resp = mongo.find_decks(ctx.author.id)
    if cnt == 0:
        await ctx.send(ctx.author + " has no decks stored")
    else:
        for item in resp:
            await ctx.send(item["cards"])
'''
@bot.command(name="new")
async def new(ctx, token: Literal["deck", "card"], atmnt : typing.Optional[discord.Attachment]):
    if token == "deck":
        mongo.add_deck(ctx.author.id, atmnt)



@bot.command(name="test")
async def test(ctx):
    #mongo.add_to_binder(ctx.author.id, "ponder", "mtg", binder="have")
    pass


@bot.command(name="add")
async def insert(ctx, card_name, to, dest, atmnt : typing.Optional[discord.Attachment]):
    pass
    #add ponder to trading
    


@bot.command(name="suggest")
async def suggest(ctx):
    pass

@bot.command(name="sell")
async def sell(ctx):
    pass

@bot.command(name="trade")
async def trade(ctx):
    pass

@bot.command(name="buy")
async def buy(ctx):
    pass

@bot.command(name="copy")
async def copy(ctx):
    pass


def format_card(card_name, set=None, foiled=False, quality=Qualities.NM):
    pass




@bot.listen('on_message')
async def on_message(message):
    print("called")
    
    cards = []
    if (message.content.count("DD")>=2):
        cards = message.content.split("DD")
    print(cards)
    cards = cards[1::2]
    if cards:
        card = None
        for count, phrase in enumerate(cards):
            card = mongo.find_card_by_name(format_card_name(phrase))
            if card:
                await message.channel.send(check_card(card))
        


def format_card_name(parts):
    card_name = ""
    non_caps = ["the", "of", "in", "a", "to", "at"]
    if type(parts) == str:
        token = parts.split(" ")
    else:
        if " " in parts:
            token = parts.split(" ")
    if len(token) > 1:
        for part in token:
            if len(part) > 1:
                if part not in non_caps:
                    card_name += (part[0].upper() + part[1:]) + " "
                else:
                    card_name += part + " "
    else:
        card_name = token[0][0].upper() + token[0][1:]
    
    return card_name.strip()

    
        


def check_card(card):
    card_text = ""
    if card["layout"] == "split":
        card_text += card["card_faces"][0]["oracle_text"] + "\n"
        card_text += "/"*25 + "\n"
        card_text += card["card_faces"][1]["oracle_text"] + "\n"
        card_text += card["image_uris"]["large"]
    else:
        card_text = card["oracle_text"] + "\n" + card["image_uris"]["large"]
        print("here")
    return card_text















'''
@client.event
async def on_reader():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('..'):
        await message.channel.send("yoyo")
'''

bot.run(config("discord_key"))
