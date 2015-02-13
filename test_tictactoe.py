import unittest
from tictactoe import *


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.board1 = ['X','X','X',3,4,5,6,7,8]
        self.board2 = [0,'O',2,3,'O',5,6,'O',8]
        self.board3 = [0,'X',2,'O','O',5,'X','O',8]

    def test_choose_player(self):
        players = choose_player()
        self.assertTrue('X' in players)
        self.assertTrue('O' in players)
        if players['X'] == 'user':
            self.assertEqual(players['O'], 'computer')
        elif players['O'] == 'computer':
            self.assertEqual(players['X'], 'user')

        count = 0.0
        for i in range(10000):
            players = choose_player()
            if players['X'] == 'computer':
                count += 1
        self.assertTrue((count / 10000) < 0.51 and (count / 10000) > 0.49)

    def test_check_winner(self):
        self.assertEqual(check_winner(self.board1), 'X')
        self.assertEqual(check_winner(self.board2), 'O')
        self.assertFalse(check_winner(self.board3))

    def test_is_available(self):
        self.assertTrue(is_available(self.board1, 4))
        self.assertFalse(is_available(self.board1, 1))


if __name__ == '__main__':
    unittest.main()