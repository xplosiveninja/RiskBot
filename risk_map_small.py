import risk_map_base

continents_dict = {
    "continent_1" : [["region_1_1", "region_1_2", "region_1_3", "region_1_4", "region_1_5"], 5],
    "continent_2" : [["region_2_1", "region_2_2", "region_2_3", "region_2_4"], 4]
}
    
connections_dict = {
    "region_1_1" : ["region_1_2", "region_1_4"],
    "region_1_2" : ["region_1_1", "region_1_3", "region_1_5"],
    "region_1_3" : ["region_1_2", "region_2_1"],
    "region_1_4" : ["region_1_1", "region_1_5", "region_2_2"],
    "region_1_5" : ["region_1_4", "region_1_2", "region_2_1", "region_2_3"],
    "region_2_1" : ["region_1_5", "region_1_3", "region_2_4"],
    "region_2_2" : ["region_1_4", "region_2_3"],
    "region_2_3" : ["region_2_2", "region_1_5", "region_2_4"],
    "region_2_4" : ["region_2_3", "region_2_1"]
}

class small_map(risk_map_base.Map):
    def __init__(self, controller):
        risk_map_base.Map.__init__(self, connections_dict, continents_dict, controller)