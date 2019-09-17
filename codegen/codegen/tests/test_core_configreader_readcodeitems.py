import unittest
from config.configreader import read

class Test_core_configreader(unittest.TestCase):
    def test_readconfig(self):
        expected = 2
        config_data = read()

        assert config_data is not None
        assert expected == len(config_data.code_items)

if __name__ == '__main__':
    unittest.main()
