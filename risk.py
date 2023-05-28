import risk_continent
import risk_region
import risk_player

territory_list = [risk_region.region("England"), risk_region.region("Scotland"), risk_region.region("Wales"), risk_region.region("Ireland")]

start_continent = risk_continent.continent("UK", territory_list, 2)

player_1 = risk_player.player("charlie", "red")
player_2 = risk_player.player("Oana", "purple")

player_1.add_territory(territory_list[0])
player_1.add_territory(territory_list[1])

player_2.add_territory(territory_list[2])
player_2.add_territory(territory_list[3])

for i in range(0, 4):
    territory_list[i].add_troops(5)
    for j in range(0, 4):
        if not i == j:
            territory_list[i].set_connections(territory_list[j])
            
print(player_1.territory)
    
player_1.attack_territory(3, territory_list[0], 2, territory_list[2])

print(territory_list[0].troops)
print(territory_list[2].troops)

player_1.attack_territory(5, territory_list[0], 2, territory_list[2])

print(territory_list[0].troops)
print(territory_list[2].troops)

player_1.attack_territory(5, territory_list[0], 2, territory_list[2])

print(territory_list[0].troops)
print(territory_list[2].troops)

player_1.attack_territory(5, territory_list[0], 2, territory_list[2])

print(territory_list[0].troops)
print(territory_list[2].troops)

player_1.attack_territory(5, territory_list[0], 2, territory_list[2])

print(territory_list[0].troops)
print(territory_list[2].troops)

player_1.attack_territory(5, territory_list[0], 2, territory_list[2])

print(territory_list[0].troops)
print(territory_list[2].troops)

player_1.attack_territory(5, territory_list[0], 2, territory_list[2])

print(territory_list[0].troops)
print(territory_list[2].troops)

player_1.attack_territory(5, territory_list[0], 2, territory_list[2])

print(territory_list[0].troops)
print(territory_list[2].troops)

player_1.attack_territory(5, territory_list[0], 2, territory_list[2])

print(territory_list[0].troops)
print(territory_list[2].troops)

print(player_1.territory)