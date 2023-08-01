import unittest

import risk_map_small
import risk_controller

class risk_map_unit_test(unittest.TestCase):
    def test_regions(self):
        board = risk_controller.board(["player_1", "player_2"], map_type = risk_map_small.small_map)

        map = risk_map_small.small_map(board)

        self.assertEqual(len(board.game_board.territory_dict), 9)
        self.assertEqual(len(board.game_board.continents), 2)

    def test_bonus(self):
        board = risk_controller.board(["player_1", "player_2"], map_type = risk_map_small.small_map)

        board.game_board.get_region("region_1_1").owner = board.players[0]
        board.game_board.get_region("region_1_2").owner = board.players[0]
        board.game_board.get_region("region_1_3").owner = board.players[0]
        board.game_board.get_region("region_1_4").owner = board.players[0]
        board.game_board.get_region("region_1_5").owner = board.players[0]
        board.game_board.get_region("region_2_1").owner = board.players[1]
        board.game_board.get_region("region_2_2").owner = board.players[1]
        board.game_board.get_region("region_2_3").owner = board.players[1]
        board.game_board.get_region("region_2_4").owner = board.players[1]

        self.assertEqual(board.game_board.continent_bonus(board.players[0]), 5)
        self.assertEqual(board.game_board.continent_bonus(board.players[1]), 4)

unittest.main()