import risk_player

class region:
    def __init__(self, name, controller):
        self.name = name
        self.troops = 0
        self.connecting_regions = []
        self.owner = ""
        self.map = controller
        self.polygon = ""
        
    def set_connections(self, connecting_regions):
        self.connecting_regions.append(connecting_regions)
    
    def get_connections(self):
        return self.connecting_regions
    
    def set_owner(self, owner):
        self.owner = owner
        
    def add_troops(self, delta_troops):
        self.troops += delta_troops
        
    def transfer_owner(self, winning_player, losing_player):
        losing_player.remove_territory(self)
        winning_player.add_territory(self)
        self.owner = winning_player
        self.map.cards.assign_card(winning_player, self.map.player_turns)