from data import *



woodcutting_lvls = [
                "Lv.1 --> Lv.5"
                ,"Lv.5 --> Lv.10"
                ,"Lv.10 --> Lv.20"
                ,"Lv.20 --> Lv.30"
                ,"Lv.30 --> Lv.40"
                ,"Lv.40 --> Lv.50"
                ,"Lv.50 --> Lv.60"
                ,"Lv.60 --> Lv.70"
                ,"Lv.70 --> Lv.80"
                ,"Lv.80 --> Lv.90"
                ,"Lv.90 --> Lv.95"
                ,"Lv.95 --> Lv.100"
                ,"Lv.100 --> Lv.110"
                ,"Lv.110 --> Lv.120" 
                ]
woodcutting_emoji = [
                rsc_emojis["Pine Log"],
                rsc_emojis["Dead Log"],
                rsc_emojis["Birch Log"],
                rsc_emojis["Applewood"],
                rsc_emojis["Willow Log"],
                rsc_emojis["Oak Log"],
                rsc_emojis["Chestnut Log"],               
                rsc_emojis["Maple Log"],
                rsc_emojis["Olive Log"],
                rsc_emojis["Palm Wood"],
                rsc_emojis["Palm Wood"],
                rsc_emojis["Palm Wood"],
                rsc_emojis["Palm Wood"],
                rsc_emojis["Palm Wood"],
                rsc_emojis["Palm Wood"]
                ]
woodcutting_xpNeeded = [
                rsc_names["lvl_1_5"],
                rsc_names["lvl_5_10"],
                rsc_names["lvl_10_20"],
                rsc_names["lvl_20_30"],
                rsc_names["lvl_30_40"],
                rsc_names["lvl_40_50"],
                rsc_names["lvl_50_60"],
                rsc_names["lvl_60_70"],
                rsc_names["lvl_70_80"],
                rsc_names["lvl_80_90"],
                rsc_names["lvl_90_95"],
                rsc_names["lvl_95_100"],
                rsc_names["lvl_100_110"],
                rsc_names["lvl_110_120"],
                ]
woodcutting_m_noboost = [
                "23"
                ,"27"
                ,"65"
                ,"113"
                ,"149"
                ,"438"
                ,"1,278"
                ,"2,769"
                ,"7,384"
                ,"20,446"
                ,"27,261"
                ,"54,522"
                ,"327,127"
                ,"1,308,506"
                ]
woodcutting_m_50boost = [
                "16"
                ,"18"
                ,"44"
                ,"76"
                ,"100"
                ,"292"
                ,"852"
                ,"1,846"
                ,"4,923"
                ,"13,631"
                ,"18,174"
                ,"36,348"
                ,"218,085"
                ,"872,338"
                ]
woodcutting_a_noboost = [
                "0"
                ,"54"
                ,"162"
                ,"260"
                ,"452"
                ,"594"
                ,"1,749"
                ,"5,112"
                ,"11,075"
                ,"29,533"
                ,"39,377"
                ,"78,753"
                ,"472,517"
                ,"1,890,065"
                ]
woodcutting_a_50boost = [
                "0"
                ,"36"
                ,"108"
                ,"173"
                ,"302"
                ,"396"
                ,"1,167"
                ,"3,408"
                ,"7,384"
                ,"19,689"
                ,"26,252"
                ,"52,502"
                ,"315,011"
                ,"1,260,043"
                ]
woodcutting_m_name = [
                rsc_names["pine_log"],
                rsc_names["dead_log"],
                rsc_names["birch_log"],
                rsc_names["apple_wood"],
                rsc_names["willow_log"],
                rsc_names["oak_log"],
                rsc_names["chestnut_log"],
                rsc_names["maple_log"],
                rsc_names["olive_log"],
                rsc_names["palm_wood"],
                rsc_names["palm_wood"],
                rsc_names["palm_wood"],
                rsc_names["palm_wood"],
                rsc_names["palm_wood"],
                ]
woodcutting_a_name = [
                rsc_names["none"],
                rsc_names["dead_log"],
                rsc_names["birch_log"],
                rsc_names["apple_wood"],
                rsc_names["willow_log"],
                rsc_names["oak_log"],
                rsc_names["chestnut_log"],
                rsc_names["maple_log"],
                rsc_names["olive_log"],
                rsc_names["olive_log"],
                rsc_names["olive_log"],
                rsc_names["olive_log"],
                rsc_names["olive_log"],
                rsc_names["olive_log"],
                ]


woodcutting_main_list = [woodcutting_lvls,woodcutting_emoji,woodcutting_xpNeeded,woodcutting_m_name,woodcutting_m_noboost,woodcutting_m_50boost]
woodcutting_alt_list = [woodcutting_lvls,woodcutting_emoji,woodcutting_xpNeeded,woodcutting_a_name,woodcutting_a_noboost,woodcutting_a_50boost]


woodcutting_list = { 
                "lvls": woodcutting_lvls ,
                "emojis" : woodcutting_emoji , 
                "xp" : woodcutting_xpNeeded , 
                "m_names" : woodcutting_m_name , 
                "a_names" : woodcutting_a_name , 
                "m_boost" :  { '1.0' : woodcutting_m_noboost, '1.5' : woodcutting_m_50boost} , 
                "a_boost" :  { '1.0' : woodcutting_a_noboost, '1.5' : woodcutting_a_50boost} 
                }