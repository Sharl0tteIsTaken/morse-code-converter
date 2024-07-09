import unittest

from unittest.mock import patch

from subject.builtins_input import BuiltinsInput

class TestInput(unittest.TestCase):
    # cite(idea): https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
    # cite(method): day82/test_try_except_block
    @patch('builtins.input', return_value='sure')
    def test_enter(self, input):
        ui = BuiltinsInput()
        ui.enter()
        self.assertEqual(ui.log[ui.counts-1], 'sure')
        
    @patch('builtins.input')
    def test_chained_enter(self, mock_input):
        # cite(usage of .side_effect): https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
        mock_input.side_effect = ['mic test', 'test mic', 'uno dos tre']
        ui = BuiltinsInput()
        ui.chained_enter()
        self.assertEqual(ui.chained_log, ['mic test', 'test mic', 'uno dos tre'])
        
    @patch('builtins.input')
    def test_tree_enter_az(self, mock_input):
        mock_input.side_effect = ['a', 'z']
        ui = BuiltinsInput()
        ui.tree_enter()
        self.assertEqual(ui.tree, 'az')
        
    @patch('builtins.input')
    def test_tree_enter_bw(self, mock_input):
        mock_input.side_effect = ['b', 'w']
        ui = BuiltinsInput()
        ui.tree_enter()
        self.assertEqual(ui.tree, 'bw')
        
    @patch('builtins.input')
    def test_tree_enter__0(self, mock_input):
        mock_input.side_effect = ['whatever']
        ui = BuiltinsInput()
        ui.tree_enter()
        self.assertEqual(ui.tree, '_0')