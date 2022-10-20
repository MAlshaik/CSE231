import unittest
from Proj06.proj06 import sort_characters


class SortCharactersTest(unittest.TestCase):
    def test_sort_characters_with_one_rarity(self):
        master_list = [
            ["Albedo", "Geo", "Sword", 5, "Mondstadt"],
            ["Aloy", "Cryo", "Bow", 5, None],
            ["Traveler", "None", "Sword", 5, None]
        ]
        expected = [
            ["Albedo", "Geo", "Sword", 5, "Mondstadt"],
            ["Aloy", "Cryo", "Bow", 5, None],
            ["Traveler", "None", "Sword", 5, None]
        ]
        actual = sorted(master_list)
        print("master_list: ", master_list)
        print("Expected: ", expected)
        print("Actual: ", actual)
        print()
        assert actual == expected

    def test_sort_characters(self):
        master_list = [
            ["Albedo", "Geo", "Sword", 5, "Mondstadt"],
            ["Aloy", "Cryo", "Bow", 5, None],
            ["Traveler", "None", "Sword", 5, None],
            ["Xingqiu", "Hydro", "Sword", 4, "Liyue"],
            ["Yae Miko", "Electro", "Catalyst", 5, "Inazuma"]
        ]
        expected = [
            ["Albedo", "Geo", "Sword", 5, "Mondstadt"],
            ["Aloy", "Cryo", "Bow", 5, None],
            ["Traveler", "None", "Sword", 5, None],
            ["Yae Miko", "Electro", "Catalyst", 5, "Inazuma"],
            ["Xingqiu", "Hydro", "Sword", 4, "Liyue"]
        ]
        actual = sort_characters(master_list)
        print("master_list: ", master_list)
        print("Expected: ", expected)
        print("Actual: ", actual)
        print()
        assert actual == expected


if __name__ == '__main__':
    unittest.main()
