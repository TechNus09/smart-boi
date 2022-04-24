import os
import time
import interactions as it
from interactions import Button, ButtonStyle, SelectMenu, SelectOption, ActionRow
import math

from data import *
from Mining import *
from Smithing import *
from Woodcutting import *
from Crafting import *
from Fishing import *
from Cooking import *
from guide_adapter import *


import logging




bot = it.Client(os.getenv("TOKEN"))

#logging.basicConfig(level=logging.DEBUG)
calc_reg = {}
g_reg = {}
lvl_reg = {}
##################calc functions##############

####get xp needed####
def getxp( lv, nlv, per, nper):
    minxp= lvltab[lv-1] + (lvldef[lv-1]*(per/100))
    if nlv == 120:
        bigxp= lvltab[119]
    else:
        bigxp= lvltab[nlv-1] + (lvldef[nlv-1]*(nper/100))
    XPneeded = round(bigxp - minxp)
    return XPneeded

####get boost value####
def getboost(b_list):
    boost_value = 1.00
    for i in b_list:
        boost_value = boost_value * boostsValues[i]
    return boost_value
####boost_list to string
def boost_str_emoji(l):
    temp=""
    for i in range(len(l)):
        temp = temp + boosts_emojis[l[i]] + l[i] + " "
    return temp
#######################Components################################ 
skills_menu = it.SelectMenu(
            options= [
	            it.SelectOption(label=f'Combat (Melee/Magic)',value='0', emoji=it.Emoji(id=962217488479834142 ,animated=False)._json),
	            it.SelectOption(label=f'Mining',value='1', emoji=it.Emoji(id=962217952927698954,animated=False)._json),
	            it.SelectOption(label=f'Smithing',value='2', emoji=it.Emoji(id=945264297167175681,animated=False)._json),
	            it.SelectOption(label=f'Woodcutting',value='3', emoji=it.Emoji(id=962217565780865024,animated=False)._json),
	            it.SelectOption(label=f'Crafting',value='4', emoji=it.Emoji(id=922871203130134528,animated=False)._json),
	            it.SelectOption(label=f'Fishing',value='5', emoji=it.Emoji(id=962217539767771217,animated=False)._json),
	            it.SelectOption(label=f'Cooking',value='6', emoji=it.Emoji(id=962217512035053599,animated=False)._json),
	            it.SelectOption(label=f'Tailoring',value='7', emoji=it.Emoji(id=937013045488648252,animated=False)._json),
	            it.SelectOption(label=f'Cancel',value='Cancel',emoji=it.Emoji(id=cancel_id,animated=False)._json)
	                ],
	            placeholder="Select Skill !",
	            custom_id="select_skill"
	                        )
g_skills_menu = it.SelectMenu(
            options= [
	            it.SelectOption(label=f'Mining',value='1', emoji=it.Emoji(id=962217952927698954,animated=False)._json),
	            it.SelectOption(label=f'Smithing',value='2', emoji=it.Emoji(id=945264297167175681,animated=False)._json),
	            it.SelectOption(label=f'Woodcutting',value='3', emoji=it.Emoji(id=962217565780865024,animated=False)._json),
	            it.SelectOption(label=f'Crafting',value='4', emoji=it.Emoji(id=922871203130134528,animated=False)._json),
	            it.SelectOption(label=f'Fishing',value='5', emoji=it.Emoji(id=962217539767771217,animated=False)._json),
	            it.SelectOption(label=f'Cooking',value='6', emoji=it.Emoji(id=962217512035053599,animated=False)._json),
	            #it.SelectOption(label=f'Tailoring',value='7', emoji=it.Emoji(id=937013045488648252,animated=False)._json),
	            it.SelectOption(label=f'Cancel',value='Cancel',emoji=it.Emoji(id=cancel_id,animated=False)._json)
	                ],
	            placeholder="Select Skill !",
	            custom_id="g_select_skill"
	                        )


########make select_menu with 1 choice
def MakeMenu(skill_id,PH,C_ID):
    resources_list = skill_rsc[int(skill_id)]
    temp_list = []
    for i in resources_list:
        temp_list.append(it.SelectOption(
                                        label=i[0],
                                        value=i[0],
                                        emoji=it.Emoji(id=i[1],animated=False)._json
                                        )
                        )
    temp_list.append(it.SelectOption(
                                    label="Cancel",
                                    value="Cancel",
                                    emoji=it.Emoji(id=cancel_id,animated=False)._json
                                    )
                    )
    menu = it.SelectMenu(
                    options=temp_list,
                    placeholder=PH,
                    custom_id=C_ID
                        )
    return menu



