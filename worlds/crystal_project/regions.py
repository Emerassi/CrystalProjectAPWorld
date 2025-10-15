from typing import List, Dict, Tuple, Callable, TYPE_CHECKING
from BaseClasses import Region, Location, CollectionState
from .options import CrystalProjectOptions
from .locations import LocationData
from .items import display_region_name_to_pass_dict
from .rules import CrystalProjectLogic
from .constants.keys import *
from .constants.key_items import *
from .constants.ap_regions import *
from .constants.display_regions import *
from .constants.teleport_stones import *
from .constants.region_passes import *

if TYPE_CHECKING:
    from . import CrystalProjectWorld

ap_region_to_display_region_dictionary: Dict[str, str] = {}

display_region_subregions_dictionary: Dict[str, List[str]] = {
    #Beginner
    MENU_DISPLAY_NAME: MENU_DISPLAY_SUBREGIONS,
    SPAWNING_MEADOWS_DISPLAY_NAME: SPAWNING_MEADOWS_DISPLAY_SUBREGIONS,
    DELENDE_DISPLAY_NAME: DELENDE_DISPLAY_SUBREGIONS,
    SOILED_DEN_DISPLAY_NAME: SOILED_DEN_DISPLAY_SUBREGIONS,
    THE_PALE_GROTTO_DISPLAY_NAME: THE_PALE_GROTTO_DISPLAY_SUBREGIONS,
    SEASIDE_CLIFFS_DISPLAY_NAME: SEASIDE_CLIFFS_DISPLAY_SUBREGIONS,
    DRAFT_SHAFT_CONDUIT_DISPLAY_NAME: DRAFT_SHAFT_CONDUIT_DISPLAY_SUBREGIONS,
    MERCURY_SHRINE_DISPLAY_NAME: MERCURY_SHRINE_DISPLAY_SUBREGIONS,
    YAMAGAWA_MA_DISPLAY_NAME: YAMAGAWA_MA_DISPLAY_SUBREGIONS,
    PROVING_MEADOWS_DISPLAY_NAME: PROVING_MEADOWS_DISPLAY_SUBREGIONS,
    SKUMPARADISE_DISPLAY_NAME: SKUMPARADISE_DISPLAY_SUBREGIONS,
    #Advanced
    CAPITAL_SEQUOIA_DISPLAY_NAME: CAPITAL_SEQUOIA_DISPLAY_SUBREGIONS,
    JOJO_SEWERS_DISPLAY_NAME: JOJO_SEWERS_DISPLAY_SUBREGIONS,
    BOOMER_SOCIETY_DISPLAY_NAME: BOOMER_SOCIETY_DISPLAY_SUBREGIONS,
    ROLLING_QUINTAR_FIELDS_DISPLAY_NAME: ROLLING_QUINTAR_FIELDS_DISPLAY_SUBREGIONS,
    QUINTAR_NEST_DISPLAY_NAME: QUINTAR_NEST_DISPLAY_SUBREGIONS,
    QUINTAR_SANCTUM_DISPLAY_NAME: QUINTAR_SANCTUM_DISPLAY_SUBREGIONS,
    CAPITAL_JAIL_DISPLAY_NAME: CAPITAL_JAIL_DISPLAY_SUBREGIONS,
    CAPITAL_PIPELINE_DISPLAY_NAME: CAPITAL_PIPELINE_DISPLAY_SUBREGIONS,
    COBBLESTONE_CRAG_DISPLAY_NAME: COBBLESTONE_CRAG_DISPLAY_SUBREGIONS,
    OKIMOTO_NS_DISPLAY_NAME: OKIMOTO_NS_DISPLAY_SUBREGIONS,
    GREENSHIRE_REPRISE_DISPLAY_NAME: GREENSHIRE_REPRISE_DISPLAY_SUBREGIONS,
    SALMON_PASS_DISPLAY_NAME: SALMON_PASS_DISPLAY_SUBREGIONS,
    SALMON_RIVER_DISPLAY_NAME: SALMON_RIVER_DISPLAY_SUBREGIONS,
    SHOUDU_WATERFRONT_DISPLAY_NAME: SHOUDU_WATERFRONT_DISPLAY_SUBREGIONS,
    POKO_POKO_DESERT_DISPLAY_NAME: POKO_POKO_DESERT_DISPLAY_SUBREGIONS,
    SARA_SARA_BAZAAR_DISPLAY_NAME: SARA_SARA_BAZAAR_DISPLAY_SUBREGIONS,
    SARA_SARA_BEACH_EAST_DISPLAY_NAME: SARA_SARA_BEACH_EAST_DISPLAY_SUBREGIONS,
    SARA_SARA_BEACH_WEST_DISPLAY_NAME: SARA_SARA_BEACH_WEST_DISPLAY_SUBREGIONS,
    ANCIENT_RESERVOIR_DISPLAY_NAME: ANCIENT_RESERVOIR_DISPLAY_SUBREGIONS,
    SALMON_BAY_DISPLAY_NAME: SALMON_BAY_DISPLAY_SUBREGIONS,
    #Expert
    THE_OPEN_SEA_DISPLAY_NAME: THE_OPEN_SEA_DISPLAY_SUBREGIONS,
    SHOUDU_PROVINCE_DISPLAY_NAME: SHOUDU_PROVINCE_DISPLAY_SUBREGIONS,
    THE_UNDERCITY_DISPLAY_NAME: THE_UNDERCITY_DISPLAY_SUBREGIONS,
    GANYMEDE_SHRINE_DISPLAY_NAME: GANYMEDE_SHRINE_DISPLAY_SUBREGIONS,
    BEAURIOR_VOLCANO_DISPLAY_NAME: BEAURIOR_VOLCANO_DISPLAY_SUBREGIONS,
    BEAURIOR_ROCK_DISPLAY_NAME: BEAURIOR_ROCK_DISPLAY_SUBREGIONS,
    LAKE_DELENDE_DISPLAY_NAME: LAKE_DELENDE_DISPLAY_SUBREGIONS,
    QUINTAR_RESERVE_DISPLAY_NAME: QUINTAR_RESERVE_DISPLAY_SUBREGIONS,
    DIONE_SHRINE_DISPLAY_NAME: DIONE_SHRINE_DISPLAY_SUBREGIONS,
    QUINTAR_MAUSOLEUM_DISPLAY_NAME: QUINTAR_MAUSOLEUM_DISPLAY_SUBREGIONS,
    EASTERN_CHASM_DISPLAY_NAME: EASTERN_CHASM_DISPLAY_SUBREGIONS,
    TALL_TALL_HEIGHTS_DISPLAY_NAME: TALL_TALL_HEIGHTS_DISPLAY_SUBREGIONS,
    NORTHERN_CAVE_DISPLAY_NAME: NORTHERN_CAVE_DISPLAY_SUBREGIONS,
    LANDS_END_DISPLAY_NAME: LANDS_END_DISPLAY_SUBREGIONS,
    SLIP_GLIDE_RIDE_DISPLAY_NAME: SLIP_GLIDE_RIDE_DISPLAY_SUBREGIONS,
    SEQUOIA_ATHENAEUM_DISPLAY_NAME: SEQUOIA_ATHENAEUM_DISPLAY_SUBREGIONS,
    NORTHERN_STRETCH_DISPLAY_NAME: NORTHERN_STRETCH_DISPLAY_SUBREGIONS,
    CASTLE_RAMPARTS_DISPLAY_NAME: CASTLE_RAMPARTS_DISPLAY_SUBREGIONS,
    THE_CHALICE_OF_TAR_DISPLAY_NAME: THE_CHALICE_OF_TAR_DISPLAY_SUBREGIONS,
    FLYERS_CRAG_DISPLAY_NAME: FLYERS_CRAG_DISPLAY_SUBREGIONS,
    JIDAMBA_TANGLE_DISPLAY_NAME: JIDAMBA_TANGLE_DISPLAY_SUBREGIONS,
    JIDAMBA_EACLANEYA_DISPLAY_NAME: JIDAMBA_EACLANEYA_DISPLAY_SUBREGIONS,
    THE_DEEP_SEA_DISPLAY_NAME: THE_DEEP_SEA_DISPLAY_SUBREGIONS,
    NEPTUNE_SHRINE_DISPLAY_NAME: NEPTUNE_SHRINE_DISPLAY_SUBREGIONS,
    JADE_CAVERN_DISPLAY_NAME: JADE_CAVERN_DISPLAY_SUBREGIONS,
    CONTINENTAL_TRAM_DISPLAY_NAME: CONTINENTAL_TRAM_DISPLAY_SUBREGIONS,
    #End Game
    ANCIENT_LABYRINTH_DISPLAY_NAME: ANCIENT_LABYRINTH_DISPLAY_SUBREGIONS,
    THE_SEQUOIA_DISPLAY_NAME: THE_SEQUOIA_DISPLAY_SUBREGIONS,
    THE_DEPTHS_DISPLAY_NAME: THE_DEPTHS_DISPLAY_SUBREGIONS,
    CASTLE_SEQUOIA_DISPLAY_NAME: CASTLE_SEQUOIA_DISPLAY_SUBREGIONS,
    THE_OLD_WORLD_DISPLAY_NAME: THE_OLD_WORLD_DISPLAY_SUBREGIONS,
    THE_NEW_WORLD_DISPLAY_NAME: THE_NEW_WORLD_DISPLAY_SUBREGIONS,
    MODDED_ZONE_DISPLAY_NAME: MODDED_ZONE_DISPLAY_SUBREGIONS,
}

