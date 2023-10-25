
#TODO: finish the replace command
#TODO: mass allow updating by reading from a database and updating it based on that (csv goes to database that the bot reads and updates values based on it)

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!', intents=intents)
elo_gains = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

'''
priority:

0 - pros
1 - collegiate
2 - registered team
3 - open team

'''

queue_database = {
    "p0": {},
    "p1": {},
    "p2": {},
    "p3": {}
}

lobbies_database = {
    0 : {
        "<@327422276473454592>" : {
            "Group": "KSU",
            "Team": "Gold",
            "Players": [f"<@{327422276473454592}>", f"<@{389897757550444545}>", f"<@{290483206610747392}>"]
        }
    }
}

group_database = {
    "KSU" : {
        "Black" : [
            1, #priority
            0, #elo
            [f"<@{221752443245953024}>", f"<@{346750457731088404}>", f"<@{393584820912914432}>"] #possible players
        ],
        "Gold": [
            2,
            0,
            [f"<@{327422276473454592}>", f"<@{389897757550444545}>", f"<@{290483206610747392}>"]
        ]
    }
}

admin_database = ["<@327422276473454592>"]

def get_priority(group, team):
    if group in group_database and team in group_database[group]:
        return group_database[group][team][0]
    return 3

def embeded_school(group):
    #create the embed
    dictionary = group_database[group]
    title = group
    embed = discord.Embed(title=title, color=discord.Color.red()) 
    for team, info in group_database[group].items():
        players = ""
        for player in info[2]:
            players += f"{player}\n"
            
        embed.add_field(name=f"{team}", value=players)
    
    #send the embed
    return embed

def embeded_team(team):
    #create the embed
    embed = discord.Embed(color=discord.Color.red()) 
    players = ""
    for player in team["Players"]:
        players += f"{player}\n"
            
    embed.add_field(name=(team["Group"] + " " + team["Team"]), value=players)
    
    #send the embed
    return embed

# Non-Admin Commands
@bot.command()
async def get(ctx, target, identifier=""):
    #returns the team of the captain and all participating players
    # this would be used for a quick check to see if a certain discord user who claims to be playing, really is (in-case of uncertainty)
    # once again, if the team was set by an admin, the captain will default to the first person in the list of players added
    
    found = False

    if target == "team":
        captain = f"<@{ctx.author.id}>"
        if identifier.find("<@") == -1:
            captain = f"<@{identifier}>"
        
        for priority, queue in queue_database.items():
            if captain in list(queue.keys()):
                found = True
                await ctx.send(embed=embeded_team(queue[captain]))
            
        
        if not found:
            for _, lobby in lobbies_database.items():
                if captain in list(lobby.keys()):
                    found = True
                    await ctx.send(embed=embeded_team(lobby[captain]))
                    break
        
        if not found:
            await ctx.send("couldn't find team")
            
    elif target == "group":
        if identifier in group_database:
            found = True
            await ctx.send(embed=embeded_school(identifier))
        
        if not found:
            await ctx.send("couldn't find group")
    
    elif target == "admins":
        #create the embed
        embed = discord.Embed(color=discord.Color.red()) 
        adms = ""
        for admin in admin_database:
            adms += f"{admin}\n"
                
        embed.add_field(name="Admins", value=adms)
        
        #send the embed
        await ctx.send(embed=embed)

@bot.command()
async def add(ctx, group, team, *players):
    #add their team to the queue
    
    captain = f"<@{ctx.author.id}>"
    priority = get_priority(group, team)
    
    queue_database[f"p{priority}"][captain] = {
        "Players" : [],
        "Group" : group,
        "Team" : team,
    }
    
    for player in players:
        if player.find("<@") == -1:
            player = f"<@{player}>"
        
        #for non-registered teams
        if group.lower() == "open":
            queue_database[f"p{priority}"][captain]["Players"].append(player)
        
        #for registered teams
        elif player in group_database[group][team][2]:
            queue_database[f"p{priority}"][captain]["Players"].append(player)
            
        else:
            await ctx.send(f"{player} is not registered on the team.")
    
    await ctx.send(embed=embeded_team(queue_database[f"p{priority}"][captain]))

@bot.command()
async def drop(ctx):
    #drop the team from the queue
    
    removed = False
    captain = f"<@{ctx.author.id}>"
    try:
        for _, queue in queue_database.items():
            try:
                del queue[captain]
                removed = True
                await ctx.send(f"{captain}'s team has been removed")
            except KeyError:
                pass
                
    except KeyError:
        for _, contestants in lobbies_database.items():
            try:
                del contestants[captain]
                removed = True
                await ctx.send(f"{captain}'s team has been removed")
                break
            except KeyError:
                pass
    
    if not removed:
        await ctx.send("couldn't find team")

# Admin Commands
@bot.command()
async def register(ctx, group, team, *players):
    # it will add the group if it doesn't exist, otherwise it will just append the team to their registered teams
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        if group in group_database: #if it didn't find the group
            group_database[group][team] = [
                2, #priority
                100, #elo
                [] #players
            ]
        else:
            group_database[group] = {
                team : [
                    2, 
                    100, 
                    []
                ]
            }
            
        for player in players:
            if player.find("@") == -1:
                #for when the use @thelegend27
                player = f"<@{player}>"
                group_database[group][team][2].append(player)
                await ctx.send(f"{player} added")
            else:
                #assuming that they directly put their userid in
                group_database[group][team][2].append(player)
                await ctx.send(f"{player} added")

        #send the embed
        await ctx.send(embed=embeded_school(group))