########make select_menu with 1 or mor choices

def MakeMenu2(skill_id,PH,C_ID):
    boosts_list = boosts[int(skill_id)]
    temp_list = []
    for i in boosts_list:
        temp_list.append(it.SelectOption(
                                        label=i[0],
                                        value=i[0],
                                        emoji=it.Emoji(id=i[1],animated=False)._json
                                        )
                        )
    temp_list.append(it.SelectOption(
                                    label="Cancel",
                                    value="Cancel",
                                    emoji=it.Emoji(id=cancel_id,animated=False)._json
                                    )
                    )
    if skill_id == '0' or skill_id == '2' :
        menu = it.SelectMenu(
                        options=temp_list,
                        placeholder=PH,
                        custom_id=C_ID,
                        min_values=1,
                        max_values=4
                            )
    elif skill_id == '1':
        menu = it.SelectMenu(
                        options=temp_list,
                        placeholder=PH,
                        custom_id=C_ID,
                        min_values=1,
                        max_values=3
                            )
    else:
        menu = it.SelectMenu(
                        options=temp_list,
                        placeholder=PH,
                        custom_id=C_ID
                            )
    return menu

def MakeMenu3(PH,C_ID):
    locations_list = locations
    temp_list = []
    for i in range(len(locations_list)):
        temp_list.append(it.SelectOption(
                                        label=locations_list[i][0],
                                        value=str(i),
                                        emoji=it.Emoji(id=locations_list[i][1],animated=False)._json
                                        )
                        )
    temp_list.append(it.SelectOption(
                                    label="Cancel",
                                    value="Cancel",
                                    emoji=it.Emoji(id=cancel_id,animated=False)._json
                                    )
                    )
    menu = it.SelectMenu(
                    options=temp_list,
                    placeholder=PH,
                    custom_id=C_ID
                        )
    return menu

def MakeMenu4(loc_id,PH,C_ID):
    mobs_list = combatRsc[int(loc_id)]
    temp_list = []
    for i in mobs_list:
        temp_list.append(it.SelectOption(
                                        label=i[0],
                                        value=i[0],
                                        emoji=it.Emoji(id=i[1],animated=False)._json
                                        )
                        )
    temp_list.append(it.SelectOption(
                                    label="Cancel",
                                    value="Cancel",
                                    emoji=it.Emoji(id=cancel_id,animated=False)._json
                                    )
                    )
    menu = it.SelectMenu(
                    options=temp_list,
                    placeholder=PH,
                    custom_id=C_ID
                        )
    return menu

def makeguide(skill_name,boost_list):
    guides_d = {
                'Mining' : mining_list ,
                'Smithing' : smithing_list ,
                'Woodcutting' : woodcutting_list ,
                'Crafting' : crafting_list ,
                'Fishing' : fishing_list ,
                'Cooking' : cooking_list 
                }
    b_value = str(round(getboost(boost_list),6))
    title = skill_name.capitalize() + "' Guide"
    description = 'Boost used : ' + boost_str_emoji(boost_list)
    chosen_guide = guides_d[skill_name.capitalize()]

    lvls = chosen_guide["lvls"]
    emojis = chosen_guide["emojis"]
    xp = chosen_guide["xp"]
    names = chosen_guide["m_names"]
    quant = chosen_guide["m_boost"][str(b_value)]
    g_fields = []
    for i in range(len(lvls)):
        field = it.EmbedField(name=lvls[i],value=emojis[i][1]+" "+names[i]+" - "+quant[i]+'\n['+xp[i]+']')
        g_fields.append(field)

    h_embed = it.Embed( title=title,
                        description=description,
                        fields = g_fields, 
                        color=0x00ff00)
    return h_embed
###########################################################################################



@bot.event
async def on_ready():
    print(f'Logged in as {str(bot.me.name)}!')
    
@bot.command(name="ping" ,description="show bot's ping" ) #,scope=839662151010353172
async def ping(ctx:it.CommandContext):
    await ctx.send(f"Pong! {round(bot.latency)}ms")


	
    



@bot.command(
            name="calc",
            description="Calculate Resources",
            options=[
                    it.Option(
                            name="current_lv",
                            description="Your Current Lvl",
                            type=it.OptionType.STRING,
                            required=True
                            ),
                    it.Option(
                            name="target_lv",
                            description="Your tTarget Lvl",
                            type=it.OptionType.STRING,
                            required=True
                            ),
                    it.Option(
                            name="current_perc",
                            description="The % Of Your Current Lvl",
                            type=it.OptionType.STRING,
                            required=False
                            ),
                    it.Option(
                            name="target_perc",
                            description="The % Of Your Target Lvl",
                            type=it.OptionType.STRING,
                            required=False
                            ),
                    ],
            )