display_region_levels_dictionary: Dict[str, Tuple[int, int]] = {
    #Beginner
    MENU_DISPLAY_NAME: (0, 0),
    SPAWNING_MEADOWS_DISPLAY_NAME: (3, 3),
    DELENDE_DISPLAY_NAME: (5, 10),
    SOILED_DEN_DISPLAY_NAME: (7, 7),
    THE_PALE_GROTTO_DISPLAY_NAME: (7, 10),
    SEASIDE_CLIFFS_DISPLAY_NAME: (10, 15),
    DRAFT_SHAFT_CONDUIT_DISPLAY_NAME: (12, 12),
    MERCURY_SHRINE_DISPLAY_NAME: (0, 0),
    YAMAGAWA_MA_DISPLAY_NAME: (15, 15),
    PROVING_MEADOWS_DISPLAY_NAME: (0, 0),
    SKUMPARADISE_DISPLAY_NAME: (15, 17),
    #Advanced
    CAPITAL_SEQUOIA_DISPLAY_NAME: (0, 0),
    JOJO_SEWERS_DISPLAY_NAME: (20, 22),
    BOOMER_SOCIETY_DISPLAY_NAME: (0, 0),
    ROLLING_QUINTAR_FIELDS_DISPLAY_NAME: (18, 21),
    QUINTAR_NEST_DISPLAY_NAME: (18, 22),
    QUINTAR_SANCTUM_DISPLAY_NAME: (21, 21),
    CAPITAL_JAIL_DISPLAY_NAME: (24, 27),
    CAPITAL_PIPELINE_DISPLAY_NAME: (50, 50),
    COBBLESTONE_CRAG_DISPLAY_NAME: (0, 0),
    OKIMOTO_NS_DISPLAY_NAME: (27, 31),
    GREENSHIRE_REPRISE_DISPLAY_NAME: (33, 33),
    SALMON_PASS_DISPLAY_NAME: (0, 0),
    SALMON_RIVER_DISPLAY_NAME: (26, 29),
    SHOUDU_WATERFRONT_DISPLAY_NAME: (0, 0),
    POKO_POKO_DESERT_DISPLAY_NAME: (30, 32),
    SARA_SARA_BAZAAR_DISPLAY_NAME: (0, 0),
    SARA_SARA_BEACH_EAST_DISPLAY_NAME: (30, 30),
    SARA_SARA_BEACH_WEST_DISPLAY_NAME: (38, 40),
    ANCIENT_RESERVOIR_DISPLAY_NAME: (33, 35),
    #IBEK_CAVE_AP_REGION: (35, 35),
    SALMON_BAY_DISPLAY_NAME: (0, 0),
    #Expert
    THE_OPEN_SEA_DISPLAY_NAME: (54, 56),
    SHOUDU_PROVINCE_DISPLAY_NAME: (36, 37),
    THE_UNDERCITY_DISPLAY_NAME: (37, 39),
    GANYMEDE_SHRINE_DISPLAY_NAME: (0, 0),
    BEAURIOR_VOLCANO_DISPLAY_NAME: (37, 37),
    BEAURIOR_ROCK_DISPLAY_NAME: (38, 40),
    LAKE_DELENDE_DISPLAY_NAME: (40, 40),
    QUINTAR_RESERVE_DISPLAY_NAME: (0, 0),
    DIONE_SHRINE_DISPLAY_NAME: (0, 0),
    QUINTAR_MAUSOLEUM_DISPLAY_NAME: (54, 56),
    EASTERN_CHASM_DISPLAY_NAME: (0, 0),
    TALL_TALL_HEIGHTS_DISPLAY_NAME: (41, 45),
    NORTHERN_CAVE_DISPLAY_NAME: (43, 44),
    LANDS_END_DISPLAY_NAME: (44, 47),
    SLIP_GLIDE_RIDE_DISPLAY_NAME: (46, 48),
    SEQUOIA_ATHENAEUM_DISPLAY_NAME: (0, 0),
    NORTHERN_STRETCH_DISPLAY_NAME: (0, 0),
    CASTLE_RAMPARTS_DISPLAY_NAME: (50, 50),
    THE_CHALICE_OF_TAR_DISPLAY_NAME: (60, 60),
    FLYERS_CRAG_DISPLAY_NAME: (0, 0),
    JIDAMBA_TANGLE_DISPLAY_NAME: (50, 54),
    JIDAMBA_EACLANEYA_DISPLAY_NAME: (54, 57),
    THE_DEEP_SEA_DISPLAY_NAME: (58, 64),
    NEPTUNE_SHRINE_DISPLAY_NAME: (0, 0),
    JADE_CAVERN_DISPLAY_NAME: (57, 57),
    CONTINENTAL_TRAM_DISPLAY_NAME: (0, 0),
    #End Game
    ANCIENT_LABYRINTH_DISPLAY_NAME: (62, 66),
    THE_SEQUOIA_DISPLAY_NAME: (60, 63),
    THE_DEPTHS_DISPLAY_NAME: (63, 65),
    CASTLE_SEQUOIA_DISPLAY_NAME: (56, 59),
    THE_OLD_WORLD_DISPLAY_NAME: (70, 70),
    THE_NEW_WORLD_DISPLAY_NAME: (60, 60),
    MODDED_ZONE_DISPLAY_NAME: (30, 30),
}

rules_on_display_regions: Dict[str, Callable[[CollectionState], bool]] = {}

class CrystalProjectLocation(Location):
    game: str = "CrystalProject"

    def __init__(self, player: int, name: str = " ", address = None, parent=None):
        super().__init__(player, name, address, parent)

