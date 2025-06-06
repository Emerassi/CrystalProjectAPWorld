def load_tests(loader, standard_tests, pattern):
    import os
    import unittest
    from .. import file_path
    from worlds.AutoWorld import AutoWorldRegister

    suite = unittest.TestSuite()
    suite.addTests(standard_tests)
    folders = [os.path.join(os.path.split(world.__file__)[0], "test")
               for world in AutoWorldRegister.world_types.values()
               # TODO remove our hack before we push our fork to main
               if world.game == "Crystal Project"] # skip ALttP/Timespinner/etc world tests

    all_tests = [
        test_case for folder in folders if os.path.exists(folder)
        for test_collection in loader.discover(folder, top_level_dir=file_path)
        for test_suite in test_collection if isinstance(test_suite, unittest.suite.TestSuite)
        for test_case in test_suite
    ]

    suite.addTests(sorted(all_tests, key=lambda test: test.__module__))
    return suite
