import unittest
from tictactoe import *


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # self.ll = LinkedList()
        # self.ll.add_node(1)
        # self.ll.add_node(2)
        # self.ll.add_node(3)
        # self.ll.add_node(4)
        # self.ll_as_list = [1, 2, 3, 4]
        pass

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




if __name__ == '__main__':
    unittest.main()