async def calc(ctx:it.CommandContext,current_lv,target_lv,current_perc="0",target_perc="0"):
    lvl_reg[str(ctx.author.user.username)]= {}
    lvl_reg[str(ctx.author.user.username)]["curlv"]=int(current_lv)
    lvl_reg[str(ctx.author.user.username)]["tarlv"]=int(target_lv)
    lvl_reg[str(ctx.author.user.username)]["curperc"]=float(current_perc)
    lvl_reg[str(ctx.author.user.username)]["tarperc"]=float(target_perc)
    row = ActionRow(
    components=[skills_menu]
    )

    await ctx.send("Select Skill !", components=row)

@bot.component("select_skill")
async def skills_response(ctx:it.ComponentContext,blah):
    skill_id = str(ctx.data.values[0])
    if skill_id == 'Cancel': #cancel
        await ctx.send("you canceled the interaction. \nhave a great day!", components=[])

    elif skill_id == '0': #combat
        calc_reg[str(ctx.author.user.username)]=[skill_id]
        loc_menu = MakeMenu3("Select Location !","select_location")
        row = ActionRow(
        components=[loc_menu]
        )
    
        await ctx.edit("Select Location !",components=row)

    else:#other skills
        calc_reg[str(ctx.author.user.username)]=[skill_id]
        rsc_menu = MakeMenu(skill_id,"Select Resource !","select_resource")
        row = ActionRow(
        components=[rsc_menu]
        )
        await ctx.edit("Select Resource !",components=row)

@bot.component("select_location")
async def loc_response(ctx:it.ComponentContext,blah):
    loc_id = str(ctx.data.values[0])
    if loc_id == 'Cancel' :
        await ctx.edit("You Chose To End The Interaction", components=[])
    else:
        mob_menu = MakeMenu4(int(loc_id),"Select Mob !","select_mob")
        row = ActionRow(
        components=[mob_menu]
        )
        await ctx.edit("Select Mob !", components=row)

@bot.component("select_mob")
async def mob_response(ctx:it.ComponentContext,blah):
    mob_id = str(ctx.data.values[0])
    if mob_id == 'Cancel' :
        await ctx.edit("You Chose To End The Interaction", components=[])
    else:
        boost_menu = MakeMenu2("0","Select Boost !","select_boost")
        calc_reg[str(ctx.author.user.username)].append(mob_id)
        row = ActionRow(
        components=[boost_menu]
        )
        
        await ctx.edit("Select Boost !",components=row)

@bot.component("select_resource")
async def rsc_response(ctx:it.ComponentContext,blah):
    resource_id = str(ctx.data.values[0])
    if resource_id == 'Cancel':
        await ctx.edit("You Chose To End The Interaction", components=[])
    else:
        skill_id = calc_reg[str(ctx.author.user.username)][0]
        
        boost_menu = MakeMenu2(skill_id,"Select Boost !","select_boost")
        calc_reg[str(ctx.author.user.username)].append(resource_id)
        row = ActionRow(
        components=[boost_menu]
        )
        
        await ctx.edit("Select Boost !",components=row)

