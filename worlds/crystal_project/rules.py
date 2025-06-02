from .options import CrystalProjectOptions
from .constants.keys import *
from BaseClasses import CollectionState
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from . import CrystalProjectWorld

class CrystalProjectLogic:
    player: int
    options: CrystalProjectOptions

    def __init__(self, player: Optional[int], options: Optional[CrystalProjectOptions]):
        self.player = player
        self.options = options

    def has_jobs(self, state: CollectionState, job_minimum: int) -> bool:
        return self.get_job_count(state) >= job_minimum
    
    def get_job_count(self, state: CollectionState) -> int:
        count = 0
        if state.has("Job - Warrior", self.player):
            count += 1
        if state.has("Job - Monk", self.player):
            count += 1
        if state.has("Job - Rogue", self.player):
            count += 1
        if state.has("Job - Cleric", self.player):
            count += 1
        if state.has("Job - Wizard", self.player):
            count += 1
        if state.has("Job - Warlock", self.player):
            count += 1
        if state.has("Job - Fencer", self.player):
            count += 1
        if state.has("Job - Shaman", self.player):
            count += 1
        if state.has("Job - Scholar", self.player):
            count += 1
        if state.has("Job - Aegis", self.player):
            count += 1
        if state.has("Job - Hunter", self.player):
            count += 1
        if state.has("Job - Chemist", self.player):
            count += 1
        if state.has("Job - Reaper", self.player):
            count += 1
        if state.has("Job - Ninja", self.player):
            count += 1
        if state.has("Job - Nomad", self.player):
            count += 1
        if state.has("Job - Dervish", self.player):
            count += 1
        if state.has("Job - Beatsmith", self.player):
            count += 1
        if state.has("Job - Samurai", self.player):
            count += 1
        if state.has("Job - Assassin", self.player):
            count += 1
        if state.has("Job - Valkyrie", self.player):
            count += 1
        if state.has("Job - Summoner", self.player):
            count += 1
        if state.has("Job - Beastmaster", self.player):
            count += 1
        if state.has("Job - Weaver", self.player):
            count += 1
        if state.has("Job - Mimic", self.player):
            count += 1

        #subtract starting jobs
        return count - self.get_starting_job_count()

    def get_starting_job_count(self):
        if self.options.jobRando.value == self.options.jobRando.option_full:
            return self.options.startingJobQuantity.value
        else:
            return 6

    def has_enough_clamshells(self, state: CollectionState):
        clamshell_quantity = 3
        if self.options.goal.value == self.options.goal.option_clamshells:
            clamshell_quantity = self.options.clamshellGoalQuantity.value
        return state.has("Item - Clamshell", self.player, clamshell_quantity)

    def has_rental_quintar(self, state: CollectionState) -> bool:
        return state.has_any({"Item - Progressive Quintar Flute"}, self.player) or state.has("Item - Owl Drum", self.player)

    def has_horizontal_movement(self, state: CollectionState) -> bool:
        return state.has("Item - Progressive Quintar Flute", self.player, 2) or state.has("Item - Owl Drum", self.player)

    def has_vertical_movement(self, state: CollectionState) -> bool:
        return state.has("Item - Ibek Bell", self.player)

    def has_glide(self, state: CollectionState) -> bool: 
        return state.has("Item - Owl Drum", self.player) or state.has("Item - Progressive Quintar Flute", self.player, 3)

    def has_swimming(self, state: CollectionState) -> bool:
        return state.has_any({"Item - Progressive Salmon Violin"}, self.player) or state.has("Item - Progressive Quintar Flute", self.player, 3)

    def has_golden_quintar(self, state: CollectionState) -> bool:
        return state.has("Item - Progressive Quintar Flute", self.player, 3)

    def new_world_requirements(self, state: CollectionState) -> bool:
        if self.options.goal.value == self.options.goal.option_astley or self.options.goal.value == self.options.goal.option_true_astley:
            return self.has_jobs(state, self.options.newWorldStoneJobQuantity.value)    
        else:
            return state.has("Item - New World Stone", self.player)

    def old_world_requirements(self, state: CollectionState) -> bool:
        if self.options.goal.value == self.options.goal.option_true_astley:
            return self.has_swimming(state) and state.has("Item - Deity Eye", self.player, 4) and state.has("Item - STEM WARD", self.player)
        else:
            return state.has("Item - Old World Stone", self.player)

    def is_area_in_level_range(self, state: CollectionState, count: int) -> bool:
        if self.options.levelGating:
            return state.has("Item - Progressive Level Cap", self.player, count)
        return True

    #has_key is for: Luxury Key, Gardeners Key, All Wing Keys, Cell Keys, Room One Key, Small Keys, Boss Key, Red Door Keys,
    #Ice Puzzle Keys, Rampart Key, Forgotten Key, Tram Key, Courtyard Key, Pyramid Key
    def has_key(self, state: CollectionState, key_name: str, count: int = 1) -> bool:
        if state.has(SKELETON_KEY, self.player):
            return True
        if (self.options.keyMode.value == self.options.keyMode.option_key_ring or
            self.options.keyMode.value == self.options.keyMode.option_key_ring_skelefree):
            return self.has_key_ring(state, key_name)
        return state.has(key_name, self.player, count)

    def has_key_ring(self, state: CollectionState, key_name: str) -> bool:
        if (key_name == GARDENERS_KEY
                or key_name == COURTYARD_KEY
                or key_name == LUXURY_KEY
                or key_name == ROOM_ONE_KEY
                or key_name == PYRAMID_KEY
                or key_name == TRAM_KEY
                or key_name == ICE_CELL_KEY
                or key_name == RAMPART_KEY
                or key_name == FORGOTTEN_KEY):
            return state.has(key_name, self.player)

        if (key_name == CELL_KEY
                or key_name == SOUTH_WING_KEY
                or key_name == EAST_WING_KEY
                or key_name == WEST_WING_KEY
                or key_name == DARK_WING_KEY):
            return state.has(PRISON_KEY_RING, self.player)

        if (key_name == BEAURIOR_BOSS_KEY
                or key_name == SMALL_KEY):
            return state.has(BEAURIOR_KEY_RING, self.player)

        if key_name == RED_DOOR_KEY:
            return state.has(SLIP_GLIDE_RIDE_KEY_RING, self.player)

        if key_name == ICE_PUZZLE_KEY:
            return state.has(ICE_PUZZLE_KEY_RING, self.player)

        if (key_name == FOLIAGE_KEY
                or key_name == CANOPY_KEY
                or key_name == CAVE_KEY):
            return state.has(JIDAMBA_KEY_RING, self.player)

        return False

    def has_jidamba_keys(self, state: CollectionState) -> bool:
        if self.has_key(state, FOLIAGE_KEY, 1) and self.has_key(state, CAVE_KEY, 1) and self.has_key(state, CANOPY_KEY,1):
            return True
        else:
            return False