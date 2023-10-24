import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=intents)

in_queue = {
    1234654 : {
        "Main": [1234654, 56789, 65798], 
        "School": "KSU"
    }
}

lobbies = {
    1 : [[1234654],]
}

school_database = {
    "KSU" : {
        "Black" : [
            1, 
            2,
            [1234654, 56789, 568745]
        ]
    }
}

admins = []

# Non-Admin Commands
@bot.command()
async def get(ctx, captain):
    #returns the team of the captain and all participating players
    # this would be used for a quick check to see if a certain discord user who claims to be playing, really is (in-case of uncertainty)
    # once again, if the team was set by an admin, the captain will default to the first person in the list of players added
    
    found = False
    
    if type(captain) != int:
        captain = captain.id
        
    if captain in in_queue:
        print(in_queue[captain])
        found = True
        
    for lobby in lobbies:
        if captain in lobby:
            print(lobby[captain])
            found = True
            break
    
    if not found:
        print("couldn't find team")
    
    pass

@bot.command()
async def add(ctx, school, team, *players):
    #add their team to the queue
    
    in_queue[ctx.author.id] = {
        ["Players"] : [],
        ["School"] : school,
        ["Team"] : team,
    }
    
    for player in players:
        if type(player) == int:
            #assuming that they directly put their userid in
            in_queue[ctx.author.id]["Players"].append(player)
        else:
            #for when the use @thelegend27
            in_queue[ctx.author.id]["Players"].append(player.id)
    
    #sending for test purposes
    ctx.send(in_queue[ctx.author.id])
    
    pass

@bot.command()
async def drop(ctx):
    #drop the team from the queue
    
    removed = False
    try:
        del in_queue[ctx.author]
    except KeyError:
        for num, contestants in lobbies.items():
            try:
                del contestants[ctx.author]
                removed = True
                break
            except KeyError:
                pass
    
    if not removed:
        print("couldn't find team")
        
    pass

bot.add_command(get)
bot.add_command(add)
bot.add_command(drop)

# Admin Commands
@bot.command()
async def register(ctx, school, team, *players):
    # it will add the school if it doesn't exist, otherwise it will just append the team to their registered teams
    
    if not school_database.find(school):
        school_database[school] = {
            team : [
                -1, 
                -1, 
                []
            ],
        }
        
    else:
        school_database[school][team] = [
            -1, #priority
            -1, #weight class (metaphor)
            [] #players
        ]
        
    for player in players:
        if type(player) == int:
            #assuming that they directly put their userid in
            school_database[school][team][2].append(player)
            print(f"{player} added")
        else:
            #for when the use @thelegend27
            school_database[school][team][2].append(player.id)
            print(f"{player.id} added")
    
    #sending for test purposes
    ctx.send(school_database[school])
    
    pass

@bot.command()
async def remove(ctx, school, team):
    # if the team paramater is filled, then it will only remove that team from the school, not the whole school
    # leave the team paramater blank if you want to remove the whole school
        
    if school in school_database:
        if team == "":
            del school_database[school]
            print("school removed")
        else:
            if team in school_database[school]:
                del school_database[school][team]
                print("team removed")
            else:
                print("team not found")
    
    pass

@bot.command()
async def fadd(ctx, school, team, *players):
    #force add a team to the queue
    
    captain = ctx.author.id
    
    if type(players[0]) == int:
        captain = players[0]
    else:
        captain = players[0].id
    
    in_queue[captain] = {
        ["Players"] : [],
        ["School"] : school,
        ["Team"] : team,
    }
    
    for player in players:
        if type(player) == int:
            #assuming that they directly put their userid in
            in_queue[captain]["Players"].append(player)
        else:
            #for when the use @thelegend27
            in_queue[captain]["Players"].append(player.id)
    
    #sending for test purposes
    ctx.send(in_queue[captain])
    
    pass

@bot.command()
async def fdrop(ctx, captain):
    #force drop a team from the queue
    #the captain paramater should be the user who added them to the queue through the !add command, otherwise it is the first player in their team
        #ex. !fadd KSU Black @user1 @user2 @user3
        #since there is no team capatin (they were added by an admin) it would default to user1
        
    captain = ctx.author.id
    
    if type(captain) != int:
        captain = captain.id
    
    removed = False
    try:
        del in_queue[captain]
    except KeyError:
        for num, contestants in lobbies.items():
            try:
                del contestants[captain]
                removed = True
                break
            except KeyError:
                pass
    
    if not removed:
        print("couldn't find team")
    
    pass

@bot.command()
async def roll(ctx):
    #begins the lobby assignments (gives lobby 1, 2 or 3 role)
    pass

@bot.command()
async def op(ctx, user):
    #allows the specified user to use admin commands
    
    if ctx.author.id in admins:
        
        if type(user) != int:
            user = user.id
        
        admins.append(user)
        
    pass

@bot.command()
async def deop(ctx, user):
    #disallows the specified user from using admin commands
    
    if ctx.author.id in admins:
        
        if type(user) != int:
            user = user.id
        
        admins.remove(user)
    
    pass

bot.add_command(register)
bot.add_command(remove)
bot.add_command(fadd)
bot.add_command(fdrop)
bot.add_command(roll)
bot.add_command(op)
bot.add_command(deop)

bot.run(TOKEN)
