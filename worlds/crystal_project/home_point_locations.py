from typing import List, Optional

from .constants.home_points import *
from .constants.region_passes import *
from .locations import LocationData
from .options import CrystalProjectOptions
from .rules import CrystalProjectLogic


#Remember if you update the AP Region a Home Point is in or its name, go change it in the Menu connections function in the region.py file
#No rules on any Home Point locations bc if you get their teleport item, you can get there with no rules whatsoever
def get_home_points(player: int, options: Optional[CrystalProjectOptions]) -> List[LocationData]:
    logic = CrystalProjectLogic(player, options)  # pyright: ignore [reportArgumentType]
    home_point_table: List[LocationData] = [
        #Beginner
        #Spawning Meadows
        LocationData(HOMEPOINT_AP_SPAWN_AP_REGION, HOMEPOINT_AP_SPAWN_NAME, 5003, lambda state: state.has(SPAWNING_MEADOWS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_OLD_NANS_WATERING_HOLE_AP_REGION, HOMEPOINT_OLD_NANS_WATERING_HOLE_NAME, 59, lambda state: state.has(SPAWNING_MEADOWS_PASS, player) or logic.is_regionsanity_disabled()),
        #Delende
        LocationData(HOMEPOINT_FISH_HATCHERY_AP_REGION, HOMEPOINT_FISH_HATCHERY_NAME, 127, lambda state: state.has(DELENDE_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_SOILED_DEN_AP_REGION, HOMEPOINT_SOILED_DEN_NAME, 66, lambda state: state.has(DELENDE_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_THE_PALE_GROTTO_ENTRANCE_AP_REGION, HOMEPOINT_THE_PALE_GROTTO_ENTRANCE_NAME, 44, lambda state: state.has(DELENDE_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_DELENDE_FALLS_AP_REGION, HOMEPOINT_DELENDE_FALLS_NAME, 186, lambda state: state.has(DELENDE_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_DELENDE_PEAK_AP_REGION, HOMEPOINT_DELENDE_PEAK_NAME, 160, lambda state: state.has(DELENDE_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_CABIN_ON_THE_CLIFF_AP_REGION, HOMEPOINT_CABIN_ON_THE_CLIFF_NAME, 94, lambda state: state.has(DELENDE_PASS, player) or logic.is_regionsanity_disabled()),
        #Mercury Shrine
        LocationData(HOMEPOINT_MERCURY_SHRINE_AP_REGION, HOMEPOINT_MERCURY_SHRINE_NAME, 152, lambda state: state.has(MERCURY_SHRINE_PASS, player) or logic.is_regionsanity_disabled()),
        #The Pale Grotto
        LocationData(HOMEPOINT_THE_PALE_GROTTO_RUINS_AP_REGION, HOMEPOINT_THE_PALE_GROTTO_RUINS_NAME, 148, lambda state: state.has(THE_PALE_GROTTO_PASS, player) or logic.is_regionsanity_disabled()),
        #Seaside Cliffs
        LocationData(HOMEPOINT_SEASIDE_CLIFFS_AP_REGION, HOMEPOINT_SEASIDE_CLIFFS_CAMP_NAME, 72, lambda state: state.has(SEASIDE_CLIFFS_PASS, player) or logic.is_regionsanity_disabled()),
        #Yamagawa M.A.
        LocationData(HOMEPOINT_YAMAGAWA_MA_SUMMIT_AP_REGION, HOMEPOINT_YAMAGAWA_MA_SUMMIT_NAME, 165, lambda state: state.has(YAMAGAWA_MA_PASS, player) or logic.is_regionsanity_disabled()),
        #Proving Meadows
        LocationData(HOMEPOINT_PROVING_MEADOWS_CAMP_AP_REGION, HOMEPOINT_PROVING_MEADOWS_CAMP_NAME, 119, lambda state: state.has(PROVING_MEADOWS_PASS, player) or logic.is_regionsanity_disabled()),
        #Skumparadise
        LocationData(HOMEPOINT_SKUMPARADISE_ENTRANCE_AP_REGION, HOMEPOINT_SKUMPARADISE_ENTRANCE_NAME, 637, lambda state: state.has(SKUMPARADISE_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_SKUMPARADISE_DEPTHS_AP_REGION, HOMEPOINT_SKUMPARADISE_DEPTHS_NAME, 331, lambda state: state.has(SKUMPARADISE_PASS, player) or logic.is_regionsanity_disabled()),

        #Advanced
        #Capital Sequoia
        LocationData(HOMEPOINT_SKUMPARADISE_EXIT_AP_REGION, HOMEPOINT_SKUMPARADISE_EXIT_NAME, 231, lambda state: state.has(CAPITAL_SEQUOIA_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_GAEA_SHRINE_AP_REGION, HOMEPOINT_GAEA_SHRINE_NAME, 112, lambda state: state.has(CAPITAL_SEQUOIA_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_EAST_MARKET_DISTRICT_AP_REGION, HOMEPOINT_EAST_MARKET_DISTRICT_NAME, 374, lambda state: state.has(CAPITAL_SEQUOIA_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_BULLETIN_SQUARE_AP_REGION, HOMEPOINT_BULLETIN_SQUARE_NAME, 890, lambda state: state.has(CAPITAL_SEQUOIA_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_KNOW_IT_ALL_DUCKS_HOUSE_AP_REGION, HOMEPOINT_KNOW_IT_ALL_DUCKS_HOUSE_NAME, 559, lambda state: state.has(CAPITAL_SEQUOIA_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_WEST_MARKET_DISTRICT_AP_REGION, HOMEPOINT_WEST_MARKET_DISTRICT_NAME, 2026, lambda state: state.has(CAPITAL_SEQUOIA_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_TRAINING_GROUNDS_AP_REGION, HOMEPOINT_TRAINING_GROUNDS_NAME, 3057, lambda state: state.has(CAPITAL_SEQUOIA_PASS, player) or logic.is_regionsanity_disabled()),
        #Boomer Society
        LocationData(HOMEPOINT_BOOMER_SOCIETY_AP_REGION, HOMEPOINT_BOOMER_SOCIETY_NAME, 170, lambda state: state.has(BOOMER_SOCIETY_PASS, player) or logic.is_regionsanity_disabled()),
        #Rolling Quintar Fields
        LocationData(HOMEPOINT_QUINTAR_ENTHUSIASTS_HOUSE_AP_REGION, HOMEPOINT_QUINTAR_ENTHUSIASTS_HOUSE_NAME, 440, lambda state: state.has(ROLLING_QUINTAR_FIELDS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_RENT_A_QUINTAR_AP_REGION, HOMEPOINT_RENT_A_QUINTAR_NAME, 462, lambda state: state.has(ROLLING_QUINTAR_FIELDS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_QUINTAR_SANCTUM_AP_REGION, HOMEPOINT_QUINTAR_SANCTUM_NAME, 917, lambda state: state.has(ROLLING_QUINTAR_FIELDS_PASS, player) or logic.is_regionsanity_disabled()),
        #Quintar Sanctum
        LocationData(HOMEPOINT_QUINTAR_NAMEKO_AP_REGION, HOMEPOINT_QUINTAR_NAMEKO_NAME, 968, lambda state: state.has(QUINTAR_SANCTUM_PASS, player) or logic.is_regionsanity_disabled()),
        #Capital Jail
        LocationData(HOMEPOINT_CAPITAL_JAIL_ENTRANCE_AP_REGION, HOMEPOINT_CAPITAL_JAIL_ENTRANCE_NAME, 643, lambda state: state.has(CAPITAL_JAIL_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_CAPITAL_JAIL_DARK_WING_AP_REGION, HOMEPOINT_CAPITAL_JAIL_DARK_WING_NAME, 915, lambda state: state.has(CAPITAL_JAIL_PASS, player) or logic.is_regionsanity_disabled()),
        #Capital Pipeline
        LocationData(HOMEPOINT_CAPITAL_PIPELINE_AP_REGION, HOMEPOINT_CAPITAL_PIPELINE_NAME, 1127, lambda state: state.has(CAPITAL_PIPELINE_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_EAST_CAPITAL_PIPELINE_AP_REGION, HOMEPOINT_EAST_CAPITAL_PIPELINE_NAME, 1420, lambda state: state.has(CAPITAL_PIPELINE_PASS, player) or logic.is_regionsanity_disabled()),
        #Okimoto N.S.
        LocationData(HOMEPOINT_OKIMOTO_N_S_BASE_AP_REGION, HOMEPOINT_OKIMOTO_N_S_BASE_NAME, 335, lambda state: state.has(OKIMOTO_NS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_OKIMOTO_N_S_BASE_AP_REGION, HOMEPOINT_NINJA_YASHIKI_NAME, 366, lambda state: state.has(OKIMOTO_NS_PASS, player) or logic.is_regionsanity_disabled()),
        #Salmon Pass
        LocationData(HOMEPOINT_SALMON_PASS_ENTRANCE_AP_REGION, HOMEPOINT_SALMON_PASS_ENTRANCE_NAME, 367, lambda state: state.has(SALMON_PASS_PASS, player) or logic.is_regionsanity_disabled()),
        #Salmon River
        LocationData(HOMEPOINT_SALMON_SHACK_AP_REGION, HOMEPOINT_SALMON_SHACK_NAME, 1076, lambda state: state.has(SALMON_RIVER_PASS, player) or logic.is_regionsanity_disabled()),
        #Poko Poko Desert
        LocationData(HOMEPOINT_LABYRINTH_ENCAMPMENT_AP_REGION, HOMEPOINT_LABYRINTH_ENCAMPMENT_NAME, 2712, lambda state: state.has(POKO_POKO_DESERT_PASS, player) or logic.is_regionsanity_disabled()),
        #Sara Sara Bazaar
        LocationData(HOMEPOINT_SARA_SARA_BAZAAR_PORT_AP_REGION, HOMEPOINT_SARA_SARA_BAZAAR_PORT_NAME, 941, lambda state: state.has(SARA_SARA_BAZAAR_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_POKO_POKO_WEST_GATE_AP_REGION, HOMEPOINT_POKO_POKO_WEST_GATE_NAME, 3783, lambda state: state.has(SARA_SARA_BAZAAR_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_POKO_POKO_EAST_GATE_AP_REGION, HOMEPOINT_POKO_POKO_EAST_GATE_NAME, 3784, lambda state: state.has(SARA_SARA_BAZAAR_PASS, player) or logic.is_regionsanity_disabled()),
        #Sara Sara Beach
        LocationData(HOMEPOINT_IBEKS_CAVE_AP_REGION, HOMEPOINT_IBEKS_CAVE_NAME, 2005, lambda state: state.has(SARA_SARA_BEACH_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_BEACH_BIRDS_NEST_AP_REGION, HOMEPOINT_BEACH_BIRDS_NEST_NAME, 2709, lambda state: state.has(SARA_SARA_BEACH_PASS, player) or logic.is_regionsanity_disabled()),
        #Ancient Reservoir
        LocationData(HOMEPOINT_ANCIENT_RESERVOIR_ENTRANCE_AP_REGION, HOMEPOINT_ANCIENT_RESERVOIR_ENTRANCE_NAME, 1124, lambda state: state.has(ANCIENT_RESERVOIR_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_MAIN_RESERVOIR_CHAMBER_AP_REGION, HOMEPOINT_MAIN_RESERVOIR_CHAMBER_NAME, 1660, lambda state: state.has(ANCIENT_RESERVOIR_PASS, player) or logic.is_regionsanity_disabled()),

        #Expert
        #The Open Sea
        LocationData(HOMEPOINT_SAILORS_RAFT_AP_REGION, HOMEPOINT_SAILORS_RAFT_NAME, 3775, lambda state: state.has(THE_OPEN_SEA_PASS, player) or logic.is_regionsanity_disabled()),
        #Shoudu Province
        #former rules: lambda state: logic.has_vertical_movement(state) or logic.has_glide(state) or state.can_reach(GANYMEDE_SHRINE_AP_REGION, player=player) or state.can_reach(QUINTAR_RESERVE_AP_REGION, player=player)
        LocationData(HOMEPOINT_SHOUDU_FIELDS_AP_REGION, HOMEPOINT_SHOUDU_FIELDS_NAME, 576, lambda state: state.has(SHOUDU_PROVINCE_PASS, player) or logic.is_regionsanity_disabled()),
        #former rules: lambda state: logic.has_vertical_movement(state) or logic.has_glide(state) or state.can_reach(GANYMEDE_SHRINE_AP_REGION, player=player) or state.can_reach(QUINTAR_RESERVE_AP_REGION, player=player)
        LocationData(HOMEPOINT_SHOUDU_MARKET_AP_REGION, HOMEPOINT_SHOUDU_MARKET_NAME, 577, lambda state: state.has(SHOUDU_PROVINCE_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_SHOUDU_PORT_AP_REGION, HOMEPOINT_SHOUDU_PORT_NAME, 672, lambda state: state.has(SHOUDU_PROVINCE_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_SHANTY_INN_AP_REGION, HOMEPOINT_SHANTY_INN_NAME, 1523, lambda state: state.has(SHOUDU_PROVINCE_PASS, player) or logic.is_regionsanity_disabled()),
        #former rules: lambda state: logic.has_vertical_movement(state) or logic.has_glide(state) or state.can_reach(QUINTAR_RESERVE_AP_REGION, player=player)
        LocationData(HOMEPOINT_SKY_ARENA_AP_REGION, HOMEPOINT_SKY_ARENA_NAME, 1524, lambda state: state.has(SHOUDU_PROVINCE_PASS, player) or logic.is_regionsanity_disabled()),
        #former rules: lambda state: logic.has_vertical_movement(state) or logic.has_glide(state) or state.can_reach(GANYMEDE_SHRINE_AP_REGION, player=player) or state.can_reach(QUINTAR_RESERVE_AP_REGION, player=player)
        LocationData(HOMEPOINT_PRIZE_COUNTER_AP_REGION, HOMEPOINT_PRIZE_COUNTER_NAME, 2731, lambda state: state.has(SHOUDU_PROVINCE_PASS, player) or logic.is_regionsanity_disabled()),
        #former rules: lambda state: logic.has_vertical_movement(state) or logic.has_glide(state) or state.can_reach(GANYMEDE_SHRINE_AP_REGION, player=player) or state.can_reach(QUINTAR_RESERVE_AP_REGION, player=player)
        LocationData(HOMEPOINT_SHOUDU_ELEVATOR_AP_REGION, HOMEPOINT_SHOUDU_ELEVATOR_NAME, 3523, lambda state: state.has(SHOUDU_PROVINCE_PASS, player) or logic.is_regionsanity_disabled()),
        #The Undercity
        #former rules: lambda state: logic.has_swimming(state) or logic.has_horizontal_movement(state) or logic.has_vertical_movement(state) or state.can_reach(GANYMEDE_SHRINE_AP_REGION, player=player) or state.can_reach(QUINTAR_RESERVE_AP_REGION, player=player)
        LocationData(HOMEPOINT_THE_UNDERCITY_AP_REGION, HOMEPOINT_THE_UNDERCITY_NAME, 1266, lambda state: state.has(THE_UNDERCITY_PASS, player) or logic.is_regionsanity_disabled()),
        #Ganymede Shrine
        LocationData(HOMEPOINT_GANYMEDE_SHRINE_AP_REGION, HOMEPOINT_GANYMEDE_SHRINE_NAME, 1573, lambda state: state.has(GANYMEDE_SHRINE_PASS, player) or logic.is_regionsanity_disabled()),
        #Beaurior Volcano
        LocationData(HOMEPOINT_BEAURIOR_ROCK_AP_REGION, HOMEPOINT_BEAURIOR_ROCK_NAME, 1792, lambda state: state.has(BEAURIOR_VOLCANO_PASS, player) or logic.is_regionsanity_disabled()),
        # TODO: put volcano peak in separate ap region instead of included in Beaurior Rock (also items nearby, not just homepoint stone)
        #former rules: lambda state: logic.has_key(state, SMALL_KEY, 4) and logic.has_key(state, BEAURIOR_BOSS_KEY)
        LocationData(HOMEPOINT_BEAURIOR_VOLCANO_PEAK_AP_REGION, HOMEPOINT_BEAURIOR_VOLCANO_PEAK_NAME, 3037, lambda state: state.has(BEAURIOR_VOLCANO_PASS, player) or logic.is_regionsanity_disabled()),
        #Beaurior Rock
        #former rules: lambda state: logic.has_key(state, SMALL_KEY, 4)
        LocationData(HOMEPOINT_BOSS_ROOM_AP_REGION, HOMEPOINT_BOSS_ROOM_NAME, 822, lambda state: state.has(BEAURIOR_ROCK_PASS, player) or logic.is_regionsanity_disabled()),
        #Quintar Reserve
        LocationData(HOMEPOINT_DIONE_SHRINE_AP_REGION, HOMEPOINT_DIONE_SHRINE_NAME, 1595, lambda state: state.has(QUINTAR_RESERVE_PASS, player) or logic.is_regionsanity_disabled()),
        #Dione Shrine
        LocationData(HOMEPOINT_FLYERS_LOOKOUT_AP_REGION, HOMEPOINT_FLYERS_LOOKOUT_NAME, 2141, lambda state: state.has(DIONE_SHRINE_PASS, player) or logic.is_regionsanity_disabled()),
        #Tall, Tall Heights
        LocationData(HOMEPOINT_SEQUOIA_ATHENAEUM_AP_REGION, HOMEPOINT_SEQUOIA_ATHENAEUM_NAME, 2361, lambda state: state.has(TALL_TALL_HEIGHTS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_ICE_PASS_AP_REGION, HOMEPOINT_ICE_PASS_NAME, 2413, lambda state: state.has(TALL_TALL_HEIGHTS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_TALL_TALL_SOUVENIR_SHOP_AP_REGION, HOMEPOINT_TALL_TALL_SOUVENIR_SHOP_NAME, 1260, lambda state: state.has(TALL_TALL_HEIGHTS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_LANDS_END_COTTAGE_AP_REGION, HOMEPOINT_LANDS_END_COTTAGE_NAME, 2564, lambda state: state.has(TALL_TALL_HEIGHTS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_SLIP_GLIDE_RIDE_EXIT_AP_REGION, HOMEPOINT_SLIP_GLIDE_RIDE_EXIT_NAME, 2743, lambda state: state.has(TALL_TALL_HEIGHTS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_ICE_FISHERS_HUT_AP_REGION, HOMEPOINT_ICE_FISHERS_HUT_NAME, 3014, lambda state: state.has(TALL_TALL_HEIGHTS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_TRITON_SHRINE_AP_REGION, HOMEPOINT_TRITON_SHRINE_NAME, 3018, lambda state: state.has(TALL_TALL_HEIGHTS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_TALL_TALL_HEIGHTS_AP_REGION, HOMEPOINT_TALL_TALL_HEIGHTS_NAME, 3047, lambda state: state.has(TALL_TALL_HEIGHTS_PASS, player) or logic.is_regionsanity_disabled()),
        #Land's End
        LocationData(HOMEPOINT_SUMMIT_SHRINE_AP_REGION, HOMEPOINT_SUMMIT_SHRINE_NAME, 1559, lambda state: state.has(LANDS_END_PASS, player) or logic.is_regionsanity_disabled()),
        #Slip Glide Ride
        LocationData(HOMEPOINT_SLIP_GLIDE_RIDE_ENTRANCE_AP_REGION, HOMEPOINT_SLIP_GLIDE_RIDE_ENTRANCE_NAME, 1550, lambda state: state.has(SLIP_GLIDE_RIDE_PASS, player) or logic.is_regionsanity_disabled()),
        #Castle Ramparts
        LocationData(HOMEPOINT_EAST_RAMPARTS_AP_REGION, HOMEPOINT_EAST_RAMPARTS_NAME, 1375, lambda state: state.has(CASTLE_RAMPARTS_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_WEST_RAMPARTS_AP_REGION, HOMEPOINT_WEST_RAMPARTS_NAME, 1376, lambda state: state.has(CASTLE_RAMPARTS_PASS, player) or logic.is_regionsanity_disabled()),
        #The Chalice of Tar
        LocationData(HOMEPOINT_THE_CHALICE_OF_TAR_AP_REGION, HOMEPOINT_THE_CHALICE_OF_TAR_NAME, 3055, lambda state: state.has(THE_CHALICE_OF_TAR_PASS, player) or logic.is_regionsanity_disabled()),
        #Jidamba Tangle
        LocationData(HOMEPOINT_EUROPA_SHRINE_AP_REGION, HOMEPOINT_EUROPA_SHRINE_NAME, 1626, lambda state: state.has(JIDAMBA_TANGLE_PASS, player) or logic.is_regionsanity_disabled()),
        #Jidamba Eaclaneya
        LocationData(HOMEPOINT_EACLANEYA_ENTRANCE_AP_REGION, HOMEPOINT_EACLANEYA_ENTRANCE_NAME, 1402, lambda state: state.has(JIDAMBA_EACLANEYA_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_SALMON_ROOM_AP_REGION, HOMEPOINT_SALMON_ROOM_NAME, 2474, lambda state: state.has(JIDAMBA_EACLANEYA_PASS, player) or logic.is_regionsanity_disabled()),
        #Neptune Shrine
        LocationData(HOMEPOINT_NEPTUNE_SHRINE_AP_REGION, HOMEPOINT_NEPTUNE_SHRINE_NAME, 3781, lambda state: state.has(NEPTUNE_SHRINE_PASS, player) or logic.is_regionsanity_disabled()),
        #Continental Tram
        LocationData(HOMEPOINT_PLATFORM_A_AP_REGION, HOMEPOINT_PLATFORM_A_NAME, 3780, lambda state: state.has(CONTINENTAL_TRAM_PASS, player) or logic.is_regionsanity_disabled()),

        #End-Game
        #Ancient Labyrinth
        LocationData(HOMEPOINT_ANCIENT_LABYRINTH_CORE_AP_REGION, HOMEPOINT_ANCIENT_LABYRINTH_CORE_NAME, 1739, lambda state: state.has(ANCIENT_LABYRINTH_PASS, player) or logic.is_regionsanity_disabled()),
        #The Sequoia
        LocationData(HOMEPOINT_TOP_OF_THE_SEQUOIA_AP_REGION, HOMEPOINT_TOP_OF_THE_SEQUOIA_NAME, 2452, lambda state: state.has(THE_SEQUOIA_PASS, player) or logic.is_regionsanity_disabled()),
        #Castle Sequoia
        LocationData(HOMEPOINT_CASTLE_SEQUOIA_FOYER_AP_REGION, HOMEPOINT_CASTLE_SEQUOIA_FOYER_NAME, 514, lambda state: state.has(CASTLE_SEQUOIA_PASS, player) or logic.is_regionsanity_disabled()),
        #The New World
        LocationData(HOMEPOINT_ASTLEYS_SHRINE_AP_REGION, HOMEPOINT_ASTLEYS_SHRINE_NAME, 3776, lambda state: state.has(THE_NEW_WORLD_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_ASTLEYS_KEEP_AP_REGION, HOMEPOINT_ASTLEYS_KEEP_NAME, 3777, lambda state: state.has(THE_NEW_WORLD_PASS, player) or logic.is_regionsanity_disabled()),
        LocationData(HOMEPOINT_DISCIPLINE_HOLLOW_AP_REGION, HOMEPOINT_DISCIPLINE_HOLLOW_NAME, 3797, lambda state: state.has(THE_NEW_WORLD_PASS, player) or logic.is_regionsanity_disabled()),
    ]

    return home_point_table