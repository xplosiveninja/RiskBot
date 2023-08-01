import risk_player
import risk_map_default
import risk_cards
import time
from enum import Enum
import random

class board:
    def __init__(self, player_names, **kwargs):
        self.players = []
        self.game_phases = Enum("game_phases", ["starting", "play"])
        self.turn_phases = Enum("turn_phases", ["assign", "attack"])
        self.game_phase = self.game_phases.starting
        self.turn_phase = self.turn_phases.assign
        self.possible_actions = []
        
        map_type = kwargs.get('map_type', risk_map_default.default_map)
        self.game_board = map_type(self)
        for i in player_names:
            self.players.append(risk_player.player(i, "", self))
        self.current_player = self.players[0]
        self.player_turns = 0
        self.cards = risk_cards.cards(self.game_board.territory_dict)
    
    def phase_controller(self):
        if (self.game_phase == self.game_phases.starting):
            self.setup_phase()
        else:
            self.turn_phase_control()

    def setup_phase(self):
        phase_finished = True
        
        for player in self.players:
            if player.free_troops != 0:
                phase_finished = False
                
        if phase_finished:
            self.game_phase = self.game_phases.play
            self.turn_phase_control()
            
    def turn_phase_control(self):
        if self.current_player.free_troops == 0:
            self.turn_phase = self.turn_phases.attack
            
    def change_player(self):
        self.player_turns += 1
        self.current_player = self.players[self.player_turns % len(self.players)]
        self.current_player.player_state = self.current_player.player_states.turn_in_play
        if self.game_phase == self.game_phases.play:
            self.current_player.add_recruits(self.game_board)
            self.turn_phase = self.turn_phases.assign
          
    def get_actions(self):
        self.possible_actions = self.current_player.available_actions(self)

    def get_region(self, region_name):
        return self.game_board.territory_dict[region_name]

    def perform_action(self, arg1, *argv):
        action_result = self.possible_actions[arg1](*argv)
        if self.current_player.player_state == self.current_player.player_states.turn_over:
            self.change_player()
        self.phase_controller()
            

