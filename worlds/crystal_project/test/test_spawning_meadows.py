from ..constants.regions import *
from ..constants.key_items import *
from ..constants.mounts import *
from .bases import CrystalProjectTestBase

class TestSpawningMeadows(CrystalProjectTestBase):
    def test_region_accessibility(self):
        self.assertTrue(self.can_reach_region(SPAWNING_MEADOWS))

    def test_region_connections_no_items(self):
        self.assert_region_entrances(SPAWNING_MEADOWS, reachable_regions=(DELENDE,), unreachable_regions=(MERCURY_SHRINE,POKO_POKO_DESERT,CONTINENTAL_TRAM,BEAURIOR_VOLCANO,YAMAGAWA_MA))

class TestSpawningMeadowsObscureRoutes(CrystalProjectTestBase):
    options = {
        "levelGating": 0,
        "progressiveMountMode": 0,
        "obscureRoutes": 1
    }

    def test_obscure_routes(self):
        unreachable_regions = (MERCURY_SHRINE, CONTINENTAL_TRAM, BEAURIOR_VOLCANO, YAMAGAWA_MA)
        reachable_regions = (DELENDE, POKO_POKO_DESERT,)
        self.assert_region_entrances(SPAWNING_MEADOWS, reachable_regions, unreachable_regions)

        self.collect_by_name(PROGRESSIVE_SALMON_VIOLA)
        unreachable_regions = (MERCURY_SHRINE, BEAURIOR_VOLCANO)
        reachable_regions = (DELENDE, POKO_POKO_DESERT, CONTINENTAL_TRAM, YAMAGAWA_MA)
        self.assert_region_entrances(SPAWNING_MEADOWS, reachable_regions, unreachable_regions)

class TestSpawningMeadowsNoObscureRoutes(CrystalProjectTestBase):
    options = {
        "levelGating": 0,
        "progressiveMountMode": 0,
        "obscureRoutes": 0
    }

    def test_obscure_routes(self):
        unreachable_regions = (MERCURY_SHRINE, POKO_POKO_DESERT, CONTINENTAL_TRAM, BEAURIOR_VOLCANO, YAMAGAWA_MA)
        reachable_regions = (DELENDE,)
        self.assert_region_entrances(SPAWNING_MEADOWS, reachable_regions, unreachable_regions)

        self.collect(self.get_item_by_name(IBEK_BELL))
        unreachable_regions = (CONTINENTAL_TRAM,)
        reachable_regions = (DELENDE, MERCURY_SHRINE, POKO_POKO_DESERT, BEAURIOR_VOLCANO, YAMAGAWA_MA)
        self.assert_region_entrances(SPAWNING_MEADOWS, reachable_regions, unreachable_regions)

        self.collect_by_name(PROGRESSIVE_SALMON_VIOLA)
        unreachable_regions = (CONTINENTAL_TRAM,)
        reachable_regions = (DELENDE, MERCURY_SHRINE, POKO_POKO_DESERT, BEAURIOR_VOLCANO, YAMAGAWA_MA)
        self.assert_region_entrances(SPAWNING_MEADOWS, reachable_regions, unreachable_regions)

        self.collect_mounts()
        unreachable_regions = (CONTINENTAL_TRAM,)
        reachable_regions = (DELENDE, MERCURY_SHRINE, POKO_POKO_DESERT, BEAURIOR_VOLCANO, YAMAGAWA_MA)
        self.assert_region_entrances(SPAWNING_MEADOWS, reachable_regions, unreachable_regions)

class TestSpawningMeadowsConnectionRulesNoLevelGating(CrystalProjectTestBase):
    options = {
        "levelGating": 0,
        "progressiveMountMode": 0,
        "obscureRoutes": 0
    }

    def test_mercury_shrine_connection(self):
        self.collect_by_name(IBEK_BELL)
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + MERCURY_SHRINE))

    def test_poko_poko_connection(self):
        self.collect_by_name(IBEK_BELL)
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + POKO_POKO_DESERT))

    def test_tram_connection(self):
        self.collect_by_name(PROGRESSIVE_SALMON_VIOLA)
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + CONTINENTAL_TRAM))

    def test_volcano_connection(self):
        self.collect_by_name(IBEK_BELL)
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + BEAURIOR_VOLCANO))

    def test_yamagawa_connection_vertical_movement(self):
        self.collect_by_name(IBEK_BELL)
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + YAMAGAWA_MA))

    def test_yamagawa_connection_swimming_salmon(self):
        self.collect_by_name(PROGRESSIVE_SALMON_VIOLA)
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + YAMAGAWA_MA))

    def test_yamagawa_connection_swimming_quintar(self):
        self.collect_by_name([PROGRESSIVE_QUINTAR_WOODWIND])
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + YAMAGAWA_MA))

