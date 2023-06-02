import unittest
import sys

sys.path.insert(0, "..")
import risk_controller

class risk_controller_unit_test(unittest.TestCase):
    def test_player_instantiation(self):
        board = risk_controller.board(["player_1", "player_2"])
        
        self.assertEqual(board.players[0].name, "player_1", "player_1 name is incorrect")
        self.assertEqual(board.players[1].name, "player_2", "player_2 name is incorrect")
        self.assertEqual(board.players[0].free_troops, 35, ("player_1 instantiated with {number_of_troops} instead of 35".format(number_of_troops = board.players[0].free_troops)))
        
unittest.main()