@bot.component("select_boost")
async def boost_response(ctx:it.ComponentContext,blah):
    boosts_used = ctx.data.values
    if 'Cancel' in boosts_used:
        await ctx.edit("You Chose To End The Interaction", components=[])
    else:
        curLv = lvl_reg[str(ctx.author.user.username)]["curlv"]
        tarLv = lvl_reg[str(ctx.author.user.username)]["tarlv"]
        curPerc = lvl_reg[str(ctx.author.user.username)]["curperc"]
        tarPerc = lvl_reg[str(ctx.author.user.username)]["tarperc"]
        xp_needed = getxp(int(curLv),int(tarLv),float(curPerc),float(tarPerc))
        bst_used = round(getboost(boosts_used),5)
        bst_name = boost_str_emoji(boosts_used)
        choice = calc_reg[ctx.author.user.username][0]

        if choice == "0" : #combat
            mob_used = calc_reg[ctx.author.user.username][1]
            mob_emoji = mobs_emoji[mob_used]
            mob_xp = combat[mob_used]
            rsc_needed = math.ceil(xp_needed / mob_xp) + 1
            rsc_needed_boosted = math.ceil(rsc_needed / bst_used)
            result = f'Skill : <:combat_sw:880221520121700362> Combat (melee/magic)' + '\nMob : ' + mob_emoji  + f'{mob_used}' + '\nLvlUp : (' + f'{curLv}' + ')[' + f'{curPerc}' + '%] --> (' + f'{tarLv}' + ')[' + f'{tarPerc}' + '%]' + '\nBoost : ' + f'{bst_name}' + '\nQuantity Needed : ' + f'{rsc_needed_boosted:,}'
            
            await ctx.edit(result, components=[])
            
        else: #skills
            rsc_used = calc_reg[ctx.author.user.username][1]
            rsc_xp = resources[rsc_used]
            resource_emoji = rsc_emojis[rsc_used][1]
            chosen_skill = skills[int(choice)].capitalize()
            skill_emoji = skills_emoji[chosen_skill]

            rsc_needed = math.ceil(xp_needed / rsc_xp) + 1
            rsc_needed_boosted = math.ceil(rsc_needed / bst_used)

            if chosen_skill.lower() == "fishing" : #fishing
                bait_emoji = baits_emojis[rsc_used]
                result = f'Skill : {skill_emoji} ' + chosen_skill.capitalize() + f'\nFish : ' + resource_emoji + ' ' + rsc_used + f'\nBait : ' + bait_emoji + " "  + baits[rsc_used] + '\nLvlUp : (' + f'{curLv}' + ')[' + f'{curPerc}' + '%] --> (' + f'{tarLv}' + ')[' + f'{tarPerc}' + '%]' + '\nBoost : ' + bst_name + f'\nQuantity Needed {resource_emoji} : ' + f'{rsc_needed_boosted:,}'

                await ctx.edit(result, components=[])
            
            elif chosen_skill.lower() == "tailoring" :
                if rsc_used in tlr_ess:
                    book_emoji = rsc_emojis['Book'][1]
                    ess_emoji = rsc_emojis['Magic Essence'][1]
                    ess_coef = tlr_ess[rsc_used][0]
                    ess_needed = rsc_needed_boosted * ess_coef
                    rlc_used = tlr_ess[rsc_used][1]             
                    rlc_emoji = rsc_emojis[rlc_used][1]
                    result = f'Skill : {skill_emoji} ' + 'Tailoring ' + f'\nResource : ' + resource_emoji + ' ' + rsc_used + '\nLvlUp : (' + f'{curLv}' + ')[' + f'{curPerc}' + '%] --> (' + f'{tarLv}' + ')[' + f'{tarPerc}' + '%]' + '\nBoost : ' + bst_name + f'\nQuantity Needed : ' + book_emoji + '||'+ rlc_emoji + f' {rsc_needed_boosted:,}'+ f'\nEssences Needed : ' + ess_emoji + f' {ess_needed:,}'

                    await ctx.edit(result, components=[])

                elif rsc_used == 'Wand' :
                        ess_emoji = rsc_emojis['Magic Essence'][1]
                        ess_needed = rsc_needed_boosted * 15
                        logs_needed = rsc_needed_boosted * 2
                        log_emoji = '<:oak_log_ca1:922856175345754163>'
                        result = f'Skill : {skill_emoji} ' + 'Tailoring ' + f'\nResource : ' + resource_emoji + ' ' + rsc_used + '\nLvlUp : (' + f'{curLv}' + ')[' + f'{curPerc}' + '%] --> (' + f'{tarLv}' + ')[' + f'{tarPerc}' + '%]' + '\nBoost : ' + bst_name + f'\nQuantity Needed : {resource_emoji} ' + f'{rsc_needed_boosted:,}' + f'\nMagic Essences Needed : {ess_emoji} ' + f'{ess_needed:,}' + f'\nLogs Needed : ' + log_emoji  + f' {logs_needed:,}'

                        await ctx.edit(result, components=[])

                else :
                    result = f'Skill : {skill_emoji} ' + chosen_skill.capitalize() + f'\nResource : ' + resource_emoji + ' ' + rsc_used + '\nLvlUp : (' + f'{curLv}' + ')[' + f'{curPerc}' + '%] --> (' + f'{tarLv}' + ')[' + f'{tarPerc}' + '%]' + '\nBoost : ' + bst_name + f'\nQuantity Needed : {resource_emoji} ' + f'{rsc_needed_boosted:,}'

                    await ctx.edit(result, components=[])
            else :
                result = f'Skill : {skill_emoji} ' + chosen_skill.capitalize() + f'\nResource : ' + resource_emoji + ' ' + rsc_used + '\nLvlUp : (' + f'{curLv}' + ')[' + f'{curPerc}' + '%] --> (' + f'{tarLv}' + ')[' + f'{tarPerc}' + '%]' + '\nBoost : ' + bst_name + f'\nQuantity Needed : {resource_emoji} ' + f'{rsc_needed_boosted:,}'

                await ctx.edit(result, components=[])
                #counter = retrieve()
                #counter = counter + 1
                #print(counter)
                #update(counter)

    #calc_reg.pop(str(ctx.author.user.username))



