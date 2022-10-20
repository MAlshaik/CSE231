from operator import itemgetter


master_list = [
            ["Albedo", "Geo", "Sword", 5, "Mondstadt"],
            ["Aloy", "Cryo", "Bow", 5, None],
            ["Traveler", "None", "Sword", 5, None],
            ["Xingqiu", "Hydro", "Sword", 4, "Liyue"],
            ["Yae Miko", "Electro", "Catalyst", 5, "Inazuma"]
        ]

print(sorted(sorted(master_list), key=itemgetter(3), reverse=True))

