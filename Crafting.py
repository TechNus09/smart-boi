from data import *

crafting_lvls = [
                 "Lv.1 --> Lv.5"
                ,"Lv.5 --> Lv.10"
                ,"Lv.10 --> Lv.20"
                ,"Lv.20 --> Lv.30"
                ,"Lv.30 --> Lv.40"
                ,"Lv.40 --> Lv.50"
                ,"Lv.50 --> Lv.60"
                ,"Lv.60 --> Lv.70"
                ,"Lv.70 --> Lv.75"
                ,"Lv.75 --> Lv.80"
                ,"Lv.80 --> Lv.90"
                ,"Lv.90 --> Lv.95"
                ,"Lv.95 --> Lv.100"
                ,"Lv.100 --> Lv.110"
                ,"Lv.110 --> Lv.120"
                ]
crafting_emoji = [
                rsc_emojis["Accuracy Relic"],
                rsc_emojis["Guarding Relic"],
                rsc_emojis["Healing Relic"],
                rsc_emojis["Wealth Relic"],
                rsc_emojis["Power Relic"],
                rsc_emojis["Nature Relic"],                    
                rsc_emojis["Fire Relic"],
                rsc_emojis["Damage Relic"],
                rsc_emojis["Leeching Relic"],
                rsc_emojis["Experience Relic"],
                rsc_emojis["Cursed Relic"],
                rsc_emojis["Cursed Relic"],
                rsc_emojis["Cursed Relic"],
                rsc_emojis["Cursed Relic"],
                rsc_emojis["Cursed Relic"]
                ]
crafting_xpNeeded = [
                rsc_names["lvl_1_5"],
                rsc_names["lvl_5_10"],
                rsc_names["lvl_10_20"],
                rsc_names["lvl_20_30"],
                rsc_names["lvl_30_40"],
                rsc_names["lvl_40_50"],
                rsc_names["lvl_50_60"],
                rsc_names["lvl_60_70"],
                rsc_names["lvl_70_75"],
                rsc_names["lvl_75_80"],
                rsc_names["lvl_80_90"],
                rsc_names["lvl_90_95"],
                rsc_names["lvl_95_100"],
                rsc_names["lvl_100_110"],
                rsc_names["lvl_110_120"],
                ]
crafting_m_noboost = [
                 "77"
                ,"68"
                ,"180"
                ,"325"
                ,"495"
                ,"1,039"
                ,"1,955"
                ,"3,692"
                ,"3,165"
                ,"4,790"
                ,"19,331"
                ,"25,774"
                ,"51,548"
                ,"309,284"
                ,"1,237,133"
                ]
crafting_m_50boost = [
                 "52"
                ,"46"
                ,"120"
                ,"217"
                ,"330"
                ,"693"
                ,"1,304"
                ,"2,462"
                ,"2,110"
                ,"3,194"
                ,"12,888"
                ,"17,183"
                ,"34,366"
                ,"206,190"
                ,"824,756"
                ]
crafting_a_noboost = [
                 "0"
                ,"180"
                ,"406"
                ,"721"
                ,"1,298"
                ,"1,978"
                ,"4,153"
                ,"7,818"
                ,"4,923"
                ,"6,329"
                ,"28,735"
                ,"38,313"
                ,"76,625"
                ,"459,746"
                ,"1,838,982"
                ]
crafting_a_50boost = [
                 "0"
                ,"120"
                ,"271"
                ,"481"
                ,"866"
                ,"1,319"
                ,"2,769"
                ,"5,212"
                ,"3,282"
                ,"4,220"
                ,"19,157"
                ,"25,542"
                ,"51,084"
                ,"306,498"
                ,"1,225,988"
                ]
crafting_m_name = [
                rsc_names["accuracy_relic"],
                rsc_names["guarding_relic"],
                rsc_names["healing_relic"],
                rsc_names["wealth_relic"],
                rsc_names["power_relic"],
                rsc_names["nature_relic"],
                rsc_names["fire_relic"],
                rsc_names["damage_relic"],
                rsc_names["leeching_relic"],
                rsc_names["experience_relic"],
                rsc_names["cursed_relic"],
                rsc_names["cursed_relic"],
                rsc_names["cursed_relic"],
                rsc_names["cursed_relic"],
                rsc_names["cursed_relic"],
                ]
crafting_a_name = [
                rsc_names["none"],
                rsc_names["accuracy_relic"],
                rsc_names["guarding_relic"],
                rsc_names["healing_relic"],
                rsc_names["wealth_relic"],
                rsc_names["power_relic"],
                rsc_names["nature_relic"],
                rsc_names["fire_relic"],
                rsc_names["damage_relic"],
                rsc_names["leeching_relic"],
                rsc_names["experience_relic"],
                rsc_names["experience_relic"],
                rsc_names["experience_relic"],
                rsc_names["experience_relic"],
                rsc_names["experience_relic"],
                ]



crafting_list = { 
                "lvls": crafting_lvls ,
                "emojis" : crafting_emoji , 
                "xp" : crafting_xpNeeded , 
                "m_names" : crafting_m_name , 
                "a_names" : crafting_a_name , 
                "m_boost" :  { '1.0' : crafting_m_noboost, '1.5' : crafting_m_50boost} , 
                "a_boost" :  { '1.0' : crafting_a_noboost, '1.5' : crafting_a_50boost} 
                }