@bot.command()
async def remove(ctx, group, team):
    # if the team paramater is filled, then it will only remove that team from the group, not the whole group
    # leave the team paramater blank if you want to remove the whole group
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        if group in group_database:
            if team == "":
                del group_database[group]
                print("group removed")
            else:
                if team in group_database[group]:
                    del group_database[group][team]
                    print("team removed")
                else:
                    print("team not found")

@bot.command()
async def fadd(ctx, group, team, *players):
    #force add a team to the queue
    
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        captain = players[0]
        priority = get_priority(group, team)
        
        if players[0].find("<@") == -1:
            captain = f"<@{players[0]}>"           
        
        queue_database[f"p{priority}"][captain] = {
            "Players" : [],
            "Group" : group,
            "Team" : team,
        }
        
        for player in players:
            if player.find("<@") == -1:
                player = f"<@{player}>"
            
            #for non-registered teams
            if group.lower() == "open":
                queue_database[f"p{priority}"][captain]["Players"].append(player)
            
            #for registered teams
            elif player in group_database[group][team][2]:
                queue_database[f"p{priority}"][captain]["Players"].append(player)
                
            else:
                await ctx.send(f"{player} is not registered on the team.")
        
        await ctx.send(embed=embeded_team(queue_database[f"p{priority}"][captain]))

@bot.command()
async def fdrop(ctx, captain):
    #force drop a team from the queue
    #the captain paramater should be the user who added them to the queue through the !add command, otherwise it is the first player in their team
        #ex. !fadd KSU Black @user1 @user2 @user3
        #since there is no team capatin (they were added by an admin) it would default to user1
    
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        
        removed = False
        if captain.find("<@") == -1:
            captain = f"<@{captain}>"

        try:
            for _, queue in queue_database.items():
                try:
                    del queue[captain]
                    removed = True
                    await ctx.send(f"{captain}'s team has been removed")
                except KeyError:
                    pass
                    
        except KeyError:
            for _, contestants in lobbies_database.items():
                try:
                    del contestants[captain]
                    removed = True
                    await ctx.send(f"{captain}'s team has been removed")
                    break
                except KeyError:
                    pass
        
        if not removed:
            await ctx.send("couldn't find team")

@bot.command()
async def roll(ctx):
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        #group_database = group_database #so we don't fetch it a whole bunch
        
        #create all the lobbies needed
        total_teams = 0
        total_lobby_elo = {0:0}
        total_lobby_teams = {0:0}
        for _, queue in queue_database.items():
            queue += len(queue)
        
        for i in range(total_teams//20):
            #create lobbies as needed
            lobbies_database[i] = {}
            total_lobby_elo[i] = 0
            total_lobby_teams[i] = 0
        
        priority = 0
        for priority, queue in queue_database.items():
            for captain, team in queue.items():
                lowest_lobby_num = 0
                lowest_lobby_avg_elo = 0
                
                for lobby_num, elo in total_lobby_elo.items():
                    next_lobby_average_elo = total_lobby_elo[lobby_num]/total_lobby_teams[lobby_num]
                    
                    if next_lobby_average_elo <= lowest_lobby_avg_elo:
                        lowest_lobby_avg_elo = total_lobby_elo[lowest_lobby_num]/total_lobby_teams[lowest_lobby_num]
                        lowest_lobby_num = lobby_num
                
                lobbies_database[lowest_lobby_num][captain] = team
                del queue[captain]
                
                if len(total_lobby_teams[lowest_lobby_num]) >= 20:
                    del total_lobby_elo[lowest_lobby_num]
                    del total_lobby_teams[lowest_lobby_num]

@bot.command()
async def op(ctx, user):
    #allows the specified user to use admin commands
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        if user.find("<@") == -1:
            user = f"<@{user}>"
        
        admin_database.append(user)

@bot.command()
async def deop(ctx, user):
    #disallows the specified user from using admin commands
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        if user.find("<@") == -1:
            user = f"<@{user}>"
        
        admin_database.remove(user)
        
@bot.command()
async def setPriority(ctx, group, team, priority):
    #sets the specified teams priority
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        if group in group_database and team in group_database[group]:
            group_database[group][team][0] = priority
        else:
            await ctx.send("No registered group / team found")

@bot.command()
async def setElo(ctx, group, team, elo):
    #sets the specified teams elo
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        if group in group_database and team in group_database[group]:
            group_database[group][team][1] = elo
        else:
            await ctx.send("No registered group / team found")
            
@bot.command()
async def placeTeam(group, team, place):
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        if group in list(group_database.keys()) and team in list(group_database[group].keys()):
            group_database[group][team][1] += elo_gains[place+1]
        return 100

@bot.command()
async def incrementElo(group, team, elo):
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        if group in list(group_database.keys()) and team in list(group_database[group].keys()):
            group_database[group][team][1] += elo
        return 100

@bot.command()
async def resetElo(ctx):
    #mass resets all elo back to 100 default
    admin = f"<@{ctx.author.id}>"
    if admin in admin_database:
        for _, group in group_database.items():
            for team in group:
                team[1] = 100

@bot.command()
async def replace(ctx, target, group, team, player, sub):
    #replaces the player with sub when in a lobby
    captain = f"<@{ctx.author.id}>"
    if captain in admin_database:
        if target.lower() == "player":
            if group in group_database and team in group_database[group]:
                group_database[group][team][1] = elo
            else:
                await ctx.send("No registered group / team found")
        elif target.lower() == "team":
            pass

bot.run(DISCORD_TOKEN)
