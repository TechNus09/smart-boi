from data import *

smithing_lvls = [
                 "Lv.1 --> Lv.10"
                ,"Lv.10 --> Lv.20"
                ,"Lv.20 --> Lv.30"
                ,"Lv.30 --> Lv.35"
                ,"Lv.35 --> Lv.40"
                ,"Lv.40 --> Lv.45"
                ,"Lv.45 --> Lv.60"
                ,"Lv.60 --> Lv.65"
                ,"Lv.65 --> Lv.70"
                ,"Lv.70 --> Lv.80"
                ,"Lv.80 --> Lv.85"
                ,"Lv.85 --> Lv.90"
                ,"Lv.90 --> Lv.95"
                ,"Lv.95 --> Lv.100"
                ,"Lv.100 --> Lv.110"
                ,"Lv.110 --> Lv.120" 
                ]
smithing_emoji = [
                rsc_emojis["Bronze Bar"],                     
                rsc_emojis["Iron Bar"],
                rsc_emojis["Steel Bar"],
                rsc_emojis["Crimsteel Bar"],
                rsc_emojis["Silver Bar"],
                rsc_emojis["Gold Bar"],
                rsc_emojis["Mythan Bar"],
                rsc_emojis["Cobalt Bar"],
                rsc_emojis["Cobalt Bar"],
                rsc_emojis["Varaxite Bar"],
                rsc_emojis["Varaxite Bar"],
                rsc_emojis["Varaxite Bar"],
                rsc_emojis["Varaxite Bar"],
                rsc_emojis["Varaxite Bar"],
                rsc_emojis["Varaxite Bar"],
                rsc_emojis["Varaxite Bar"]
                ]
smithing_xpNeeded = [
                rsc_names["lvl_1_10"],
                rsc_names["lvl_10_20"],
                rsc_names["lvl_20_30"],
                rsc_names["lvl_30_35"],
                rsc_names["lvl_35_40"],
                rsc_names["lvl_40_45"],
                rsc_names["lvl_45_60"],
                rsc_names["lvl_60_65"],
                rsc_names["lvl_65_70"],
                rsc_names["lvl_70_80"],
                rsc_names["lvl_80_85"],
                rsc_names["lvl_85_90"],
                rsc_names["lvl_90_95"],
                rsc_names["lvl_95_100"],
                rsc_names["lvl_100_110"],
                rsc_names["lvl_110_120"],
                ]

smithing_m_name = [
                 rsc_names["bronze_bar"],
                rsc_names["iron_bar"],
                rsc_names["steel_bar"],
                rsc_names["crimsteel_bar"],
                rsc_names["silver_bar"],
                rsc_names["gold_bar"],
                rsc_names["mythan_bar"],
                rsc_names["cobalt_bar"],
                rsc_names["varaxite_bar"],
                rsc_names["varaxite_bar"],
                rsc_names["varaxite_bar"],
                rsc_names["varaxite_bar"],
                rsc_names["varaxite_bar"],
                rsc_names["varaxite_bar"],
                rsc_names["varaxite_bar"],
                rsc_names["varaxite_bar"],
                ]
smithing_m_noboost = [
                 "154"
                ,"232"
                ,"649"
                ,"134"
                ,"34"
                ,"4"
                ,"108"
                ,"74"
                ,"148"
                ,"665"
                ,"886"
                ,"1,772"
                ,"3,544"
                ,"7,088"
                ,"42,527"
                ,"170,106"
                ]
smithing_m_4boost = [
                 "149"
                ,"224"
                ,"625"
                ,"129"
                ,"33"
                ,"4"
                ,"104"
                ,"72"
                ,"143"
                ,"640"
                ,"852"
                ,"1,704"
                ,"3,408"
                ,"6,816"
                ,"40,892"
                ,"163,564"
                ]
smithing_m_8boost = [
                 "143"
                ,"215"
                ,"601"
                ,"124"
                ,"32"
                ,"4"
                ,"100"
                ,"69"
                ,"137"
                ,"615"
                ,"820"
                ,"1,639"
                ,"3,277"
                ,"6,554"
                ,"39,319"
                ,"157,273"
                ]
smithing_m_50boost = [
                 "103"
                ,"155"
                ,"433"
                ,"90"
                ,"23"
                ,"3"
                ,"72"
                ,"50"
                ,"99"
                ,"444"
                ,"591"
                ,"1,182"
                ,"2,363"
                ,"4,726"
                ,"28,352"
                ,"113,404"
                ]
