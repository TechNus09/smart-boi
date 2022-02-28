from data import *

cooking_lvls = [
                 "Lv.1 --> Lv.10"
                ,"Lv.10 --> Lv.20"
                ,"Lv.20 --> Lv.30"
                ,"Lv.30 --> Lv.40"
                ,"Lv.40 --> Lv.45"
                ,"Lv.45 --> Lv.50"
                ,"Lv.50 --> Lv.60"
                ,"Lv.60 --> Lv.70"
                ,"Lv.70 --> Lv.75"
                ,"Lv.75 --> Lv.80"
                ,"Lv.80 --> Lv.85"
                ,"Lv.85 --> Lv.90"
                ,"Lv.90 --> Lv.95"
                ,"Lv.95 --> Lv.100"
                ,"Lv.100 --> Lv.110"
                ,"Lv.110 --> Lv.120" 
                ]
cooking_emoji = [
                rsc_emojis["Cooked Anchovies"],
                rsc_emojis["Cooked Mackerel"],
                rsc_emojis["Cooked Squid"],
                rsc_emojis["Cooked Sardine"],
                rsc_emojis["Cooked Eel"],
                rsc_emojis["Cooked Anglerfish"],
                rsc_emojis["Cooked Trout"],
                rsc_emojis["Cooked Bass"],
                rsc_emojis["Cooked Tuna"],
                rsc_emojis["Cooked Lobster"],
                rsc_emojis["Cooked Sea Turtle"],
                rsc_emojis["Cooked Manta Ray"],
                rsc_emojis["Cooked Shark"],
                rsc_emojis["Cooked Orca"],
                rsc_emojis["Cooked Giant Squid"],
                rsc_emojis["Cooked Giant Squid"]
                ]
cooking_xpNeeded = [
                rsc_names["lvl_1_10"],
                rsc_names["lvl_10_20"],
                rsc_names["lvl_20_30"],
                rsc_names["lvl_30_40"],
                rsc_names["lvl_40_45"],
                rsc_names["lvl_45_50"],
                rsc_names["lvl_50_60"],
                rsc_names["lvl_60_70"],
                rsc_names["lvl_70_75"],
                rsc_names["lvl_75_80"],
                rsc_names["lvl_80_85"],
                rsc_names["lvl_85_90"],
                rsc_names["lvl_90_95"],
                rsc_names["lvl_95_100"],
                rsc_names["lvl_100_110"],
                rsc_names["lvl_110_120"],
                ]
cooking_m_noboost = [
                 "77"
                ,"65"
                ,"113"
                ,"139"
                ,"139"
                ,"222"
                ,"1,108"
                ,"2,462"
                ,"2,215"
                ,"2,532"
                ,"2,727"
                ,"3,731"
                ,"5,251"
                ,"6,301"
                ,"20,495"
                ,"81,979"
                ]
cooking_m_50boost = [
                 "52"
                ,"44"
                ,"76"
                ,"93"
                ,"93"
                ,"148"
                ,"739"
                ,"1,641"
                ,"1,477"
                ,"1,688"
                ,"1,818"
                ,"2,487"
                ,"3,501"
                ,"4,201"
                ,"13,664"
                ,"54,653"
                ]
cooking_a_noboost = [
                 "0"
                ,"324"
                ,"260"
                ,"452"
                ,"185"
                ,"277"
                ,"1,329"
                ,"4,430"
                ,"3,282"
                ,"4,430"
                ,"5,063"
                ,"5,453"
                ,"7,461"
                ,"10,501"
                ,"37,802"
                ,"151,206"
                ]
cooking_a_50boost = [
                 "0"
                ,"216"
                ,"174"
                ,"302"
                ,"124"
                ,"185"
                ,"886"
                ,"2,954"
                ,"2,188"
                ,"2,954"
                ,"3,376"
                ,"3,635"
                ,"4,974"
                ,"7,001"
                ,"25,201"
                ,"100,804"
                ]
cooking_m_name = [
                rsc_names["cooked_anchovies"],
                rsc_names["cooked_mackerel"],
                rsc_names["cooked_squid"],
                rsc_names["cooked_sardine"],
                rsc_names["cooked_eel"],
                rsc_names["cooked_anglerfish"],
                rsc_names["cooked_trout"],
                rsc_names["cooked_bass"],
                rsc_names["cooked_tuna"],
                rsc_names["cooked_lobster"],
                rsc_names["cooked_sea_turtle"],
                rsc_names["cooked_manta_ray"],
                rsc_names["cooked_shark"],
                rsc_names["cooked_orca"],
                rsc_names["cooked_giant_squid"],
                rsc_names["cooked_giant_squid"],
                ]
cooking_a_name = [
                rsc_names["none"],
                rsc_names["cooked_anchovies"],
                rsc_names["cooked_mackerel"],
                rsc_names["cooked_squid"],
                rsc_names["cooked_sardine"],
                rsc_names["cooked_eel"],
                rsc_names["cooked_anglerfish"],
                rsc_names["cooked_trout"],
                rsc_names["cooked_bass"],
                rsc_names["cooked_tuna"],
                rsc_names["cooked_lobster"],
                rsc_names["cooked_sea_turtle"],
                rsc_names["cooked_manta_ray"],
                rsc_names["cooked_shark"],
                rsc_names["cooked_orca"],
                rsc_names["cooked_orca"],
                ]




cooking_list = { 
                "lvls": cooking_lvls ,
                "emojis" : cooking_emoji , 
                "xp" : cooking_xpNeeded , 
                "m_names" : cooking_m_name , 
                "a_names" : cooking_a_name , 
                "m_boost" :  { '1.0' : cooking_m_noboost, '1.5' : cooking_m_50boost} , 
                "a_boost" :  { '1.0' : cooking_a_noboost, '1.5' : cooking_a_50boost} 
                }



