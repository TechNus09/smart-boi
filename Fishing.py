from data import *

fishing_lvls = [
                "Lv.1 --> Lv.5"
                ,"Lv.5 --> Lv.10"
                ,"Lv.10 --> Lv.20"
                ,"Lv.20 --> Lv.30"
                ,"Lv.30 --> Lv.40"
                ,"Lv.40 --> Lv.45"
                ,"Lv.45 --> Lv.50"
                ,"Lv.50 --> Lv.55"
                ,"Lv.55 --> Lv.60"
                ,"Lv.60 --> Lv.65"
                ,"Lv.65 --> Lv.70"
                ,"Lv.70 --> Lv.75"
                ,"Lv.75 --> Lv.80"
                ,"Lv.80 --> Lv.85"
                ,"Lv.85 --> Lv.90"
                ,"Lv.90 --> Lv.95"
                ,"Lv.95 --> Lv.100"
                ,"Lv.100 --> Lv.110"
                ,"Lv.110 --> Lv.120" 
                ]


fishing_emoji = [
                rsc_emojis["Anchovies"],
                rsc_emojis["Anchovies+Goldfish"],
                rsc_emojis["Mackerel"],
                rsc_emojis["Squid"],
                rsc_emojis["Sardine"],
                rsc_emojis["Eel"],
                rsc_emojis["Anglerfish"],
                rsc_emojis["Trout"],
                rsc_emojis["Trout+Jellyfish"],
                rsc_emojis["Bass"],
                rsc_emojis["Bass+Herringbone"],
                rsc_emojis["Tuna"],
                rsc_emojis["Lobster"],
                rsc_emojis["Lobster+SeaTurtle"],         
                rsc_emojis["Manta Ray"],
                rsc_emojis["Shark"],
                rsc_emojis["Shark+Orca"],
                rsc_emojis["Shark+Orca+GiantSquid"],
                rsc_emojis["Shark+Orca+GiantSquid"]
                ]
fishing_xpNeeded = [
                rsc_names["lvl_1_5"],
                rsc_names["lvl_5_10"],
                rsc_names["lvl_10_20"],
                rsc_names["lvl_20_30"],
                rsc_names["lvl_30_40"],
                rsc_names["lvl_40_45"],
                rsc_names["lvl_45_50"],
                rsc_names["lvl_50_55"],
                rsc_names["lvl_55_60"],
                rsc_names["lvl_60_65"],
                rsc_names["lvl_65_70"],
                rsc_names["lvl_70_75"],
                rsc_names["lvl_75_80"],
                rsc_names["lvl_80_85"],
                rsc_names["lvl_85_90"],
                rsc_names["lvl_90_95"],
                rsc_names["lvl_95_100"],
                rsc_names["lvl_100_110"],
                rsc_names["lvl_110_120"],
                ]
fishing_m_noboost = [
                 "23"
                ,"36"
                ,"65"
                ,"113"
                ,"139"
                ,"139"
                ,"222"
                ,"370"
                ,"672"
                ,"821"
                ,"1,453"
                ,"2,215"
                ,"2,532"
                ,"3,544"
                ,"3,731"
                ,"4,889"
                ,"6,444"
                ,"25,774"
                ,"103,095"
                ]
fishing_m_50boost = [
                 "16"
                ,"24"
                ,"44"
                ,"76"
                ,"93"
                ,"93"
                ,"148"
                ,"247"
                ,"448"
                ,"547"
                ,"969"
                ,"1,477"
                ,"1,688"
                ,"2,366"
                ,"2,487"
                ,"3,259"
                ,"4,296"
                ,"17,183"
                ,"68,727"
                ]
fishing_a_noboost = [
                 "0"
                ,"0"
                ,"217"
                ,"260"
                ,"452"
                ,"185"
                ,"277"
                ,"443"
                ,"886"
                ,"1,343"
                ,"2,685"
                ,"2,905"
                ,"4,430"
                ,"8,860"
                ,"7,088"
                ,"7,461"
                ,"14,922"
                ,"89,530"
                ,"358,118"
                ]
fishing_a_50boost = [
                 "0"
                ,"0"
                ,"145"
                ,"173"
                ,"301"
                ,"124"
                ,"185"
                ,"296"
                ,"591"
                ,"895"
                ,"1,790"
                ,"1,937"
                ,"2,954"
                ,"5,907"
                ,"4,726"
                ,"4,974"
                ,"9,948"
                ,"59,687"
                ,"238,745"
                ]
fishing_m_name = [
                rsc_names["anchovies"],
                rsc_names["anchovies_goldfish"],
                rsc_names["mackerel"],
                rsc_names["squid"],
                rsc_names["sardine"],
                rsc_names["eel"],
                rsc_names["anglerfish"],
                rsc_names["trout"],
                rsc_names["trout_jelly"],
                rsc_names["bass"],
                rsc_names["bass_bones"],
                rsc_names["tuna"],
                rsc_names["lobster"],
                rsc_names["lobster_sea_turtle"],
                rsc_names["manta_ray"],
                rsc_names["shark"],
                rsc_names["shark_orca"],
                rsc_names["shark_orca_giant_squid"],
                rsc_names["shark_orca_giant_squid"],
                ]
        
fishing_a_name = [
                rsc_names["none"],
                rsc_names["none"],
                rsc_names["anchovies_goldfish"],
                rsc_names["mackerel"],
                rsc_names["squid"],
                rsc_names["sardine"],
                rsc_names["eel"],
                rsc_names["anglerfish"],
                rsc_names["anglerfish"],
                rsc_names["trout_jelly"],
                rsc_names["trout_jelly"],
                rsc_names["bass_bones"],
                rsc_names["tuna"],
                rsc_names["tuna"],
                rsc_names["lobster_sea_turtle"],
                rsc_names["manta_ray"],
                rsc_names["manta_ray"],
                rsc_names["manta_ray"],
                rsc_names["manta_ray"],
                ]


fishing_list = { 
                "lvls": fishing_lvls ,
                "emojis" : fishing_emoji , 
                "xp" : fishing_xpNeeded , 
                "m_names" : fishing_m_name , 
                "a_names" : fishing_a_name , 
                "m_boost" :  { '1.0' : fishing_m_noboost, '1.5' : fishing_m_50boost} , 
                "a_boost" :  { '1.0' : fishing_a_noboost, '1.5' : fishing_a_50boost} 
                }