from enum import Enum
from random import choice

class Armies(Enum):
    infantry = 0
    cavalry = 1
    artillery = 2

class cards:
    last_turn = 0
    
    def __init__(self, territories):
        self.cards = self.generate_card(territories)

    def generate_card(self, territories):
        result = []
        curr = Armies.infantry
        i = 0
        
        for key, value in territories.items():
            result.append((value, curr))
            i += 1
            curr = Armies(i % 3)
            
        result.append(("", ""))
        result.append(("", ""))
            
        return result
    
    def assign_card(self, player, turn):
        if turn == self.last_turn:
            return
        else:
            card = choice(self.cards)
            player.cards.append(card)
            self.cards.remove(card)
    