from typing import Dict, Set, Tuple, NamedTuple, Optional, List, TYPE_CHECKING
from BaseClasses import ItemClassification
from .constants.item_groups import *
from .constants.jobs import *
from .constants.keys import *
from .constants.key_items import *
from .constants.maps import *
from .constants.mounts import *
from .constants.scholar_abilities import *
from .constants.summons import *
from .constants.teleport_stones import *
from .constants.region_passes import *
from .constants.display_regions import *

job_index_offset = 1
item_index_offset = 101
equipment_index_offset = 1001
summon_index_offset = 10001
scholar_index_offset = 100001
trap_index_offset = 1000001

class ItemData(NamedTuple):
    name: str
    category: str
    code: int
    classification: ItemClassification
    amount: Optional[int] = 1

region_equipment: Dict[str, List[ItemData]] = {
    MENU_DISPLAY_NAME: [],
    SPAWNING_MEADOWS_DISPLAY_NAME: [
        ItemData("Equipment - Burglars Glove", EQUIPMENT, 53 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Cedar Staff", EQUIPMENT, 62 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Cedar Wand", EQUIPMENT, 13 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Cleaver", EQUIPMENT, 2 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Stabbers", EQUIPMENT, 63 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Stout Shield", EQUIPMENT, 45 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Squirrel Dung", EQUIPMENT, 85 + equipment_index_offset, ItemClassification.useful),
    ],
    DELENDE_DISPLAY_NAME: [
        ItemData("Equipment - Fervor Charm", EQUIPMENT, 48 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Bone Smasher", EQUIPMENT, 14 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Aggro Band", EQUIPMENT, 505 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Cinquedea", EQUIPMENT, 393 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Scope Bit", EQUIPMENT, 226 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Red Hairpin", EQUIPMENT, 247 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Bracer", EQUIPMENT, 70 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Chartreuse", EQUIPMENT, 403 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Cotton Hood", EQUIPMENT, 32 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Earring", EQUIPMENT, 79 + equipment_index_offset, ItemClassification.useful, 2),
        ItemData("Equipment - Looters Ring", EQUIPMENT, 54 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Mages Robe", EQUIPMENT, 21 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Protect Amulet", EQUIPMENT, 49 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Iron Sword", EQUIPMENT, 11 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Storm Hood", EQUIPMENT, 76 + equipment_index_offset, ItemClassification.useful),
    ]
}

region_items: Dict[str, List[ItemData]] = {
    MENU_DISPLAY_NAME: [
        ItemData(WARRIOR_JOB, JOB, 0 + job_index_offset, ItemClassification.progression),
        ItemData(MONK_JOB, JOB, 5 + job_index_offset, ItemClassification.progression),
        ItemData(ROGUE_JOB, JOB, 2 + job_index_offset, ItemClassification.progression),
        ItemData(CLERIC_JOB, JOB, 4 + job_index_offset, ItemClassification.progression),
        ItemData(WIZARD_JOB, JOB, 3 + job_index_offset, ItemClassification.progression),
        ItemData(WARLOCK_JOB, JOB, 14 + job_index_offset, ItemClassification.progression),
        ItemData(FENCER_JOB, JOB, 1 + job_index_offset, ItemClassification.progression),
        ItemData(SHAMAN_JOB, JOB, 8 + job_index_offset, ItemClassification.progression),
        ItemData(SCHOLAR_JOB, JOB, 13 + job_index_offset, ItemClassification.progression),  # requirement for Grans subbasement
        ItemData(AEGIS_JOB, JOB, 10 + job_index_offset, ItemClassification.progression),
        ItemData(HUNTER_JOB, JOB, 7 + job_index_offset, ItemClassification.progression),
        ItemData(CHEMIST_JOB, JOB, 17 + job_index_offset, ItemClassification.progression),
        ItemData(REAPER_JOB, JOB, 6 + job_index_offset, ItemClassification.progression),
        ItemData(NINJA_JOB, JOB, 18 + job_index_offset, ItemClassification.progression),
        ItemData(NOMAD_JOB, JOB, 12 + job_index_offset, ItemClassification.progression),
        ItemData(DERVISH_JOB, JOB, 11 + job_index_offset, ItemClassification.progression),
        ItemData(BEATSMITH_JOB, JOB, 9 + job_index_offset, ItemClassification.progression),
        ItemData(SAMURAI_JOB, JOB, 20 + job_index_offset, ItemClassification.progression),
        ItemData(ASSASSIN_JOB, JOB, 19 + job_index_offset, ItemClassification.progression),
        ItemData(VALKYRIE_JOB, JOB, 15 + job_index_offset, ItemClassification.progression),
        ItemData(SUMMONER_JOB, JOB, 21 + job_index_offset, ItemClassification.progression),  # Required for summon fights; only job checked by NPCs
        ItemData(BEASTMASTER_JOB, JOB, 23 + job_index_offset, ItemClassification.progression),
        ItemData(WEAVER_JOB, JOB, 16 + job_index_offset, ItemClassification.progression),
        ItemData(MIMIC_JOB, JOB, 22 + job_index_offset, ItemClassification.progression),
        ItemData(PROGRESSIVE_QUINTAR_WOODWIND, MOUNT, 39 + item_index_offset, ItemClassification.progression, 3),  # Quintar Pass ID 7 & Quintar Flute ID 39 & Quintar Ocarina 115
        ItemData(IBEK_BELL, MOUNT, 50 + item_index_offset, ItemClassification.progression),
        ItemData(OWL_DRUM, MOUNT, 49 + item_index_offset, ItemClassification.progression),
        ItemData(PROGRESSIVE_SALMON_VIOLA, MOUNT, 48 + item_index_offset, ItemClassification.progression, 2),  # Salmon Violin ID 48 & Salmon Cello ID 114
        ItemData(PROGRESSIVE_MOUNT, MOUNT, 700 + item_index_offset, ItemClassification.progression, 7),
        ItemData(HOME_POINT_STONE, TELEPORT_STONE, 19 + item_index_offset, ItemClassification.useful),
    ],
    SPAWNING_MEADOWS_DISPLAY_NAME: [
        ItemData(SPAWNING_MEADOWS_PASS, PASS, 801 + item_index_offset, ItemClassification.progression),
        ItemData(SPAWNING_MEADOWS_MAP, MAP, 73 + item_index_offset, ItemClassification.useful),
        ItemData(BLACK_SQUIRREL, ITEM, 21 + item_index_offset, ItemClassification.progression, 4),
        ItemData("Item - Tonic Pouch", ITEM, 133 + item_index_offset, ItemClassification.useful, 2),
    ],
    DELENDE_DISPLAY_NAME: [
        ItemData(DELENDE_PASS, PASS, 802 + item_index_offset, ItemClassification.progression),
        ItemData(DELENDE_MAP, MAP, 74 + item_index_offset, ItemClassification.useful),
        ItemData(BASEMENT_MAP, MAP, 213 + item_index_offset, ItemClassification.useful),
        ItemData(DOG_BONE, ITEM, 6 + item_index_offset, ItemClassification.progression, 3),
        ItemData("Item - Gold Dust", ORE, 70 + item_index_offset, ItemClassification.useful),
        ItemData("Item - Tincture Pouch", ITEM, 135 + item_index_offset, ItemClassification.useful, 2),
        ItemData("Item - Flimsy Rod", TACKLE, 55 + item_index_offset, ItemClassification.progression),
        ItemData("Item - Plug Lure", TACKLE, 91 + item_index_offset, ItemClassification.progression),
    ]
}

region_shop_items: Dict[str, List[ItemData]] = {
    SPAWNING_MEADOWS_DISPLAY_NAME: [
        ItemData("Equipment - Short Sword", EQUIPMENT, 0 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Dirk", EQUIPMENT, 3 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Rapier", EQUIPMENT, 73 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Short Staff", EQUIPMENT, 5 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Ash Wand", EQUIPMENT, 8 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Buckler", EQUIPMENT, 44 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Chain Helm", EQUIPMENT, 25 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Breastplate", EQUIPMENT, 18 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Leather Cap", EQUIPMENT, 24 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Leather Outfit", EQUIPMENT, 17 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Hemp Hood", EQUIPMENT, 31 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Hemp Robe", EQUIPMENT, 19 + equipment_index_offset, ItemClassification.useful),
    ],
    DELENDE_DISPLAY_NAME: [
        ItemData("Equipment - Stout Shield", EQUIPMENT, 45 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Sturdy Helm", EQUIPMENT, 26 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Ring Mail", EQUIPMENT, 28 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Beret", EQUIPMENT, 27 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Studded Armor", EQUIPMENT, 35 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Cotton Hood", EQUIPMENT, 32 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Cotton Robe", EQUIPMENT, 20 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Earring", EQUIPMENT, 79 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Iron Sword", EQUIPMENT, 11 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Stabbers", EQUIPMENT, 63 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Stinger", EQUIPMENT, 1 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Cedar Staff", EQUIPMENT, 62 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Cedar Wand", EQUIPMENT, 13 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Bracer", EQUIPMENT, 70 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Cleaver", EQUIPMENT, 2 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Fishgutter", EQUIPMENT, 77 + equipment_index_offset, ItemClassification.useful),
        ItemData("Equipment - Moby Dick", EQUIPMENT, 51 + equipment_index_offset, ItemClassification.useful),
    ]
}