smithing_m_54boost = [
                 "99"
                ,"149"
                ,"417"
                ,"86"
                ,"22"
                ,"3"
                ,"70"
                ,"48"
                ,"95"
                ,"427"
                ,"568"
                ,"1,136"
                ,"2,272"
                ,"4,544"
                ,"27,261"
                ,"109,043"
                ]
smithing_m_58boost = [
                 "95"
                ,"143"
                ,"401"
                ,"83"
                ,"21"
                ,"3"
                ,"67"
                ,"46"
                ,"92"
                ,"410"
                ,"547"
                ,"1,093"
                ,"2,185"
                ,"4,369"
                ,"26,213"
                ,"104,849"
                ]

smithing_a_name = [
                 rsc_names["none"],
                rsc_names["bronze_bar"],
                rsc_names["iron_bar"],
                rsc_names["steel_bar"],
                rsc_names["crimsteel_bar"],
                rsc_names["silver_bar"],
                rsc_names["gold_bar"],
                rsc_names["mythan_bar"],
                rsc_names["cobalt_bar"],
                rsc_names["cobalt_bar"],
                rsc_names["cobalt_bar"],
                rsc_names["cobalt_bar"],
                rsc_names["cobalt_bar"],
                rsc_names["cobalt_bar"],
                rsc_names["cobalt_bar"],
                rsc_names["cobalt_bar"],
                ]
smithing_a_noboost = [
                 "0"
                ,"648"
                ,"927"
                ,"866"
                ,"267"
                ,"68"
                ,"49"
                ,"222"
                ,"443"
                ,"886"
                ,"1,182"
                ,"2,363"
                ,"4,726"
                ,"9,451"
                ,"56,702"
                ,"226,808"
                ]
smithing_a_4boost = [
                 "0"
                ,"624"
                ,"892"
                ,"833"
                ,"257"
                ,"66"
                ,"48"
                ,"214"
                ,"426"
                ,"852"
                ,"1,137"
                ,"2,273"
                ,"4,545"
                ,"9,088"
                ,"54,522"
                ,"218,085"
                ]
smithing_a_8boost = [
                 "0"
                ,"600"
                ,"858"
                ,"801"
                ,"247"
                ,"63"
                ,"46"
                ,"206"
                ,"410"
                ,"820"
                ,"1,093"
                ,"2,185"
                ,"4,370"
                ,"8,738"
                ,"52,425"
                ,"209,697"
                ]
smithing_a_50boost = [
                "0"
                ,"432"
                ,"618"
                ,"578"
                ,"178"
                ,"46"
                ,"33"
                ,"148"
                ,"296"
                ,"591"
                ,"788"
                ,"1,576"
                ,"3,151"
                ,"6,301"
                ,"37,802"
                ,"151,206"
                ]
smithing_a_54boost = [
                 "0"
                ,"416"
                ,"595"
                ,"556"
                ,"172"
                ,"44"
                ,"32"
                ,"143"
                ,"284"
                ,"568"
                ,"758"
                ,"1,515"
                ,"3,030"
                ,"6,059"
                ,"36,348"
                ,"145,390"
                ]
smithing_a_58boost = [
                 "0"
                ,"400"
                ,"572"
                ,"534"
                ,"165"
                ,"42"
                ,"31"
                ,"137"
                ,"274"
                ,"547"
                ,"729"
                ,"1,457"
                ,"2,913"
                ,"5,826"
                ,"34,950"
                ,"139,798"
                ]




####################make emojis for alt_resources






smithing_list = { 
                "lvls": smithing_lvls ,
                "xp" : smithing_xpNeeded , 
                "emojis" : smithing_emoji , 
                "m_names" : smithing_m_name , 
                "a_names" : smithing_a_name , 
                "m_boost" :  { '1.0' : smithing_m_noboost, '1.04' : smithing_m_4boost, '1.0816' : smithing_m_8boost, '1.5' : smithing_m_50boost, '1.56' : smithing_m_54boost, '1.6224' : smithing_m_58boost} , 
                "a_boost" :  { '1.0' : smithing_a_noboost, '1.04' : smithing_a_4boost, '1.0816' : smithing_a_8boost, '1.5' : smithing_a_50boost, '1.56' : smithing_a_54boost, '1.6224' : smithing_a_58boost} 
                }