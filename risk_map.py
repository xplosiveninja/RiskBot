import risk_continent
import risk_region

class Map:
    territory_dict = {}

    north_america_names = ["Alaska", "Northwest Territory", "Greenland", "Alberta", "Ontario", "Quebec", "Western United States", "Eastern United States", "Central America"]
    south_america_names = ["Venezuela", "Peru", "Brazil", "Argentina"]
    africa_names = ["North Africa", "Egypt", "East Africa", "Congo", "South Africa", "Madagascar"]
    europe_names = ["Iceland", "Scandinavia", "Ukraine", "Great Britian", "Northern Europe", "Southern Europe", "Western Europe"]
    oceana_names = ["Indonesia", "New Guinea", "Western Australia", "Eastern Australia"]
    asia_names = ["Siam", "India", "China", "Mongolia", "Japan", "Irkutsk", "Yakutsk", "Kamchatka", "Siberia", "Afghanistan", "Ural", "Middle East"]
    
    connections_dict = {"Alaska" : ["Northwest Territory", "Alberta", "Kamchatka"],
"Northwest Territory" : ["Alaska", "Alberta", "Ontario", "Greenland"],
"Greenland" : ["Northwest Territory", "Ontario", "Quebec", "Iceland"],
"Alberta" : ["Alaska", "Northwest Territory", "Ontario", "Western United States"],
"Ontario" : ["Northwest Territory", "Alberta", "Western United States", "Eastern United States", "Quebec", "Greenland"],
"Quebec" : ["Ontario", "Eastern United States", "Greenland"],
"Western United States" : ["Alberta", "Ontario", "Eastern United States", "Central America"],
"Eastern United States" : ["Ontario", "Quebec", "Western United States", "Central America"],
"Central America" : ["Western United States", "Eastern United States", "Venezuela"],
"Venezuela" : ["Central America", "Brazil", "Peru"],
"Peru" : ["Venezuela", "Brazil", "Argentina"],
"Brazil" : ["Venezuela", "Peru", "Argentina"],
"Argentina" : ["Brazil", "Peru"],
"North Africa" : ["Western Europe", "Southern Europe", "Egypt", "Brazil"],
"Egypt" : ["Southern Europe", "Middle East", "North Africa", "East Africa"],
"East Africa" : ["Egypt", "North Africa", "Congo", "South Africa", "Madagascar"],
"Congo" : ["North Africa", "East Africa", "South Africa"],
"South Africa" : ["Congo", "East Africa", "Madagascar"],
"Madagascar" : ["East Africa", "South Africa"],
"Iceland" : ["Greenland", "Scandinavia", "Great Britian"],
"Scandinavia" : ["Iceland", "Ukraine", "Northern Europe"],
"Ukraine" : ["Scandinavia", "Ural", "Northern Europe", "Afghanistan", "Southern Europe", "Middle East"],
"Great Britian" : ["Iceland", "Scandinavia", "Northern Europe", "Western Europe"],
"Northern Europe" : ["Scandinavia", "Great Britian", "Ukraine", "Western Europe", "Southern Europe"],
"Southern Europe" : ["Ukraine", "Northern Europe", "Western Europe", "Middle East", "Egypt", "North Africa"],
"Western Europe" : ["Great Britian", "Northern Europe", "North Africa"],
"Indonesia" : ["Siam", "New Guinea", "Western Australia"],
"New Guinea" : ["Indonesia", "Eastern Australia"],
"Western Australia" : ["Indonesia", "Eastern Australia"],
"Eastern Australia" : ["New Guinea", "Western Australia"],
"Siam" : ["China", "India", "Indonesia"],
"India" : ["Afghanistan", "China", "Middle East", "Siam"],
"China" : ["Siberia", "Ural", "Mongolia", "Afghanistan", "India", "Siam"],
"Mongolia" : ["Kamchatka", "Siberia", "Irkutsk", "Japan", "China"],
"Japan" : ["Kamchatka", "Mongolia"],
"Irkutsk" : ["Yakutsk", "Kamchatka", "Siberia", "Mongolia"],
"Yakutsk" : ["Kamchatka", "Siberia", "Irkutsk"],
"Kamchatka" : ["Alaska", "Yakutsk", "Irkutsk", "Japan", "Mongolia"],
"Siberia" : ["Yakutsk", "Ural", "Irkutsk", "China"],
"Afghanistan" : ["Ural", "Ukraine", "China", "Middle East", "India"],
"Ural" : ["Siberia", "Ukraine", "China", "Afghanistan"],
"Middle East" : ["Ukraine", "Afghanistan", "Southern Europe", "India", "Egypt", "East Africa"]}
    
    def __init__(self, controller):
        self.north_america_territories = []
        self.south_america_territories = []
        self.africa_territories = []
        self.europe_territories = []
        self.oceana_territories = []
        self.asia_territories = []
        
        for territory in self.connections_dict:
            self.territory_dict[territory] = risk_region.region(territory, controller)
            
        for territory in self.connections_dict:
            for connections in self.connections_dict[territory]:
                self.territory_dict[territory].set_connections(self.territory_dict[connections])
                
        for i in self.north_america_names:
            self.north_america_territories.append(self.territory_dict[i])
            
        for i in self.south_america_names:
            self.south_america_territories.append(self.territory_dict[i])
        
        for i in self.africa_names:
            self.africa_territories.append(self.territory_dict[i])
            
        for i in self.europe_names:
            self.europe_territories.append(self.territory_dict[i])
            
        for i in self.oceana_names:
            self.oceana_territories.append(self.territory_dict[i])
            
        for i in self.asia_names:
            self.asia_territories.append(self.territory_dict[i])
            
        self.north_america = risk_continent.continent("North America", self.north_america_territories, 5)
        self.south_america = risk_continent.continent("South America", self.south_america_territories, 2)
        self.africa = risk_continent.continent("Africa", self.africa_territories, 3)
        self.europe = risk_continent.continent("Europe", self.europe_territories, 5)
        self.oceana = risk_continent.continent("Oceana", self.oceana_territories, 2)
        self.asia = risk_continent.continent("Asia", self.asia_territories, 7)
        
    def continent_bonus(self, player):
        bonus = 24
        
        for i in self.north_america.territories:
            if not i.owner == player:
                bonus -= 5
                break
            
        for i in self.south_america.territories:
            if not i.owner == player:
                bonus -= 2
                break
            
        for i in self.africa.territories:
            if not i.owner == player:
                bonus -= 3
                break
            
        for i in self.europe.territories:
            if not i.owner == player:
                bonus -= 5
                break
            
        for i in self.oceana.territories:
            if not i.owner == player:
                bonus -= 2
                break
            
        for i in self.asia.territories:
            if not i.owner == player:
                bonus -= 7
                break
            
        return bonus
        
        