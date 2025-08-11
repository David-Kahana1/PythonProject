import unittest


class testCitySize(unittest.TestCase):

    def setUp(self):
        print("into set up ")

    def test_city(self):
        city= "Jerusalem"
        city_len= len(city)
        assert city_len < 15, "the name is biggest"


    def test_city_num2(self):
        city= "Petah tikwa"
        city_len = len(city)
        assert city_len <12 ,f"we have a problem with {city}"

    def test_city_num3(self):
        city= "nes ziona"
        city_len= len(city)
        assert city_len>5 , "it's not valid"