@bot.command(name="invite" ,description="get bot's invite link" )
async def invite(ctx:it.CommandContext):
    await ctx.send("Sorry, currently the bot is in 100 servers and waiting for verification to be able to join more :(.")
#    e = it.Embed(title="Click The Button To Invite Me", color=0x00ff00)
#    inv_button_on = Button(
#                            style=ButtonStyle.LINK, 
#                            label="Invite Me !", 
#                            url=invite_url,
#                            disabled=False
#                            )
#
#    await ctx.send(embeds=[e],components=[inv_button_on])
#    time.sleep(10)
#    await ctx.edit("Invite Link Timed'Out",embeds=[],components=[])

@bot.command(name="help" ,description="show list of commands")
async def help(ctx:it.CommandContext):

    h_embed = it.Embed( title="Help",
                        description="Smart-boi Commands :",
                        fields = [
                                it.EmbedField(name="Calc",value="```/calc [current lvl] [target lvl] [current %](optional) [target %](optional) ```\nCalculate how much resources you need to get from your current Lvl to your targeted Lvl"),
                                it.EmbedField(name="Guide",value="```/guide```\nMake a guide for a specific skill based on your prefered boost method"),
                                it.EmbedField(name="Invite",value="```/invite```\nSend button with bot's invite link."),
                                it.EmbedField(name="Ping",value="```/ping```\nShow bot's latency."),
                                it.EmbedField(name="Help",value="```/help```\nShow this list.")
                                ], 
                        color=0x00ff00)




    await ctx.send(embeds=[h_embed])


@bot.command(name="servers" ,description="show the servers connected to" ,scope=[922854662141526037,922870521648013372,922919205429473340,869611702042378250])
async def servers(ctx:it.CommandContext):
    tech_id = 465858376182530059
    if int(ctx.author.user.id) == tech_id :

        guilds =  await bot._http.get_self_guilds()
        print(guilds)
        guilds_list = []
        for i in guilds :
            guilds_list.append(i["name"])
        gl_msg = '\n'.join(guilds_list)
        await ctx.send(f"Connected on {str(len(guilds))} servers:" + '\n' + gl_msg)
        
    else :
        await ctx.send("You don't have permissions to check this")


#@bot.command(name="test" ,description="test command" ,scope=[839662151010353172,869611702042378250])
#async def test(ctx:it.CommandContext):
#    emoji = "<:combat_sw:880221520121700362>"
#    msg = emoji + " : combat emoji"
#    await ctx.send(msg)


@bot.command(name="guide" ,description="make a guide for a specific skill with specific boost" )
async def guide(ctx:it.CommandContext):
    await ctx.send("Select Skill To Make Guide For !", components=[g_skills_menu])



@bot.component("g_select_skill")
async def skills_response(ctx:it.ComponentContext,blah):
    skill_id = str(ctx.data.values[0])
    if skill_id == 'Cancel': #cancel
        await ctx.send("you canceled the interaction. \nhave a great day!", components=[])
    else:
        g_reg[str(ctx.author.user.username)] = skill_id
        g_boost_menu = MakeMenu2(skill_id,"Select Boost !","g_select_boost")        
        await ctx.edit("Select Boost To Cast On Your Guide !",components=[g_boost_menu])
        #time.sleep(10)
        #await ctx.edit("Select Boost To Cast On Your Guide !")

@bot.component("g_select_boost")
async def boost_response(ctx:it.ComponentContext,blah):
    g_boosts_used = ctx.data.values
    skill_id = g_reg[str(ctx.author.user.username)]
    skill_boosted = skills[int(skill_id)]
    g_embed = makeguide(skill_boosted,g_boosts_used)
    await ctx.edit("Good Luck With The Grind, Skiller !!", embeds = g_embed)
    time.sleep(5)
    await ctx.edit("Good Luck With The Grind, Skiller !!", embeds = g_embed, components=[])



bot.start()