def init_areas(world: "CrystalProjectWorld", locations: List[LocationData], options: CrystalProjectOptions) -> None:
    multiworld = world.multiworld
    player = world.player
    logic = CrystalProjectLogic(player, options)

    for display_region in display_region_subregions_dictionary:
        for ap_region in display_region_subregions_dictionary[display_region]:
            ap_region_to_display_region_dictionary[ap_region] = display_region

    rules_on_display_regions[MODDED_ZONE_AP_REGION] = lambda state: True

    for display_region in display_region_levels_dictionary:
        if world.options.regionsanity.value == world.options.regionsanity.option_true and display_region != MODDED_ZONE_AP_REGION:
            rules_on_display_regions[display_region] = lambda state, lambda_region = display_region: (logic.is_area_in_level_range(state, display_region_levels_dictionary[lambda_region][0])
                                                                                                      and state.has(display_region_name_to_pass_dict[lambda_region], player))

            rules_on_display_regions[MODDED_ZONE_AP_REGION] = combine_callables(rules_on_display_regions[MODDED_ZONE_AP_REGION], rules_on_display_regions[display_region])
        else:
            rules_on_display_regions[display_region] = lambda state, lambda_region = display_region: (logic.is_area_in_level_range(state, display_region_levels_dictionary[lambda_region][0]))

    locations_per_region = get_locations_per_ap_region(locations)

    excluded = False

    beginner_regions = [
        create_display_region(world, player, locations_per_region, MENU_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SPAWNING_MEADOWS_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, DELENDE_DISPLAY_NAME, excluded),
        # bumped up mercury shrine because region order influences shop price NOTE TO DRAGONS, DO NOT MOVE WITHOUT REASON!!
        create_display_region(world, player, locations_per_region, MERCURY_SHRINE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SOILED_DEN_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, THE_PALE_GROTTO_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SEASIDE_CLIFFS_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, DRAFT_SHAFT_CONDUIT_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, YAMAGAWA_MA_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, PROVING_MEADOWS_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SKUMPARADISE_DISPLAY_NAME, excluded),
    ]

    if (options.includedRegions == options.includedRegions.option_advanced or
        options.includedRegions == options.includedRegions.option_expert or
        options.includedRegions == options.includedRegions.option_all):
        excluded = False
    else:
        excluded = True

    advanced_regions = [
        create_display_region(world, player, locations_per_region, CAPITAL_SEQUOIA_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, JOJO_SEWERS_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, BOOMER_SOCIETY_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, ROLLING_QUINTAR_FIELDS_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, QUINTAR_NEST_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, QUINTAR_SANCTUM_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, CAPITAL_JAIL_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, CAPITAL_PIPELINE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, COBBLESTONE_CRAG_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, OKIMOTO_NS_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, GREENSHIRE_REPRISE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SALMON_PASS_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SALMON_RIVER_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SHOUDU_WATERFRONT_DISPLAY_NAME, excluded), #moved from Expert to Advanced
        create_display_region(world, player, locations_per_region, POKO_POKO_DESERT_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SARA_SARA_BAZAAR_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SARA_SARA_BEACH_EAST_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SARA_SARA_BEACH_WEST_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, ANCIENT_RESERVOIR_DISPLAY_NAME, excluded),
        #create_display_region(world, player, locations_per_region, IBEK_CAVE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SALMON_BAY_DISPLAY_NAME, excluded),
    ]

    if (options.includedRegions == options.includedRegions.option_expert or
        options.includedRegions == options.includedRegions.option_all):
        excluded = False
    else:
        excluded = True

    expert_regions = [
        create_display_region(world, player, locations_per_region, THE_OPEN_SEA_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SHOUDU_PROVINCE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, THE_UNDERCITY_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, GANYMEDE_SHRINE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, BEAURIOR_VOLCANO_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, BEAURIOR_ROCK_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, LAKE_DELENDE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, QUINTAR_RESERVE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, DIONE_SHRINE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, QUINTAR_MAUSOLEUM_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, EASTERN_CHASM_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, TALL_TALL_HEIGHTS_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, NORTHERN_CAVE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, LANDS_END_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SLIP_GLIDE_RIDE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, SEQUOIA_ATHENAEUM_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, NORTHERN_STRETCH_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, CASTLE_RAMPARTS_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, THE_CHALICE_OF_TAR_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, FLYERS_CRAG_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, JIDAMBA_TANGLE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, JIDAMBA_EACLANEYA_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, THE_DEEP_SEA_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, NEPTUNE_SHRINE_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, JADE_CAVERN_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, CONTINENTAL_TRAM_DISPLAY_NAME, excluded),
    ]

    if options.includedRegions == options.includedRegions.option_all:
        excluded = False
    else:
        excluded = True
     
    end_game_regions = [
        create_display_region(world, player, locations_per_region, ANCIENT_LABYRINTH_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, THE_SEQUOIA_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, THE_DEPTHS_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, CASTLE_SEQUOIA_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, THE_OLD_WORLD_DISPLAY_NAME, excluded),
        create_display_region(world, player, locations_per_region, THE_NEW_WORLD_DISPLAY_NAME, excluded),
    ]

    if options.useMods.value == options.useMods.option_true:
        excluded = False
    else:
        excluded = True

    modded_regions = [
        create_display_region(world, player, locations_per_region, MODDED_ZONE_DISPLAY_NAME, excluded),
    ]

    for beginner_display_region_subregions in beginner_regions:
        multiworld.regions += beginner_display_region_subregions
    for advanced_display_region_subregions in advanced_regions:
        multiworld.regions += advanced_display_region_subregions
    for expert_display_region_subregions in expert_regions:
        multiworld.regions += expert_display_region_subregions
    for end_game_display_region_subregions in end_game_regions:
        multiworld.regions += end_game_display_region_subregions
    for modded_display_region_subregions in modded_regions:
        multiworld.regions += modded_display_region_subregions

    connect_menu_region(world, options)

    fancy_add_exits(world, SPAWNING_MEADOWS_AP_REGION, [DELENDE_AP_REGION, MERCURY_SHRINE_AP_REGION, POKO_POKO_DESERT_AP_REGION, CONTINENTAL_TRAM_AP_REGION, BEAURIOR_VOLCANO_AP_REGION, YAMAGAWA_MA_AP_REGION],
                    {CONTINENTAL_TRAM_AP_REGION: lambda state: logic.has_swimming(state) and options.obscureRoutes.value == options.obscureRoutes.option_true,
                     MERCURY_SHRINE_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     POKO_POKO_DESERT_AP_REGION: lambda state: logic.has_vertical_movement(state) or options.obscureRoutes.value == options.obscureRoutes.option_true,
                     BEAURIOR_VOLCANO_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     YAMAGAWA_MA_AP_REGION: lambda state: logic.has_swimming(state) or logic.has_vertical_movement(state)})
    fancy_add_exits(world, DELENDE_AP_REGION, [GRAN_AP_REGION, BELOW_GRAN_AP_REGION, SPAWNING_MEADOWS_AP_REGION, SOILED_DEN_AP_REGION, THE_PALE_GROTTO_AP_REGION, YAMAGAWA_MA_AP_REGION, SEASIDE_CLIFFS_AP_REGION, MERCURY_SHRINE_AP_REGION, GREENSHIRE_REPRISE_AP_REGION, SALMON_PASS_AP_REGION, PROVING_MEADOWS_AP_REGION, LAKE_DELENDE_AP_REGION],
                    {GRAN_AP_REGION: lambda state: logic.can_fight_gran(state),
                     BELOW_GRAN_AP_REGION: lambda state: options.obscureRoutes.value == options.obscureRoutes.option_true,
                     SALMON_PASS_AP_REGION: lambda state: logic.has_swimming(state),
                     GREENSHIRE_REPRISE_AP_REGION: lambda state: logic.has_swimming(state) or options.obscureRoutes.value == options.obscureRoutes.option_true,
                     PROVING_MEADOWS_AP_REGION: lambda state: logic.has_horizontal_movement(state) or logic.has_vertical_movement(state),
                     LAKE_DELENDE_AP_REGION: lambda state: logic.has_vertical_movement(state) or options.obscureRoutes.value == options.obscureRoutes.option_true})
    fancy_add_exits(world, GRAN_AP_REGION, [DELENDE_AP_REGION, BELOW_GRAN_AP_REGION])
    fancy_add_exits(world, BELOW_GRAN_AP_REGION, [GRAN_AP_REGION, ANCIENT_RESERVOIR_AP_REGION, JADE_CAVERN_AP_REGION],
                    {GRAN_AP_REGION: lambda state: logic.can_fight_gran(state),
                    ANCIENT_RESERVOIR_AP_REGION: lambda state: logic.has_swimming(state),
                    JADE_CAVERN_AP_REGION: lambda state: logic.has_golden_quintar(state)})
    fancy_add_exits(world, MERCURY_SHRINE_AP_REGION, [DELENDE_AP_REGION, SEASIDE_CLIFFS_AP_REGION, BEAURIOR_VOLCANO_AP_REGION],
                    {BEAURIOR_VOLCANO_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, SOILED_DEN_AP_REGION, [JADE_CAVERN_AP_REGION, DELENDE_AP_REGION, THE_PALE_GROTTO_AP_REGION, DRAFT_SHAFT_CONDUIT_AP_REGION],
                    {JADE_CAVERN_AP_REGION: lambda state: logic.has_golden_quintar(state),
                     THE_PALE_GROTTO_AP_REGION: lambda state: logic.has_swimming(state),
                     DRAFT_SHAFT_CONDUIT_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, THE_PALE_GROTTO_AP_REGION, [DELENDE_AP_REGION, SOILED_DEN_AP_REGION, PROVING_MEADOWS_AP_REGION, JOJO_SEWERS_AP_REGION, TALL_TALL_HEIGHTS_AP_REGION, SALMON_PASS_AP_REGION],
                    {SOILED_DEN_AP_REGION: lambda state: logic.has_swimming(state),
                     JOJO_SEWERS_AP_REGION: lambda state: logic.has_swimming(state),
                     TALL_TALL_HEIGHTS_AP_REGION: lambda state: logic.has_swimming(state),
                     SALMON_PASS_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, SEASIDE_CLIFFS_AP_REGION, [DELENDE_AP_REGION, DRAFT_SHAFT_CONDUIT_AP_REGION, THE_OPEN_SEA_AP_REGION, MERCURY_SHRINE_AP_REGION, BEAURIOR_VOLCANO_AP_REGION],
                    {BEAURIOR_VOLCANO_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state),
                     MERCURY_SHRINE_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, DRAFT_SHAFT_CONDUIT_AP_REGION, [SEASIDE_CLIFFS_AP_REGION, SOILED_DEN_AP_REGION],
                    {SOILED_DEN_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, YAMAGAWA_MA_AP_REGION, [SPAWNING_MEADOWS_AP_REGION, DELENDE_AP_REGION, LAKE_DELENDE_AP_REGION],
                    {LAKE_DELENDE_AP_REGION: lambda state: logic.has_vertical_movement(state) or options.obscureRoutes.value == options.obscureRoutes.option_true})
    fancy_add_exits(world, PROVING_MEADOWS_AP_REGION, [DELENDE_AP_REGION, THE_PALE_GROTTO_AP_REGION, PROVING_MEADOWS_SKUMPARADISE_CONNECTOR_AP_REGION, THE_OPEN_SEA_AP_REGION],
                    {THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state)})
    #A Proving Meadows <-> Skumparadise connector; untraversable w/o a region pass in Regionsanity
    fancy_add_exits(world, PROVING_MEADOWS_SKUMPARADISE_CONNECTOR_AP_REGION, [PROVING_MEADOWS_AP_REGION, SKUMPARADISE_AP_REGION],
                    {PROVING_MEADOWS_AP_REGION: lambda state: logic.has_jobs(state, 3),
                     SKUMPARADISE_AP_REGION: lambda state: logic.has_jobs(state, 3)})
    fancy_add_exits(world, SKUMPARADISE_AP_REGION, [PROVING_MEADOWS_SKUMPARADISE_CONNECTOR_AP_REGION, CAPITAL_SEQUOIA_AP_REGION])
    fancy_add_exits(world, CAPITAL_SEQUOIA_AP_REGION, [PROVING_MEADOWS_AP_REGION, JOJO_SEWERS_AP_REGION, BOOMER_SOCIETY_AP_REGION, ROLLING_QUINTAR_FIELDS_AP_REGION, COBBLESTONE_CRAG_AP_REGION, GREENSHIRE_REPRISE_AP_REGION, CASTLE_SEQUOIA_AP_REGION, SKUMPARADISE_AP_REGION],
                    # why rental and horizontal both listed?
                    {BOOMER_SOCIETY_AP_REGION: lambda state: logic.has_vertical_movement(state) or logic.has_glide(state),
                     COBBLESTONE_CRAG_AP_REGION: lambda state: logic.has_key(state, COURTYARD_KEY) or logic.has_rental_quintar(state, ROLLING_QUINTAR_FIELDS_DISPLAY_NAME) or logic.has_horizontal_movement(state),
                     GREENSHIRE_REPRISE_AP_REGION: lambda state: logic.has_jobs(state, 5),
                     #note for eme: technically possible to get into the first dungeon with quintar instead of glide, but it's hard lol; come from Quintar Sanctum save point and go west up mountain and fall down through grate (that part's easy) then the quintar jump to the lamp is hard
                     CASTLE_SEQUOIA_AP_REGION: lambda state: logic.has_vertical_movement(state) or logic.has_glide(state)})
    fancy_add_exits(world, JOJO_SEWERS_AP_REGION, [CAPITAL_SEQUOIA_AP_REGION, SEWERS_PAST_SECRET_PASSWORD_AP_REGION, THE_PALE_GROTTO_AP_REGION, CAPITAL_JAIL_AP_REGION, QUINTAR_NEST_AP_REGION],
                    {SEWERS_PAST_SECRET_PASSWORD_AP_REGION: lambda state: state.has(JOJO_SEWERS_PASS, player) or logic.options.regionsanity.value == logic.options.regionsanity.option_false or logic.has_swimming(state),
                     CAPITAL_JAIL_AP_REGION: lambda state: logic.has_rental_quintar(state, ROLLING_QUINTAR_FIELDS_DISPLAY_NAME) or logic.has_swimming(state),
                     THE_PALE_GROTTO_AP_REGION: lambda state: logic.has_swimming(state),
                     QUINTAR_NEST_AP_REGION: lambda state: (logic.has_rental_quintar(state, ROLLING_QUINTAR_FIELDS_DISPLAY_NAME) or logic.has_swimming(state))})
    fancy_add_exits(world, SEWERS_PAST_SECRET_PASSWORD_AP_REGION, [JOJO_SEWERS_AP_REGION, BOOMER_SOCIETY_AP_REGION],
                    {JOJO_SEWERS_AP_REGION: lambda state: state.has(JOJO_SEWERS_PASS, player) or logic.options.regionsanity.value == logic.options.regionsanity.option_false or logic.has_swimming(state)})
    fancy_add_exits(world, BOOMER_SOCIETY_AP_REGION, [CAPITAL_SEQUOIA_AP_REGION, SEWERS_PAST_SECRET_PASSWORD_AP_REGION, GREENSHIRE_REPRISE_AP_REGION])
    fancy_add_exits(world, ROLLING_QUINTAR_FIELDS_AP_REGION, [CAPITAL_SEQUOIA_AP_REGION, QUINTAR_NEST_AP_REGION, QUINTAR_SANCTUM_AP_REGION, QUINTAR_RESERVE_AP_REGION],
                    {QUINTAR_SANCTUM_AP_REGION: lambda state: (logic.has_rental_quintar(state, ROLLING_QUINTAR_FIELDS_DISPLAY_NAME) or logic.has_vertical_movement(state)),
                     QUINTAR_RESERVE_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, QUINTAR_NEST_AP_REGION, [QUINTAR_SANCTUM_AP_REGION, COBBLESTONE_CRAG_AP_REGION, JOJO_SEWERS_AP_REGION],
                    {QUINTAR_SANCTUM_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, QUINTAR_SANCTUM_AP_REGION, [ROLLING_QUINTAR_FIELDS_AP_REGION, QUINTAR_NEST_AP_REGION, QUINTAR_MAUSOLEUM_AP_REGION],
                    {QUINTAR_MAUSOLEUM_AP_REGION: lambda state: logic.has_swimming(state),
                     QUINTAR_NEST_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, CAPITAL_JAIL_AP_REGION, [JOJO_SEWERS_AP_REGION, JAIL_SOUTH_WING_AP_REGION],
                    {JAIL_SOUTH_WING_AP_REGION: lambda state: logic.has_key(state, SOUTH_WING_KEY)})
    fancy_add_exits(world, JAIL_SOUTH_WING_AP_REGION, [CAPITAL_JAIL_AP_REGION, JAIL_SOUTH_WING_RUBBLE_AP_REGION],
                    {CAPITAL_JAIL_AP_REGION: lambda state: logic.has_key(state, SOUTH_WING_KEY),
                     JAIL_SOUTH_WING_RUBBLE_AP_REGION: lambda state: logic.has_key(state, CELL_KEY, 6)})
    fancy_add_exits(world, JAIL_SOUTH_WING_RUBBLE_AP_REGION, [JAIL_SOUTH_WING_AP_REGION, PIPELINE_NORTH_AP_REGION],
                    {JAIL_SOUTH_WING_AP_REGION: lambda state: logic.has_key(state, CELL_KEY, 6)})
    fancy_add_exits(world, PIPELINE_NORTH_AP_REGION, [PIPELINE_SOUTH_AP_REGION, JAIL_SOUTH_WING_RUBBLE_AP_REGION],
                    {PIPELINE_SOUTH_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, PIPELINE_SOUTH_AP_REGION, [PIPELINE_NORTH_AP_REGION, CONTINENTAL_TRAM_AP_REGION, PIPELINE_JIDAMBA_CONNECTOR_AP_REGION])
    #A Pipeline <-> Jidamba connector; untraversable w/o region pass in Regionsanity
    fancy_add_exits(world, PIPELINE_JIDAMBA_CONNECTOR_AP_REGION, [PIPELINE_SOUTH_AP_REGION, JIDAMBA_CAVE_AP_REGION])
    fancy_add_exits(world, COBBLESTONE_CRAG_AP_REGION, [CAPITAL_SEQUOIA_AP_REGION, THE_OPEN_SEA_AP_REGION, SHOUDU_WATERFRONT_AP_REGION, OKIMOTO_NS_AP_REGION],
                    {SHOUDU_WATERFRONT_AP_REGION: lambda state: logic.has_horizontal_movement(state),
                     OKIMOTO_NS_AP_REGION: lambda state: logic.has_horizontal_movement(state),
                     THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, OKIMOTO_NS_AP_REGION, [COBBLESTONE_CRAG_AP_REGION, THE_OPEN_SEA_AP_REGION, FLYERS_CRAG_AP_REGION],
                    {THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state),
                     FLYERS_CRAG_AP_REGION: lambda state: (logic.has_glide(state) and logic.has_vertical_movement(state)) or logic.has_swimming(state)})
    fancy_add_exits(world, GREENSHIRE_REPRISE_AP_REGION, [CAPITAL_SEQUOIA_AP_REGION, SALMON_PASS_AP_REGION, TALL_TALL_HEIGHTS_AP_REGION],
                    # if we add hard logic, it is possible to jump from the rolling quintar fields onto the cap seq walls from the southeast and manage to bypass the guard and thus the job requirement
                    {SALMON_PASS_AP_REGION: lambda state: (logic.has_rental_quintar(state, ROLLING_QUINTAR_FIELDS_DISPLAY_NAME) and logic.has_jobs(state, 5)) or logic.has_vertical_movement(state),
                     TALL_TALL_HEIGHTS_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, SALMON_PASS_AP_REGION, [GREENSHIRE_REPRISE_AP_REGION, SALMON_RIVER_AP_REGION, DELENDE_AP_REGION],
                    {GREENSHIRE_REPRISE_AP_REGION: lambda state: (logic.has_horizontal_movement(state) or logic.has_swimming(state)),
                     SALMON_RIVER_AP_REGION: lambda state: logic.has_horizontal_movement(state) or logic.has_swimming(state),
                     DELENDE_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, SALMON_RIVER_AP_REGION, [SALMON_PASS_AP_REGION, SALMON_BAY_AP_REGION, TALL_TALL_HEIGHTS_AP_REGION],
                    {SALMON_BAY_AP_REGION: lambda state: (logic.has_vertical_movement(state) and logic.has_glide(state)) or logic.has_swimming(state),
                     TALL_TALL_HEIGHTS_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, POKO_POKO_DESERT_AP_REGION, [SARA_SARA_BAZAAR_AP_REGION, ANCIENT_RESERVOIR_AP_REGION, LAKE_DELENDE_AP_REGION, SALMON_BAY_AP_REGION, ANCIENT_LABYRINTH_AP_REGION],
                    {ANCIENT_RESERVOIR_AP_REGION: lambda state: logic.has_key(state, PYRAMID_KEY),
                     LAKE_DELENDE_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     SALMON_BAY_AP_REGION: lambda state: logic.has_horizontal_movement(state) and logic.has_vertical_movement(state),
                     ANCIENT_LABYRINTH_AP_REGION: lambda state: (state.has(ANCIENT_TABLET_A, player) or options.obscureRoutes.value == options.obscureRoutes.option_true) and logic.has_vertical_movement(state) and logic.has_glide(state)})
    fancy_add_exits(world, SARA_SARA_BAZAAR_AP_REGION, [POKO_POKO_DESERT_AP_REGION, SARA_SARA_BEACH_EAST_AP_REGION, SARA_SARA_BEACH_WEST_AP_REGION, SHOUDU_PROVINCE_AP_REGION, THE_OPEN_SEA_AP_REGION, CONTINENTAL_TRAM_AP_REGION],
                    {SARA_SARA_BEACH_WEST_AP_REGION: lambda state: logic.has_rental_quintar(state, SARA_SARA_BAZAAR_DISPLAY_NAME),
                     SHOUDU_PROVINCE_AP_REGION: lambda state: state.has(FERRY_PASS, player),
                     THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state),
                     CONTINENTAL_TRAM_AP_REGION: lambda state: logic.has_swimming(state) or logic.has_key(state, TRAM_KEY)})
    fancy_add_exits(world, SARA_SARA_BEACH_EAST_AP_REGION, [SARA_SARA_BAZAAR_AP_REGION, THE_OPEN_SEA_AP_REGION, IBEK_CAVE_AP_REGION, BEAURIOR_VOLCANO_AP_REGION],
                    {IBEK_CAVE_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state),
                     BEAURIOR_VOLCANO_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, SARA_SARA_BEACH_WEST_AP_REGION, [POKO_POKO_DESERT_AP_REGION, SARA_SARA_BAZAAR_AP_REGION, THE_OPEN_SEA_AP_REGION],
                    {POKO_POKO_DESERT_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     SARA_SARA_BAZAAR_AP_REGION: lambda state: logic.has_horizontal_movement(state),
                     THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, ANCIENT_RESERVOIR_AP_REGION, [POKO_POKO_DESERT_AP_REGION, IBEK_CAVE_AP_REGION, BELOW_GRAN_AP_REGION],
                    {IBEK_CAVE_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     BELOW_GRAN_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, IBEK_CAVE_AP_REGION, [SARA_SARA_BEACH_EAST_AP_REGION],
                    {SARA_SARA_BEACH_EAST_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, SALMON_BAY_AP_REGION, [THE_OPEN_SEA_AP_REGION, SALMON_RIVER_AP_REGION],
                    {THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state),
                     SALMON_RIVER_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, THE_OPEN_SEA_AP_REGION, [SEASIDE_CLIFFS_AP_REGION, PROVING_MEADOWS_AP_REGION, OKIMOTO_NS_AP_REGION, SHOUDU_WATERFRONT_AP_REGION, SARA_SARA_BAZAAR_AP_REGION, SARA_SARA_BEACH_EAST_AP_REGION, SARA_SARA_BEACH_WEST_AP_REGION, SALMON_BAY_AP_REGION, SHOUDU_PROVINCE_AP_REGION, THE_UNDERCITY_AP_REGION, JIDAMBA_ATOLLS_AP_REGION, JIDAMBA_WATERWAYS_AP_REGION, THE_DEEP_SEA_AP_REGION],
                    {SEASIDE_CLIFFS_AP_REGION: lambda state: logic.has_swimming(state),
                     PROVING_MEADOWS_AP_REGION: lambda state: logic.has_swimming(state),
                     OKIMOTO_NS_AP_REGION: lambda state: logic.has_swimming(state),
                     SHOUDU_WATERFRONT_AP_REGION: lambda state: logic.has_swimming(state),
                     THE_UNDERCITY_AP_REGION: lambda state: logic.has_swimming(state),
                     SARA_SARA_BAZAAR_AP_REGION: lambda state: logic.has_swimming(state),
                     SARA_SARA_BEACH_EAST_AP_REGION: lambda state: logic.has_swimming(state),
                     SARA_SARA_BEACH_WEST_AP_REGION: lambda state: logic.has_swimming(state),
                     SALMON_BAY_AP_REGION: lambda state: logic.has_swimming(state),
                     SHOUDU_PROVINCE_AP_REGION: lambda state: logic.has_swimming(state),
                     JIDAMBA_ATOLLS_AP_REGION: lambda state: logic.has_swimming(state),
                     JIDAMBA_WATERWAYS_AP_REGION: lambda state: logic.has_swimming(state),
                     THE_DEEP_SEA_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, JIDAMBA_ATOLLS_AP_REGION, [JIDAMBA_FOREST_FLOOR_AP_REGION, THE_OPEN_SEA_AP_REGION],
                    {JIDAMBA_FOREST_FLOOR_AP_REGION: lambda state: logic.has_glide(state),
                     THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, SHOUDU_WATERFRONT_AP_REGION, [THE_OPEN_SEA_AP_REGION, SHOUDU_PROVINCE_AP_REGION, COBBLESTONE_CRAG_AP_REGION],
                    {THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state),
                     SHOUDU_PROVINCE_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     COBBLESTONE_CRAG_AP_REGION: lambda state: logic.has_horizontal_movement(state)})
    fancy_add_exits(world, SHOUDU_PROVINCE_AP_REGION, [SARA_SARA_BAZAAR_AP_REGION, SHOUDU_WATERFRONT_AP_REGION, GANYMEDE_SHRINE_AP_REGION, THE_UNDERCITY_AP_REGION, QUINTAR_RESERVE_AP_REGION],
                    {SARA_SARA_BAZAAR_AP_REGION: lambda state: state.has(FERRY_PASS, player),
                     GANYMEDE_SHRINE_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     QUINTAR_RESERVE_AP_REGION: lambda state: logic.has_vertical_movement(state) and state.has(ELEVATOR_PART, player, 10)})
    fancy_add_exits(world, THE_UNDERCITY_AP_REGION, [SHOUDU_PROVINCE_AP_REGION, THE_OPEN_SEA_AP_REGION],
                    {THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, GANYMEDE_SHRINE_AP_REGION, [SHOUDU_PROVINCE_AP_REGION])
    fancy_add_exits(world, BEAURIOR_VOLCANO_AP_REGION, [SARA_SARA_BEACH_EAST_AP_REGION, BEAURIOR_ROCK_AP_REGION, THE_OPEN_SEA_AP_REGION],
                    {BEAURIOR_ROCK_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, BEAURIOR_ROCK_AP_REGION, [BEAURIOR_VOLCANO_AP_REGION])
    fancy_add_exits(world, LAKE_DELENDE_AP_REGION, [POKO_POKO_DESERT_AP_REGION, DELENDE_AP_REGION],
                    {POKO_POKO_DESERT_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     DELENDE_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, QUINTAR_RESERVE_AP_REGION, [SHOUDU_PROVINCE_AP_REGION, DIONE_SHRINE_AP_REGION, QUINTAR_MAUSOLEUM_AP_REGION],
                    {QUINTAR_MAUSOLEUM_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, DIONE_SHRINE_AP_REGION, [QUINTAR_RESERVE_AP_REGION, EASTERN_CHASM_AP_REGION, JIDAMBA_SUMMIT_AP_REGION, THE_CHALICE_OF_TAR_AP_REGION],
                    {JIDAMBA_SUMMIT_AP_REGION: lambda state: logic.has_glide(state),
                     THE_CHALICE_OF_TAR_AP_REGION: lambda state: logic.has_glide(state) and state.has(DIONE_STONE, player),
                     EASTERN_CHASM_AP_REGION: lambda state: logic.has_glide(state) and logic.has_vertical_movement(state)})
    fancy_add_exits(world, QUINTAR_MAUSOLEUM_AP_REGION, [QUINTAR_RESERVE_AP_REGION, QUINTAR_SANCTUM_AP_REGION],
                    {QUINTAR_RESERVE_AP_REGION: lambda state: logic.has_swimming(state),
                     QUINTAR_SANCTUM_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, EASTERN_CHASM_AP_REGION, [QUINTAR_RESERVE_AP_REGION, THE_OPEN_SEA_AP_REGION],
                    {QUINTAR_RESERVE_AP_REGION: lambda state: logic.has_glide(state),
                     THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, TALL_TALL_HEIGHTS_AP_REGION, [SALMON_RIVER_AP_REGION, GREENSHIRE_REPRISE_AP_REGION, LANDS_END_AP_REGION, SEQUOIA_ATHENAEUM_AP_REGION, NORTHERN_STRETCH_AP_REGION, CASTLE_RAMPARTS_AP_REGION, THE_CHALICE_OF_TAR_AP_REGION, THE_PALE_GROTTO_AP_REGION, NORTHERN_CAVE_AP_REGION],
                    {LANDS_END_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     SEQUOIA_ATHENAEUM_AP_REGION: lambda state: state.has(VERMILLION_BOOK, player) and state.has(VIRIDIAN_BOOK, player) and state.has(CERULEAN_BOOK, player),
                     NORTHERN_STRETCH_AP_REGION: lambda state: logic.has_glide(state),
                     CASTLE_RAMPARTS_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     THE_PALE_GROTTO_AP_REGION: lambda state: logic.has_swimming(state),
                     THE_CHALICE_OF_TAR_AP_REGION: lambda state: logic.has_glide(state) and logic.has_vertical_movement(state)})
    fancy_add_exits(world, NORTHERN_CAVE_AP_REGION, [TALL_TALL_HEIGHTS_AP_REGION, SLIP_GLIDE_RIDE_AP_REGION],
                    {SLIP_GLIDE_RIDE_AP_REGION: lambda state: logic.has_glide(state) and logic.has_vertical_movement(state),
                     TALL_TALL_HEIGHTS_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, LANDS_END_AP_REGION, [TALL_TALL_HEIGHTS_AP_REGION, JIDAMBA_SUMMIT_AP_REGION],
                    {JIDAMBA_SUMMIT_AP_REGION: lambda state: logic.has_glide(state),
                     TALL_TALL_HEIGHTS_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, SLIP_GLIDE_RIDE_AP_REGION, [TALL_TALL_HEIGHTS_AP_REGION, NORTHERN_CAVE_AP_REGION],
                    {NORTHERN_CAVE_AP_REGION: lambda state: logic.has_glide(state),
                     TALL_TALL_HEIGHTS_AP_REGION: lambda state: logic.has_vertical_movement(state) and logic.has_glide(state)})
    fancy_add_exits(world, SEQUOIA_ATHENAEUM_AP_REGION, [TALL_TALL_HEIGHTS_AP_REGION],
                    {TALL_TALL_HEIGHTS_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, NORTHERN_STRETCH_AP_REGION, [TALL_TALL_HEIGHTS_AP_REGION, THE_OPEN_SEA_AP_REGION],
                    {THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state),
                     TALL_TALL_HEIGHTS_AP_REGION: lambda state: logic.has_vertical_movement(state)})
    fancy_add_exits(world, CASTLE_RAMPARTS_AP_REGION, [TALL_TALL_HEIGHTS_AP_REGION, CASTLE_SEQUOIA_AP_REGION],
                    {TALL_TALL_HEIGHTS_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     CASTLE_SEQUOIA_AP_REGION: lambda state: logic.has_vertical_movement(state) and logic.has_glide(state)})
    fancy_add_exits(world, THE_CHALICE_OF_TAR_AP_REGION, [TALL_TALL_HEIGHTS_AP_REGION, QUINTAR_RESERVE_AP_REGION],
                    {TALL_TALL_HEIGHTS_AP_REGION: lambda state: logic.has_glide(state),
                     QUINTAR_RESERVE_AP_REGION: lambda state: logic.has_glide(state)})
    fancy_add_exits(world, FLYERS_CRAG_AP_REGION, [OKIMOTO_NS_AP_REGION, JIDAMBA_SUMMIT_AP_REGION],
                    {JIDAMBA_SUMMIT_AP_REGION: lambda state: logic.has_glide(state)})
    #Jidamba Tangle section start
    fancy_add_exits(world, JIDAMBA_FOREST_FLOOR_AP_REGION, [JIDAMBA_DIAMONDSMITH_AP_REGION, JIDAMBA_SOUTHWEST_BEACH_AP_REGION, EUROPA_SHRINE_AP_REGION, JIDAMBA_CANOPY_AP_REGION, JIDAMBA_WATERWAYS_AP_REGION],
                    #if we change the elevators to Pipeline to always be powered, then add an exit to Pipeline Jidamba Connector
                    {JIDAMBA_DIAMONDSMITH_AP_REGION: lambda state: logic.has_glide(state),
                     JIDAMBA_SOUTHWEST_BEACH_AP_REGION: lambda state: logic.has_glide(state),
                     EUROPA_SHRINE_AP_REGION: lambda state: logic.has_glide(state),
                     JIDAMBA_CANOPY_AP_REGION: lambda state: logic.has_vertical_movement(state),
                     JIDAMBA_WATERWAYS_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, JIDAMBA_DIAMONDSMITH_AP_REGION, [JIDAMBA_FOREST_FLOOR_AP_REGION, JIDAMBA_ATOLLS_AP_REGION, JIDAMBA_CANOPY_AP_REGION],
                    {JIDAMBA_ATOLLS_AP_REGION: lambda state: logic.has_glide(state)})
    fancy_add_exits(world, JIDAMBA_SOUTHWEST_BEACH_AP_REGION,[JIDAMBA_FOREST_FLOOR_AP_REGION, JIDAMBA_WATERWAYS_AP_REGION],
                    {JIDAMBA_FOREST_FLOOR_AP_REGION: lambda state: logic.has_glide(state),
                     JIDAMBA_WATERWAYS_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, EUROPA_SHRINE_AP_REGION, [JIDAMBA_FOREST_FLOOR_AP_REGION, JIDAMBA_CAVE_AP_REGION, JIDAMBA_SOUTH_CLIFF_AP_REGION, JIDAMBA_SUMMIT_AP_REGION],
                    {JIDAMBA_CAVE_AP_REGION: lambda state: logic.has_vertical_movement(state) or logic.has_glide(state),
                     JIDAMBA_SOUTH_CLIFF_AP_REGION: lambda state: logic.has_glide(state),
                     JIDAMBA_SUMMIT_AP_REGION: lambda state: logic.has_glide(state)})
    fancy_add_exits(world, JIDAMBA_CAVE_AP_REGION, [EUROPA_SHRINE_AP_REGION, JIDAMBA_SOUTHWEST_BEACH_CLIFF_AP_REGION, JIDAMBA_SUMMIT_AP_REGION],
                    {EUROPA_SHRINE_AP_REGION: lambda state: logic.has_glide(state),
                     JIDAMBA_SOUTHWEST_BEACH_CLIFF_AP_REGION: lambda state: logic.has_glide(state),
                     JIDAMBA_SUMMIT_AP_REGION: lambda state: logic.has_glide(state)})
    fancy_add_exits(world, JIDAMBA_SOUTH_CLIFF_AP_REGION, [JIDAMBA_FOREST_FLOOR_AP_REGION, JIDAMBA_DIAMONDSMITH_AP_REGION, EUROPA_SHRINE_AP_REGION, JIDAMBA_EACLANEYA_COURTYARD_AP_REGION, JIDAMBA_SOUTHWEST_BEACH_CLIFF_AP_REGION, JIDAMBA_WATERWAYS_AP_REGION],
                    {JIDAMBA_DIAMONDSMITH_AP_REGION: lambda state: logic.has_horizontal_movement(state),
                     EUROPA_SHRINE_AP_REGION: lambda state: logic.has_vertical_movement(state) or logic.has_glide(state),
                     JIDAMBA_SOUTHWEST_BEACH_CLIFF_AP_REGION: lambda state: logic.has_horizontal_movement(state) or logic.has_vertical_movement(state),
                     JIDAMBA_WATERWAYS_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, JIDAMBA_EACLANEYA_COURTYARD_AP_REGION, [JIDAMBA_SOUTH_CLIFF_AP_REGION, JIDAMBA_SOUTHWEST_BEACH_CLIFF_AP_REGION, JIDAMBA_SUMMIT_AP_REGION, JIDAMBA_WATERWAYS_AP_REGION],
                    {JIDAMBA_SOUTHWEST_BEACH_CLIFF_AP_REGION: lambda state: logic.has_horizontal_movement(state) or logic.has_vertical_movement(state),
                     JIDAMBA_SUMMIT_AP_REGION: lambda state: logic.has_vertical_movement(state) or logic.has_glide(state),
                     JIDAMBA_WATERWAYS_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, JIDAMBA_SOUTHWEST_BEACH_CLIFF_AP_REGION, [JIDAMBA_SOUTHWEST_BEACH_AP_REGION, JIDAMBA_CAVE_AP_REGION, JIDAMBA_SOUTH_CLIFF_AP_REGION, JIDAMBA_EACLANEYA_COURTYARD_AP_REGION, JIDAMBA_SUMMIT_AP_REGION, JIDAMBA_WATERWAYS_AP_REGION],
                    {JIDAMBA_SOUTH_CLIFF_AP_REGION: lambda state: logic.has_vertical_movement(state) or logic.has_horizontal_movement(state),
                     JIDAMBA_EACLANEYA_COURTYARD_AP_REGION: lambda state: logic.has_vertical_movement(state) or logic.has_horizontal_movement(state),
                     JIDAMBA_SUMMIT_AP_REGION: lambda state: logic.has_glide(state),
                     JIDAMBA_WATERWAYS_AP_REGION: lambda state: logic.has_swimming(state)})
    #The one-way Tangle -> Eaclaneya connector is logically connected from the Summit because the Canopy door you need to unlock & switch you need to press is up there, even though the physical door to the Eaclaneya is in the Courtyard
    fancy_add_exits(world, JIDAMBA_SUMMIT_AP_REGION, [JIDAMBA_FOREST_FLOOR_AP_REGION, EUROPA_SHRINE_AP_REGION, JIDAMBA_CAVE_AP_REGION, JIDAMBA_SOUTH_CLIFF_AP_REGION, JIDAMBA_EACLANEYA_COURTYARD_AP_REGION, JIDAMBA_SOUTHWEST_BEACH_CLIFF_AP_REGION, JIDAMBA_CANOPY_AP_REGION, JIDAMBA_WATERWAYS_AP_REGION, TANGLE_EACLANEYA_CONNECTOR_AP_REGION],
                    {JIDAMBA_WATERWAYS_AP_REGION: lambda state: logic.has_swimming(state)})
    #A one-way Tangle -> Eaclaneya connector; untraversable w/o region pass in Regionsanity
    fancy_add_exits(world, TANGLE_EACLANEYA_CONNECTOR_AP_REGION, [JIDAMBA_EACLANEYA_AP_REGION],
                    {JIDAMBA_EACLANEYA_AP_REGION: lambda state: logic.has_jidamba_keys(state)})
    fancy_add_exits(world, JIDAMBA_CANOPY_AP_REGION, [JIDAMBA_FOREST_FLOOR_AP_REGION, JIDAMBA_DIAMONDSMITH_AP_REGION, EUROPA_SHRINE_AP_REGION, JIDAMBA_SOUTH_CLIFF_AP_REGION, JIDAMBA_SUMMIT_AP_REGION, JIDAMBA_WATERWAYS_AP_REGION],
                    {JIDAMBA_WATERWAYS_AP_REGION: lambda state: logic.has_swimming(state)})
    #I am not listing has_swimming on all these exits; i already wrote a has_swimming rule on every entrance into the Waterways
    fancy_add_exits(world, JIDAMBA_WATERWAYS_AP_REGION, [THE_OPEN_SEA_AP_REGION, JIDAMBA_FOREST_FLOOR_AP_REGION, JIDAMBA_ATOLLS_AP_REGION, JIDAMBA_SOUTHWEST_BEACH_AP_REGION, JIDAMBA_SOUTH_CLIFF_AP_REGION, JIDAMBA_EACLANEYA_COURTYARD_AP_REGION, JIDAMBA_SOUTHWEST_BEACH_CLIFF_AP_REGION, JIDAMBA_SUMMIT_AP_REGION])
    #Jidamba Tangle section end
    #Removed connection from Eaclaneya -> Tangle because you can't go through that door if you haven't hit the switches on the Tangle side
    fancy_add_exits(world, JIDAMBA_EACLANEYA_AP_REGION, [THE_OPEN_SEA_AP_REGION],
                    {THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, THE_DEEP_SEA_AP_REGION, [THE_OPEN_SEA_AP_REGION, NEPTUNE_SHRINE_AP_REGION, THE_DEPTHS_AP_REGION, THE_SEQUOIA_AP_REGION],
                    {THE_OPEN_SEA_AP_REGION: lambda state: logic.has_swimming(state),
                     NEPTUNE_SHRINE_AP_REGION: lambda state: logic.has_swimming(state),
                     THE_DEPTHS_AP_REGION: lambda state: logic.has_swimming(state),
                     THE_SEQUOIA_AP_REGION: lambda state: logic.has_golden_quintar(state)})
    fancy_add_exits(world, NEPTUNE_SHRINE_AP_REGION, [THE_DEEP_SEA_AP_REGION],
                    {THE_DEEP_SEA_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, JADE_CAVERN_AP_REGION, [SOILED_DEN_AP_REGION, BELOW_GRAN_AP_REGION],
                    {SOILED_DEN_AP_REGION: lambda state: logic.has_swimming(state),
                     BELOW_GRAN_AP_REGION: lambda state: logic.has_swimming(state)})
    fancy_add_exits(world, CONTINENTAL_TRAM_AP_REGION, [PIPELINE_SOUTH_AP_REGION, SARA_SARA_BAZAAR_AP_REGION],
                    {SARA_SARA_BAZAAR_AP_REGION: lambda state: logic.has_swimming(state) or state.has(TRAM_KEY, player)})
    fancy_add_exits(world, ANCIENT_LABYRINTH_AP_REGION, [POKO_POKO_DESERT_AP_REGION])
    fancy_add_exits(world, THE_SEQUOIA_AP_REGION, [THE_DEEP_SEA_AP_REGION])
    fancy_add_exits(world, THE_DEPTHS_AP_REGION, [THE_DEEP_SEA_AP_REGION])
    fancy_add_exits(world, CASTLE_SEQUOIA_AP_REGION, [CAPITAL_SEQUOIA_AP_REGION])
    # regions without connections don't get parsed by Jsonifier
    fancy_add_exits(world, THE_NEW_WORLD_AP_REGION, [MENU_AP_REGION])
    fancy_add_exits(world, THE_OLD_WORLD_AP_REGION, [MENU_AP_REGION])
    fancy_add_exits(world, MODDED_ZONE_AP_REGION, [MENU_AP_REGION])

def get_locations_per_ap_region(locations: List[LocationData]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.ap_region, []).append(location)

    return per_region

def create_ap_region(world: "CrystalProjectWorld", player: int, locations_per_region: Dict[str, List[LocationData]], name: str, excluded: bool) -> Tuple[Region, Location | None]:
    """
    Creates an AP Region and returns it, as well as the Location used for region completion
    """
    logic = CrystalProjectLogic(player, world.options)
    ap_region = Region(name, player, world.multiworld)

    region_completion: Location | None = None

    #if the region isn't part of the multiworld, we still make the region so that all the exits still work,
        #but we also don't fill it with locations
    if not excluded:
        if name in locations_per_region:
            for location_data in locations_per_region[name]:
                location = create_location(player, location_data, ap_region)
                ap_region.locations.append(location)
                if location_data.regionsanity:
                    region_completion = location

        # This is for making sure players can earn money for required shop checks in shopsanity + regionsanity
        if world.options.regionsanity.value == world.options.regionsanity.option_true and world.options.shopsanity.value != world.options.shopsanity.option_disabled:
            for location in ap_region.locations:
                if "Shop -" in location.name:
                    location.access_rule = combine_callables(location.access_rule, lambda state: logic.can_earn_money(state, ap_region.name))

    return ap_region, region_completion

def create_display_region(world: "CrystalProjectWorld", player: int, locations_per_region: Dict[str, List[LocationData]], display_region_name: str, excluded: bool) -> List[Region]:
    ap_regions: List[Region] = []
    ap_region_names = display_region_subregions_dictionary[display_region_name]

    region_completion_location = None

    if not excluded:
        world.included_regions.append(display_region_name)

    for ap_region_name in ap_region_names:
        ap_region, region_completion_location_temp = create_ap_region(world, player, locations_per_region, ap_region_name, excluded)
        ap_regions.append(ap_region)
        if not excluded:
            if region_completion_location_temp is not None:
                if region_completion_location is not None:
                    raise Exception(f"Two region completion locations exist inside {display_region_name}")
                region_completion_location = region_completion_location_temp

    #need to add the rule for every other location in the ap region, as well as every location in other ap regions, as well as a can_reach rule on other ap regions in this display region
    # This is for the region completion location
    if not excluded:
        if world.options.regionsanity.value == world.options.regionsanity.option_true and region_completion_location is not None:
            for ap_region_name in display_region_subregions_dictionary[display_region_name]:
                ap_region = Region(ap_region_name, player, world.multiworld)
                region_completion_location.access_rule = combine_callables(region_completion_location.access_rule, lambda state, lambda_region_name = ap_region_name: state.can_reach(lambda_region_name, player=player))
                for location in ap_region.locations:
                    if location != region_completion_location:
                        region_completion_location.access_rule = combine_callables(region_completion_location.access_rule, location.access_rule)

    return ap_regions

def create_location(player: int, location_data: LocationData, region: Region) -> Location:
    location = CrystalProjectLocation(player, location_data.name, location_data.code, region)

    if location_data.rule:
        location.access_rule = location_data.rule

    return location

def combine_callables(callable1: Callable[[CollectionState], bool], callable2: Callable[[CollectionState], bool]) -> Callable[[CollectionState], bool]:
    return lambda state, a=callable1, b=callable2: a(state) and b(state)

def fancy_add_exits(self, region: str, exits: List[str],
                    rules: Dict[str, Callable[[CollectionState], bool]] | None = None):
    if rules is not None:
        for region_rule in rules:
            if not region_rule in exits:
                raise Exception(f"A rule was defined for the entrance {region} -> {region_rule} but {region_rule} isn't in the list of exits from {region}")

    for destination_ap_region in exits:
        destination_display_region = ap_region_to_display_region_dictionary[destination_ap_region]
        if rules is None:
            rules = {}
        if destination_ap_region in rules:
            rules[destination_ap_region] = combine_callables(rules[destination_ap_region], rules_on_display_regions[destination_display_region])
        else:
            rules[destination_ap_region] = rules_on_display_regions[destination_display_region]

    # all regions except Menu have an exit to menu
    if region != MENU_AP_REGION:
        exits.append(MENU_AP_REGION)

    self.multiworld.get_region(region, self.player).add_exits(exits, rules)

def connect_menu_region(world: "CrystalProjectWorld", options: CrystalProjectOptions) -> None:
    logic = CrystalProjectLogic(world.player, options)

    fancy_add_exits(world, MENU_AP_REGION, [SPAWNING_MEADOWS_AP_REGION, CAPITAL_SEQUOIA_AP_REGION, MERCURY_SHRINE_AP_REGION, SALMON_RIVER_AP_REGION, POKO_POKO_DESERT_AP_REGION, GANYMEDE_SHRINE_AP_REGION, DIONE_SHRINE_AP_REGION, TALL_TALL_HEIGHTS_AP_REGION, LANDS_END_AP_REGION, EUROPA_SHRINE_AP_REGION, NEPTUNE_SHRINE_AP_REGION, THE_OLD_WORLD_AP_REGION, THE_NEW_WORLD_AP_REGION, MODDED_ZONE_AP_REGION],
                    # If regionsanity is enabled it will set its own origin region, if it isn't we should connect menu to spawning meadows
                    {SPAWNING_MEADOWS_AP_REGION: lambda state: options.regionsanity.value == options.regionsanity.option_false,
                     CAPITAL_SEQUOIA_AP_REGION: lambda state: state.has(GAEA_STONE, world.player),
                     MERCURY_SHRINE_AP_REGION: lambda state: state.has(MERCURY_STONE, world.player),
                     SALMON_RIVER_AP_REGION: lambda state: state.has(POSEIDON_STONE, world.player),
                     POKO_POKO_DESERT_AP_REGION: lambda state: state.has(MARS_STONE, world.player),
                     GANYMEDE_SHRINE_AP_REGION: lambda state: state.has(GANYMEDE_STONE, world.player),
                     DIONE_SHRINE_AP_REGION: lambda state: state.has(DIONE_STONE, world.player),
                     TALL_TALL_HEIGHTS_AP_REGION: lambda state: state.has(TRITON_STONE, world.player),
                     LANDS_END_AP_REGION: lambda state: state.has(CALLISTO_STONE, world.player),
                     EUROPA_SHRINE_AP_REGION: lambda state: state.has(EUROPA_STONE, world.player),
                     NEPTUNE_SHRINE_AP_REGION: lambda state: state.has(NEPTUNE_STONE, world.player),
                     THE_OLD_WORLD_AP_REGION: lambda state: logic.old_world_requirements(state),
                     THE_NEW_WORLD_AP_REGION: lambda state: logic.new_world_requirements(state)})