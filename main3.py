import os
from pprint import pprint
import time
import interactions as it
from interactions import CommandContext as CC, component
from interactions import ComponentContext as CPC
from interactions import Button, ButtonStyle, SelectMenu, SelectOption, ActionRow
import math
import asyncio
from interactions.ext import wait_for
from pandas import describe_option

from data import *
from Mining import *
from Smithing import *
from Woodcutting import *
from Crafting import *
from Fishing import *
from Cooking import *
from guide_adapter import *





import logging


skills_options = [
                'combat',
                'mining',
                'smithing',
                'woodcutting',
                'crafting',
                'fishing',
                'cooking',
                'tailoring'
                ]

presence = it.PresenceActivity(name="Tests", type=it.PresenceActivityType.GAME)
bot = it.Client("ODgxMTc4MzEzMTYxMzEwMjI4.Gx6wp2.r2ufEu_gLEDw2-PsNvZABA2MQYLAJM455GE-qk",presence=it.ClientPresence(activities=[presence]),disable_sync=True)
logging.basicConfig(level=logging.DEBUG)
wait_for.setup(bot, add_method=True)


calc_reg = {} #{'useid':{'xp':xp,'rows':rows:'selected':[1,2,3]}}
#####################################################################################################################
#####################################################################################################################
def make_skills_menu(PH,C_ID):
    skills_menu = it.SelectMenu(
                options= [
                    it.SelectOption(label=f'Combat (Melee/Magic)',value='combat', emoji=it.Emoji(id=962217488479834142 ,animated=False)),
                    it.SelectOption(label=f'Mining',value='mining', emoji=it.Emoji(id=962217952927698954,animated=False)),
                    it.SelectOption(label=f'Smithing',value='smithing', emoji=it.Emoji(id=945264297167175681,animated=False)),
                    it.SelectOption(label=f'Woodcutting',value='woodcutting', emoji=it.Emoji(id=962217565780865024,animated=False)),
                    it.SelectOption(label=f'Crafting',value='crafting', emoji=it.Emoji(id=922871203130134528,animated=False)),
                    it.SelectOption(label=f'Fishing',value='fishing', emoji=it.Emoji(id=962217539767771217,animated=False)),
                    it.SelectOption(label=f'Cooking',value='cooking', emoji=it.Emoji(id=962217512035053599,animated=False)),
                    it.SelectOption(label=f'Tailoring',value='tailoring', emoji=it.Emoji(id=937013045488648252,animated=False)),
                    it.SelectOption(label=f'Cancel',value='cancel',emoji=it.Emoji(id=cancel_id,animated=False))
                        ],
                    placeholder=PH,
                    custom_id=C_ID
                                )
    return skills_menu

################################-Menus-Makers########################################################
def make_rsc_menu(skill_id,PH,C_ID):
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
                                    value="cancel",
                                    emoji=it.Emoji(id=cancel_id,animated=False)._json
                                    )
                    )
    menu = it.SelectMenu(
                    options=temp_list,
                    placeholder=PH,
                    custom_id=C_ID
                        )
    return menu

def make_boost_menu(skill_id,PH,C_ID):
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
                                    value="cancel",
                                    emoji=it.Emoji(id=cancel_id,animated=False)._json
                                    )
                    )
    if str(skill_id) == '0' or skill_id == '2' :
        menu = it.SelectMenu(
                        options=temp_list,
                        placeholder=PH,
                        custom_id=C_ID,
                        min_values=1,
                        max_values=4
                            )
    elif str(skill_id) == '1':
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

def make_loc_menu(PH,C_ID):
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
                                    value="cancel",
                                    emoji=it.Emoji(id=cancel_id,animated=False)._json
                                    )
                    )
    menu = it.SelectMenu(
                    options=temp_list,
                    placeholder=PH,
                    custom_id=C_ID
                        )
    return menu

def make_mob_menu(loc_id,PH,C_ID):
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
                                    value="cancel",
                                    emoji=it.Emoji(id=cancel_id,animated=False)._json
                                    )
                    )
    menu = it.SelectMenu(
                    options=temp_list,
                    placeholder=PH,
                    custom_id=C_ID
                        )
    return menu

