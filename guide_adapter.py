from Mining import *
from Smithing import *
from Woodcutting import *
from Crafting import *
from Fishing import *
from Cooking import *
from data import *





rsc_names = {
    "lvl_1_5":"XP: 229",
    "lvl_5_10":"XP: 539",
    "lvl_1_10":"XP: 768",
    "lvl_10_15":"XP: 1,079",
    "lvl_10_20":"XP: 3,240",
    "lvl_15_20":"XP: 2,161",
    "lvl_20_25":"XP: 4,324",
    "lvl_20_30":"XP: 12,974",
    "lvl_25_30":"XP: 8,650",
    "lvl_30_35":"XP: 17,303",
    "lvl_30_40":"XP: 51,910",
    "lvl_35_40":"XP: 34,607",
    "lvl_40_45":"XP: 69,214",
    "lvl_40_50":"XP: 207,644",
    "lvl_45_50":"XP: 138,430",
    "lvl_45_60":"XP: 969,022",
    "lvl_50_55":"XP: 276,864",
    "lvl_50_60":"XP: 830,592",
    "lvl_55_60":"XP: 553,728",
    "lvl_60_65":"XP: 1,107,458",
    "lvl_65_70":"XP: 2,214,917",
    "lvl_60_70":"XP: 3,322,375",
    "lvl_70_75":"XP: 4,429,836",
    "lvl_70_80":"XP: 13,289,511",
    "lvl_75_80":"XP: 8,859,675",
    "lvl_80_85":"XP: 17,719,350",
    "lvl_80_90":"XP: 53,158,050",
    "lvl_85_90":"XP: 35,438,700",
    "lvl_90_95":"XP: 70,877,402",
    "lvl_90_100":"XP: 212,632,207",
    "lvl_95_100":"XP: 141,754,805",
    "lvl_100_110":"XP: 850,528,841",
    "lvl_110_120":"XP: 3,402,115,380",
    
    
    "none":"-none-",
    "pine_log":"Pine Log",
    "dead_log":"Dead Log",
    "birch_log":"Birch Log",
    "apple_wood":"Applewood",
    "willow_log":"Willow Log",
    "oak_log":"Oak Log",
    "chestnut_log":"Chestnut Log",
    "maple_log":"Maple Log",
    "olive_log":"Olive Log",
    "palm_wood":"Palm Wood",
    "magic_log":"Magic Log",
    
    "accuracy_relic":"Accuracy Relic",
    "guarding_relic":"Guarding Relic",
    "healing_relic":"Healing Relic",
    "wealth_relic":"Wealth Relic",
    "power_relic":"Power Relic",
    "nature_relic":"Nature Relic",
    "fire_relic":"Fire Relic",
    "damage_relic":"Damage Relic",
    "leeching_relic":"Leeching Relic",
    "experience_relic":"Experience Relic",
    "cursed_relic":"Cursed Relic",
    "ice_relic":"Ice Relic",
    
    "anchovies":"Anchovies",
    "anchovies_goldfish":"Anchovies+Goldfish",
    "mackerel":"Mackerel",
    "squid":"Squid",
    "sardine":"Sardine",
    "eel":"Eel",
    "anglerfish":"Anglerfish",
    "trout":"Trout",
    "trout_jelly":"Trout+Jellyfish",
    "bass":"Bass",
    "bass_bones":"Bass+Herringbone",
    "tuna":"Tuna",
    "lobster":"Lobster",
    "lobster_sea_turtle":"Lobster+Sea Turtle",
    "manta_ray":"Manta Ray",
    "shark":"Shark",
    "shark_orca":"Shark+Orca",
    "orca":"Orca",
    "giant_squid":"Giant Squid",
    "shark_orca_giant_squid":"Shark+Orca+Giant Squid",
    
    "cooked_anchovies":"Cooked Anchovies",
    "cooked_mackerel":"Cooked Mackerel",
    "cooked_squid":"Cooked Squid",
    "cooked_sardine":"Cooked Sardine",
    "cooked_eel":"Cooked Eel",
    "cooked_anglerfish":"Cooked Anglerfish",
    "cooked_trout":"Cooked Trout",
    "cooked_bass":"Cooked Bass",
    "cooked_tuna":"Cooked Tuna",
    "cooked_lobster":"Cooked Lobster",
    "cooked_sea_turtle":"Cooked Sea Turtle",
    "cooked_manta_ray":"Cooked Manta Ray",
    "cooked_shark":"Cooked Shark",
    "cooked_orca":"Cooked Orca",
    "cooked_giant_squid":"Cooked Giant Squid",
    
    "tin_ore":"Tin Ore",
    "iron_ore":"Iron Ore",
    "salt":"Salt",
    "coal":"Coal",
    "silver_ore":"Silver Ore",
    "crimsteel_ore":"Crimsteel Ore",
    "gold_ore":"Gold Ore",
    "pink_salt":"Pink Salt",
    "mythan_ore":"Mythan Ore",
    "sandstone":"Sandstone",
    "cobalt_ore":"Cobalt Ore",
    "varaxium":"Varaxium",
    "black_salt":"Black Salt",
    "magic_ore":"Magic Ore",
    
    "bronze_bar":"Bronze Bar",
    "iron_bar":"Iron Bar",
    "steel_bar":"Steel Bar",
    "crimsteel_bar":"Crimsteel Bar",
    "silver_bar":"Silver Bar",
    "gold_bar":"Gold Bar",
    "mythan_bar":"Mythan Bar",
    "cobalt_bar":"Cobalt Bar",
    "varaxite_bar":"Varaxite Bar",
    "magic_bar":"Magic Bar"
    }







