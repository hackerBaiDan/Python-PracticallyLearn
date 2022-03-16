"""
    Test 2022.3.15 hackerBaidan
"""
print("========= Test 2022.3.15 hackerBaidan=========")
# 测试 name_function.py & names.py
import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
if __name__ =='__main__':
    unittest.main()
