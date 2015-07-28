__author__ = 'a-aron'
import unittest
import pymap

class PymapTestCase(unittest.TestCase):
    """Tests pymap.py"""

    def test_make_query_str(self):
        filters = {'SHIPNAME': ['=', 'TIE-FIGHTER', '', ''], 'unixtime': ['BETWEEN', '0', 'and', '1403709097'], 'lon': ['BETWEEN', '0', 'AND', '-150']}
        self.assertEquals("SELECT unixtime, lat, lon, crs, spd, MMSI, SHIPNAME FROM test_table WHERE 1 AND unixtime BETWEEN '0' and '1403709097' AND SHIPNAME = 'TIE-FIGHTER'  '' AND lon BETWEEN '-150' AND '0'", pymap.make_query_str("test_table", filters))