def defaultize(obj,ids):
    for i in range(len(obj.components[0].options)):
        if i in ids:
            obj.components[0].options[i].default = True
        else:
            obj.components[0].options[i].default = False

def get_default(obj):
    for i in range(len(obj.components[0].options)):
            if obj.components[0].options[i].default :
                return i

def get_index(ord_dict:list,item:str):
    for i in range(len(ord_dict)):
        if ord_dict[i][0] == item :
            return i

@bot.event
async def on_ready():
    print(f'Logged in as {str(bot.me.name)}!')
    
@bot.command(name="ping" ,description="show bot's ping" )
async def ping(ctx:it.CommandContext):
    await ctx.send(f"Pong! {round(bot.latency)}ms")


@bot.command(name="cascade" ,description="show menus in cascade" )
async def cascade(ctx:CC):
    await ctx.defer()
    #get_xp
    usr_id = str(ctx.author.user.id)
    skill_id = 1
    b = Button(label='Calc',style=ButtonStyle.SUCCESS,custom_id=f"calc-{usr_id}")
    c = Button(label='Close',style=ButtonStyle.DANGER,custom_id=f"close-{usr_id}")
    skills_menu = make_skills_menu("Select Skill !",f"select_skill-{usr_id}")
    rsc_menu = make_rsc_menu(skill_id,"Select Ressouce !",f"select_rsc-{usr_id}")
    bst_menu = make_boost_menu(skill_id,"Select Boost !",f"select_boost-{usr_id}")

    calc_row1 = ActionRow(components=[skills_menu])
    calc_row2 = ActionRow(components=[rsc_menu])
    calc_row3 = ActionRow(components=[bst_menu])
    calc_row4 = ActionRow(components=[b,c])
    rows =  [
            calc_row1,calc_row2,calc_row3,calc_row4
            ]  
    calc_reg[usr_id]=rows
    embed = it.Embed(title="Skill Calculator",
                    description="```Result Result```")
    await ctx.send("Select !" ,components=rows)


@bot.event(name="on_component")
async def resp(ctx:CPC):
    if ctx.custom_id.startswith("select_skill"):
        rows = calc_reg[str(ctx.member.user.id)]
        #update other menu
        #update placeholder
        skill_order = skills_options.index(ctx.data.values[0])
        u_i = str(ctx.member.user.id)
        print(u_i)
        rsc_m = make_rsc_menu(skill_order,"Select Ressouce !",f"select_rsc-{u_i}")
        bst_m = make_boost_menu(skill_order,"Select Boost !",f"select_boost-{u_i}")
        defaultize(rows[0],[skill_order])
        rows[1] = ActionRow(components=[rsc_m])
        rows[2] = ActionRow(components=[bst_m])
        print(rows)
        await ctx.edit("done",components=rows)
        for i in range(len(rows)):
            pprint(rows[i]._json)
    #enable calc button if all fields selected
    #on calc finished : freeze every thing
    if ctx.custom_id.startswith("select_rsc"):
        rows = calc_reg[str(ctx.member.user.id)]
        skill_order = get_default(rows[0])
        rsc_order = get_index(skill_rsc[skill_order],ctx.data.values[0])
        defaultize(rows[1],[rsc_order])
        await ctx.edit("done",components=rows)

    if ctx.custom_id.startswith("select_boost"):
        rows = calc_reg[str(ctx.member.user.id)]
        defaultize(rows[2],[0,1])
        await ctx.edit("done",components=rows)

    if ctx.custom_id.startswith(("close-")):
        rows = calc_reg[str(ctx.member.user.id)]
        for i in range(len(rows)-1):
            rows[i].components[0].disabled=True
        for i in range(2):
            rows[len(rows)-1].components[i].disabled=True
        await ctx.edit("done",components=rows)

    if ctx.custom_id.startswith(("calc-")):
        rows = calc_reg[str(ctx.member.user.id)]
        for i in range(len(rows)-1):
            rows[i].components[0].disabled=True
        for i in range(2):
            rows[len(rows)-1].components[i].disabled=True
        await ctx.edit("done",components=rows)




bot.start()
