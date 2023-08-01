import risk_continent
import risk_region

class Map:
    territory_dict = {}
    continents = {}

    def __init__(self, connections_dict, continents_dict, controller):
        for territory in connections_dict:
            self.territory_dict[territory] = risk_region.region(territory, controller)
            
        for territory in connections_dict:
            for connections in connections_dict[territory]:
                self.territory_dict[territory].set_connections(self.territory_dict[connections])

        for continent in continents_dict:
            self.continents[continent] = risk_continent.continent(continent, [], continents_dict[continent][1])

            for i in continents_dict[continent][0]:
                self.continents[continent].territories.append(self.territory_dict[i])

    def continent_bonus(self, player):
        bonus = 0

        for name, continent in self.continents.items():
            player_set = set(())
            for region in continent.territories:
                if len(player_set) == 0:
                    player_set.add(region.owner)
                elif region.owner not in player_set:
                    player_set.add(region.owner)
                    break
            
            if len(player_set) == 1 and player in player_set:
                bonus += continent.bonus

        return bonus
    
    def get_region(self, region_name):
        return self.territory_dict[region_name]