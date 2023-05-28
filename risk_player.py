import random
import risk_region
import risk_map
import risk_controller
from math import floor
from enum import Enum

class player: 
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.territory = []
        self.cards = []
        self.free_troops = 35
        
    def __str__(self):
        ret_string = self.name + "\n" + str(self.free_troops) + "\n"
        
        for i in self.territory:
            ret_string += str(i.name) + "\n"
            
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
            return True
        else:
            print("Territory is taken")
            return False
    
    def remove_territory(self, lost_territory):
        self.territory.remove(lost_territory)
        
    def attack_territory(self, attacking_number, attacking_territory, defending_number, defending_territory):
        attack_rolls = []
        defend_rolls = []
        
        attackers_lost = 0
        defenders_lost = 0
        
        if not defending_territory in attacking_territory.get_connections():
           print("You can only attack neighbouring regions")
           return
       
        if defending_territory.owner == self:
            print("You can't attack yourself")
            return
        
        if attacking_territory.troops - attacking_number < 1:
            print("You must leave a troop on the attacking territory")
            return
        
        if attacking_number > 3:
            print("You can only attack with 3 troops at a time")
            return
            
        if defending_number > 2:
            print("You can only defend with 2 troops at a time")
        
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
            return True
        else:
            print("Cannot assign troops to that location, either you don't own it or have enough free troops")
            return False
        
    def move_troops(self, begin_territory, end_territory, number):
        if begin_territory.troops - number <= 1:
            print("You need to leave atleast 1 troop on each territory")
            return False
        
        if begin_territory.owner != self and end_territory.owner != self:
            print("You need to own both the start and end territories")
            return False
        
        begin_territory.troops -= number
        end_territory.troops += number
        
        return True