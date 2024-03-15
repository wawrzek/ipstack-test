#!/usr/bin/env python3


import os
import sys
import unittest

sys.path.append(os.path.dirname(os.getcwd()))

RESPONSE_NOKEY = {
  "success": False,
  "error": {
    "code": 101,
    "type": "missing_access_key",
    "info": "You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]"
  }
}

RESPONSE_GOOD= {
        "ip": "134.201.250.155",
        "type": "ipv4",
        "continent_code": "NA",
        "continent_name": "North America",
        "country_code": "US",
        "country_name": "United States",
        "region_code": "CA",
        "region_name": "California",
        "city": "Los Angeles",
        "zip": "90012",
        "latitude": 34.0655517578125,
        "longitude": -118.24053955078125,
        "location": {
            "geoname_id": 5368361,
            "capital": "Washington D.C.",
            "languages": [{
                "code": "en",
                "name": "English",
                "native": "English",
                }],
            "country_flag": "https://assets.ipstack.com/flags/us.svg",
            "country_flag_emoji": "\ud83c\uddfa\ud83c\uddf8",
            "country_flag_emoji_unicode": "U+1F1FA U+1F1F8",
            "calling_code": "1",
            "is_eu": False
        }
}


from location import *
class TestClass(unittest.TestCase):
    def test_ip_1(self):
        self.assertTrue(checkIP("134.32.11.13"))
    def test_ip_2(self):
        self.assertFalse(checkIP("10.0.0.0"))
    def test_ip_3(self):
        self.assertFalse(checkIP("34.3234.23.4"))
    def test_ip_4(self):
        self.assertFalse(checkIP("ThisIsTest"))
    def test_request(self):
        self.assertEqual(getResponse("134.32.11.13", test=True),RESPONSE_NOKEY)
    def test_response(self):
        self.assertEqual(tuneOutput(RESPONSE_GOOD), [34.0655517578125, -118.24053955078125])

if __name__ == "__main__":
    unittest.main()
