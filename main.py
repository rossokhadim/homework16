import spells.marauder_map as mm

p = 'D:/PyCharm/pythonProject19/data.json'
map = mm.MarauderMap(p)
map.map_generator()
print(map.path)
