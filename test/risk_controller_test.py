import unittest
import sys
import inspect

import risk_controller

class risk_controller_unit_test(unittest.TestCase):
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
        board.perform_action(1, board.game_board.territory_dict["Ural"], 14)
        
        board.get_actions()
        board.perform_action(1, board.game_board.territory_dict["Afghanistan"], 14)
        
        board.get_actions()
        self.assertEqual(board.possible_actions, [board.current_player.attack_territory, board.current_player.move_troops])

        board.perform_action(0, 3, board.game_board.territory_dict["Ural"], 2, board.game_board.territory_dict["Afghanistan"])
        self.assertEqual(board.possible_actions, [board.current_player.attack_territory, board.current_player.move_troops])

        board.perform_action(1, board.game_board.territory_dict["Ural"], board.game_board.territory_dict["Great Britain"], 2)
        board.get_actions()
        self.assertEqual(board.possible_actions, [board.current_player.assign_recruits])

    def test_attack(self):
        board = risk_controller.board(["player_1", "player_2"])
        board.get_actions()
        self.assertEqual(board.possible_actions, [board.current_player.claim_territory, board.current_player.assign_recruits])
        
        for key, value in board.game_board.territory_dict.items():
            board.get_actions()
            board.perform_action(0, value)
        
        board.get_actions()
        board.perform_action(1, board.game_board.territory_dict["Ural"], 14)
        
        board.get_actions()
        board.perform_action(1, board.game_board.territory_dict["Afghanistan"], 14)

        board.get_actions()
        before = board.game_board.territory_dict["Ural"].troops + board.game_board.territory_dict["Afghanistan"].troops
        board.perform_action(0, 3, board.game_board.territory_dict["Ural"], 2, board.game_board.territory_dict["Afghanistan"])
        self.assertTrue(board.game_board.territory_dict["Ural"].troops + board.game_board.territory_dict["Afghanistan"].troops < before)

        before = board.game_board.territory_dict["Ural"].troops + board.game_board.territory_dict["Afghanistan"].troops
        board.perform_action(0, 5, board.game_board.territory_dict["Ural"], 2, board.game_board.territory_dict["Afghanistan"])
        self.assertTrue(board.game_board.territory_dict["Ural"].troops + board.game_board.territory_dict["Afghanistan"].troops == before)

        before = board.game_board.territory_dict["China"].troops + board.game_board.territory_dict["Afghanistan"].troops
        board.perform_action(0, 1, board.game_board.territory_dict["China"], 2, board.game_board.territory_dict["Afghanistan"])
        self.assertTrue(board.game_board.territory_dict["China"].troops + board.game_board.territory_dict["Afghanistan"].troops == before)

        before = board.game_board.territory_dict["Ural"].troops + board.game_board.territory_dict["Siberia"].troops
        board.perform_action(0, 1, board.game_board.territory_dict["Ural"], 1, board.game_board.territory_dict["Siberia"])
        self.assertTrue(board.game_board.territory_dict["Ural"].troops + board.game_board.territory_dict["Siberia"].troops == before)

        before = board.game_board.territory_dict["Ural"].troops + board.game_board.territory_dict["Ukraine"].troops
        board.perform_action(0, 1, board.game_board.territory_dict["Ural"], 2, board.game_board.territory_dict["Ukraine"])
        self.assertTrue(board.game_board.territory_dict["Ural"].troops + board.game_board.territory_dict["Ukraine"].troops == before)

unittest.main()