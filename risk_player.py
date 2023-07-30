import random
import risk_region
import risk_map
import risk_controller
from math import floor
from enum import Enum

class player:
    def __init__(self, name, colour, game_board_ref):
        self.name = name
        self.colour = colour
        self.territory = []
        self.cards = []
        self.free_troops = 35
        self.player_states = Enum("player_states", ["turn_in_play", "turn_over", "player_lost"])
        self.player_state = self.player_states.turn_over
        self.game_board = game_board_ref
        
    def __str__(self):
        ret_string = self.name + "\nFree Troops : " + str(self.free_troops) + "\n\nPlayer Cards :\n"
        
        for i in self.cards:
            ret_string += str(i[0].name) + " : " + str(i[1]) + "\n"
            
        ret_string += "\nPossible Actions :\n"
        
        for i in self.available_actions(self.game_board):
            ret_string += i.__name__ + "\n"
            
        ret_string += "\nControlled Territories :\n"
        
        for i in self.territory:
            ret_string += str(i.name) + " : " + str(i.troops) + "\n"
            
        return ret_string
    
    def available_actions(self, game_board):
        result = []
        
        if game_board.game_phase == game_board.game_phases.starting:
            claim = self.claim_territory
            assign = self.assign_recruits
            result.append(claim)
            result.append(assign)
        else:
            if game_board.turn_phase == game_board.turn_phases.assign:
                assign = self.assign_recruits
                result.append(assign)
            elif game_board.turn_phase == game_board.turn_phases.attack:
                attack = self.attack_territory
                move_troops = self.move_troops
                result.append(attack)
                result.append(move_troops)
        return result
    
    def add_territory(self, new_territory):
        self.territory.append(new_territory)
        new_territory.set_owner(self)
    
    def claim_territory(self, new_territory):
        if new_territory.owner == "":
            self.territory.append(new_territory)
            new_territory.set_owner(self)
            new_territory.troops = 1
            self.free_troops -= 1
            self.player_state = self.player_states.turn_over
        else:
            raise Exception("Territory is taken")
    
    def remove_territory(self, lost_territory):
        self.territory.remove(lost_territory)
        
    def attack_territory(self, attacking_number, attacking_territory, defending_number, defending_territory):
        attack_rolls = []
        defend_rolls = []
        
        attackers_lost = 0
        defenders_lost = 0
        
        if not defending_territory in attacking_territory.get_connections():
           raise Exception("You can only attack neighbouring regions")
       
        if defending_territory.owner == self:
            raise Exception("You can't attack yourself")
        
        if attacking_territory.troops - attacking_number < 1:
            raise Exception("You must leave a troop on the attacking territory")
        
        if attacking_number > 3:
            raise Exception("You can only attack with 3 troops at a time")
            
        if defending_number > 2:
            raise Exception("You can only defend with 2 troops at a time")
        
        if defending_number > defending_territory.troops:
            raise Exception("You only have {def_troops} troops to defend with".format(def_troops = defending_territory.troops))
        
        for i in range(0, attacking_number):
            attack_rolls.append(random.randrange(1,7))
            
        for i in range(0, defending_number):
            defend_rolls.append(random.randrange(1,7))
            
        attack_rolls.sort(reverse=True)
        defend_rolls.sort(reverse=True)
        
        while attack_rolls and defend_rolls:
            if attack_rolls[0] > defend_rolls[0]:
                defenders_lost += 1
            else:
                attackers_lost += 1
                
            del attack_rolls[0]
            del defend_rolls[0]
        
        defending_territory.troops -= defenders_lost
        
        if defending_territory.troops <= 0:
            defending_territory.troops = attacking_number - attackers_lost
            attacking_territory.troops -= attacking_number
            defending_territory.transfer_owner(self, defending_territory.owner)
        else:
            attacking_territory.troops -= attackers_lost
            
    def add_recruits(self, curr_map):
        new_recruits = floor(len(self.territory) / 3) + curr_map.continent_bonus(self)
        self.free_troops += new_recruits
        
    def assign_recruits(self, territory, number):
        if (self.free_troops - number) >= 0 and territory.owner == self:
            territory.troops += number
            self.free_troops -= number
        else:
            raise Exception("Cannot assign troops to that location, either you don't own it or have enough free troops")
        
        if(self.game_board.game_phase == self.game_board.game_phases.starting):
            self.player_state = self.player_states.turn_over
        
    def move_troops(self, begin_territory, end_territory, number):
        if begin_territory.troops - number <= 1:
            raise Exception("You need to leave atleast 1 troop on each territory")
        
        if begin_territory.owner != self and end_territory.owner != self:
            raise Exception("You need to own both the start and end territories")
        
        begin_territory.troops -= number
        end_territory.troops += number
        self.player_state = self.player_states.turn_over