import risk_map_base

continents_dict = {
    "north_america_names" : [["Alaska", "Northwest Territory", "Greenland", "Alberta", "Ontario", "Quebec", "Western United States", "Eastern United States", "Central America"], 5],
    "south_america_names" : [["Venezuela", "Peru", "Brazil", "Argentina"], 2],
    "africa_names" : [["North Africa", "Egypt", "East Africa", "Congo", "South Africa", "Madagascar"], 3],
    "europe_names" : [["Iceland", "Scandinavia", "Ukraine", "Great Britain", "Northern Europe", "Southern Europe", "Western Europe"], 5],
    "oceana_names" : [["Indonesia", "New Guinea", "Western Australia", "Eastern Australia"], 2],
    "asia_names" : [["Siam", "India", "China", "Mongolia", "Japan", "Irkutsk", "Yakutsk", "Kamchatka", "Siberia", "Afghanistan", "Ural", "Middle East"], 7]
}
    
connections_dict = {
    "Alaska" : ["Northwest Territory", "Alberta", "Kamchatka"],
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
    "Iceland" : ["Greenland", "Scandinavia", "Great Britain"],
    "Scandinavia" : ["Iceland", "Ukraine", "Northern Europe"],
    "Ukraine" : ["Scandinavia", "Ural", "Northern Europe", "Afghanistan", "Southern Europe", "Middle East"],
    "Great Britain" : ["Iceland", "Scandinavia", "Northern Europe", "Western Europe"],
    "Northern Europe" : ["Scandinavia", "Great Britain", "Ukraine", "Western Europe", "Southern Europe"],
    "Southern Europe" : ["Ukraine", "Northern Europe", "Western Europe", "Middle East", "Egypt", "North Africa"],
    "Western Europe" : ["Great Britain", "Northern Europe", "North Africa"],
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
    "Middle East" : ["Ukraine", "Afghanistan", "Southern Europe", "India", "Egypt", "East Africa"]
}

class default_map(risk_map_base.Map):
    def __init__(self, controller):
        risk_map_base.Map.__init__(self, connections_dict, continents_dict, controller)