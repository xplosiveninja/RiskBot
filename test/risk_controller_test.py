import unittest
import sys
import inspect
import random

import risk_controller

class game_states:
    def assigned_troops_1():
        board = risk_controller.board(["player_1", "player_2"])

        board.get_actions()

        for key, value in board.game_board.territory_dict.items():
            board.get_actions()
            board.perform_action(0, value)
        
        board.get_actions()
        board.perform_action(1, board.get_region("Ural"), 14)
        
        board.get_actions()
        board.perform_action(1, board.get_region("Afghanistan"), 14)

        return board
    
    def base_setup():
        board = risk_controller.board(["player_1", "player_2"])

        return board


class risk_controller_unit_test(unittest.TestCase):
    max_iter = 5

    def test_player_instantiation(self):
        board = risk_controller.board(["player_1", "player_2"])
        
        self.assertEqual(board.players[0].name, "player_1")
        self.assertEqual(board.players[1].name, "player_2")
        self.assertEqual(board.players[0].free_troops, 35)
        self.assertEqual(board.current_player.name, "player_1")
        self.assertEqual(board.game_phase, board.game_phases.starting)
        self.assertEqual(board.turn_phase, board.turn_phases.assign)
        
    def test_get_actions(self):
        board = risk_controller.board(["player_1", "player_2"])
        board.get_actions()
        self.assertEqual(board.possible_actions, [board.current_player.claim_territory, board.current_player.assign_recruits])
        
        for key, value in board.game_board.territory_dict.items():
            board.get_actions()
            board.perform_action(0, value)
        
        board.get_actions()
        board.perform_action(1, board.get_region("Ural"), 14)
        
        board.get_actions()
        board.perform_action(1, board.get_region("Afghanistan"), 14)
        
        board.get_actions()
        self.assertEqual(board.possible_actions, [board.current_player.attack_territory, board.current_player.move_troops])

        board.perform_action(0, 3, board.get_region("Ural"), 2, board.get_region("Afghanistan"))
        self.assertEqual(board.possible_actions, [board.current_player.attack_territory, board.current_player.move_troops])

        board.perform_action(1, board.get_region("Ural"), board.get_region("Great Britain"), 2)
        board.get_actions()
        self.assertEqual(board.possible_actions, [board.current_player.assign_recruits])

    def test_attack(self):
        board = game_states.assigned_troops_1()

        board.get_actions()
        before = board.get_region("Ural").troops + board.get_region("Afghanistan").troops
        board.perform_action(0, 3, board.get_region("Ural"), 2, board.get_region("Afghanistan"))
        self.assertTrue(board.get_region("Ural").troops + board.get_region("Afghanistan").troops < before)

        self.assertRaises(Exception, board.perform_action, 0, 5, board.get_region("Ural"), 2, board.get_region("Afghanistan"))

        self.assertRaises(Exception, board.perform_action, 0, 1, board.get_region("China"), 2, board.get_region("Afghanistan"))

        self.assertRaises(Exception, board.perform_action, 0, 1, board.get_region("Ural"), 1, board.get_region("Siberia"))

        self.assertRaises(Exception, board.perform_action, 0, 1, board.get_region("Ural"), 2, board.get_region("Ukraine"))

    def test_take_over(self):
        board = game_states.assigned_troops_1()

        prev_owner = board.get_region("Ukraine").owner.name

        board.get_actions()
        for i in range(self.max_iter):
            try:
                board.perform_action(0, 3, board.get_region("Ural"), 1, board.get_region("Ukraine"))
            except:
                pass

        self.assertTrue(board.get_region("Ukraine").owner.name != prev_owner)

    def test_get_region(self):
        board = game_states.base_setup()

        territory = board.get_region("Ukraine")

        self.assertTrue(territory.name == "Ukraine")

        
unittest.main()