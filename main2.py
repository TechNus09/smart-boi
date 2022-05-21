import os
import time
import interactions as it
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC
from interactions import Button, ButtonStyle, SelectMenu, SelectOption, ActionRow
import math
import asyncio
from interactions.ext import wait_for

from data import *
from Mining import *
from Smithing import *
from Woodcutting import *
from Crafting import *
from Fishing import *
from Cooking import *
from guide_adapter import *


import logging



presence = it.PresenceActivity(name="Tests", type=it.PresenceActivityType.GAME)
bot = it.Client("ODgxMTc4MzEzMTYxMzEwMjI4.Gx6wp2.r2ufEu_gLEDw2-PsNvZABA2MQYLAJM455GE-qk",presence=it.ClientPresence(activities=[presence]),disable_sync=True)

wait_for.setup(bot, add_method=True)

#####################################################################################################################
#####################################################################################################################

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
	            placeholder="Select Skill !",
	            custom_id="select_skill"
	                        )

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



@bot.event
async def on_ready():
    print(f'Logged in as {str(bot.me.name)}!')
    
@bot.command(name="ping" ,description="show bot's ping" )
async def ping(ctx:it.CommandContext):
    await ctx.send(f"Pong! {round(bot.latency)}ms")


@bot.command(name="cascade" ,description="show menus in cascade" )
async def cascade(ctx:CC):
    await ctx.defer()
    await ctx.send("Select Skill !", components=[skills_menu])

    async def check(comp_ctx):
        if int(comp_ctx.author.user.id) == int(ctx.author.user.id):
            return True
        await ctx.send("I wasn't asking you!", ephemeral=True)
        return False

    try:
        skills_ctx: CPC = await bot.wait_for_component(
            components=skills_menu, check=check, timeout=120
        )
    except asyncio.TimeoutError:
        return await ctx.edit("You didn't choose anything :(",components=[])
    else:
        skill_choice = skills_ctx.data.values[0]
        if skill_choice == "cancel":
            await ctx.edit("You canceled the operation.",components=[])
        elif skill_choice == "combat":
            loc_menu = make_loc_menu("Select Mob Location !","select_loc")
            await ctx.edit("Select Mob Location !",components=[loc_menu])
            try:
                loc_ctx: CPC = await bot.wait_for_component(
                    components=loc_menu, check=check, timeout=120
                )
            except asyncio.TimeoutError:
                return await ctx.edit("You didn't choose anything :(",components=[])
            else:
                loc_choice = loc_ctx.data.values[0]
                if loc_choice == "cancel":
                    await ctx.edit("You canceled the operation.",components=[])
                else:
                    mob_menu = make_mob_menu(int(loc_choice),"Select Mob !","select_mob")
                    await ctx.edit("Select Mob !",components=[mob_menu])
                    try:
                        mob_ctx: CPC = await bot.wait_for_component(
                            components=mob_menu, check=check, timeout=120
                        )
                    except asyncio.TimeoutError:
                        return await ctx.edit("You didn't choose anything :(",components=[])
                    else:
                        mob_choice = mob_ctx.data.values[0]
                        if mob_choice == "cancel":
                            await ctx.edit("You canceled the operation.",components=[])
                        else:
                            await ctx.edit(f"you chose {mob_choice} ",components=[])






bot.start()