class TestSpawningMeadowsConnectionRulesWithLevelGating(CrystalProjectTestBase):
    options = {
        "levelGating": 1,
        "progressiveMountMode": 0,
        "obscureRoutes": 0
    }

    def test_poko_poko_connection_fails_with_ibek_no_level_cap(self):
        self.collect_by_name(IBEK_BELL)
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + POKO_POKO_DESERT))

    def test_poko_poko_connection_fails_with_level_cap_no_ibek(self):
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP, PROGRESSIVE_LEVEL_CAP])
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + POKO_POKO_DESERT))

    def test_poko_poko_connection_succeeds_with_ibek_and_level_cap(self):
        self.collect_by_name(IBEK_BELL)
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP, PROGRESSIVE_LEVEL_CAP])
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + POKO_POKO_DESERT))

    def test_tram_connection_fails_with_salmon_no_level_cap(self):
        self.collect_by_name(PROGRESSIVE_SALMON_VIOLA)
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + CONTINENTAL_TRAM))

    def test_tram_connection_fails_with_quintar_no_level_cap(self):
        self.collect_by_name([PROGRESSIVE_QUINTAR_WOODWIND])
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + CONTINENTAL_TRAM))

    def test_tram_connection_fails_with_level_cap_no_swimming(self):
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP])
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + CONTINENTAL_TRAM))

    def test_tram_connection_fails_with_salmon_and_level_cap(self):
        self.collect_by_name(PROGRESSIVE_SALMON_VIOLA)
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP, PROGRESSIVE_LEVEL_CAP])
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + CONTINENTAL_TRAM))

    def test_tram_connection_fails_with_quintar_and_level_cap(self):
        self.collect_by_name([PROGRESSIVE_QUINTAR_WOODWIND])
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP])
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + CONTINENTAL_TRAM))

    def test_beaurior_volcano_fails_with_ibek_no_level_cap(self):
        self.collect_by_name([IBEK_BELL])
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + BEAURIOR_VOLCANO))

    def test_beaurior_volcano_connection_fails_with_level_cap_no_ibek(self):
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP])
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + BEAURIOR_VOLCANO))

    def test_beaurior_connection_succeeds_with_ibek_and_level_cap(self):
        self.collect_by_name(IBEK_BELL)
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP])
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + BEAURIOR_VOLCANO))

    def test_yamagawa_connection_fails_with_ibek_no_level_cap(self):
        self.collect_by_name([IBEK_BELL])
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + YAMAGAWA_MA))

    def test_yamagawa_connection_fails_with_salmon_no_level_cap(self):
        self.collect_by_name(PROGRESSIVE_SALMON_VIOLA)
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + YAMAGAWA_MA))

    def test_yamagawa_connection_fails_with_quintar_no_level_cap(self):
        self.collect_by_name([PROGRESSIVE_QUINTAR_WOODWIND])
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + YAMAGAWA_MA))

    def test_yamagawa_connection_fails_with_level_cap_no_mounts(self):
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP])
        self.assertFalse(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + YAMAGAWA_MA))

    def test_yamagawa_connection_succeeds_with_level_cap_and_ibek(self):
        self.collect_by_name([IBEK_BELL])
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP])
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + YAMAGAWA_MA))

    def test_yamagawa_connection_succeeds_with_level_cap_and_salmon(self):
        self.collect_by_name([PROGRESSIVE_SALMON_VIOLA])
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP])
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + YAMAGAWA_MA))

    def test_yamagawa_connection_succeeds_with_level_cap_and_quintar(self):
        self.collect_by_name([PROGRESSIVE_QUINTAR_WOODWIND])
        self.collect_by_name([PROGRESSIVE_LEVEL_CAP])
        self.assertTrue(self.can_reach_entrance(SPAWNING_MEADOWS + " -> " + YAMAGAWA_MA))