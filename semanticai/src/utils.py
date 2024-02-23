def strip_unittest_path(unittest_path):
    split_path = unittest_path.split("/")
    test_name = split_path[-1].split("_test.py")[0]
    unittest_path = "/".join(split_path[:-1]) + "/"
    return test_name, unittest_path