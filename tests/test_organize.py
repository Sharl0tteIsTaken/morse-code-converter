import unittest, json

from unittest.mock import patch

from converter.organizer import Organizer
from tests.answers import convert_ans_codes, convert_ans_output_default, convert_ans_output_mess


cfg_default = {
    'dot': '.',
    'dash': '-',
    'code_space': ' ',
    'letter_space': '   ',
    'word_space': '       ',
}

path = 'C:/Users/88693/Documents/.MyDoc/Projects/#100Days/day-82-morse_code_converter/converter/config.json'

class TestOrganize(unittest.TestCase):
    def test_init(self):
        """
        didn't test FileNotFoundError is due to can't just mock the first `with open():`.
        it's doable to let every functionallity of code be in different function,
        but that will take extra time, this project is already a sinkhole, will pass on that.
        """
        o = Organizer()
        self.assertEqual(o.config_name, 'default')
        self.assertEqual(o.configs, cfg_default)
    
    @patch('builtins.input')
    def test_command_config_noname(self, mock_input):
        mock_input.side_effect = ['z', 'x', 'c', 'v', 'b', 'cancel']
        o = Organizer()
        o.commands(user_input='!config')
        self.assertEqual(o.configs, {
            'dot': 'z', 
            'dash': 'x', 
            'code_space': 'c', 
            'letter_space': 'v', 
            'word_space': 'b', 
        })
        self.assertEqual(o.config_name, None)

    @patch('builtins.input')
    def test_command_config_withname_del(self, mock_input):
        mock_input.side_effect = ['a', 's', 'd', 'f', 'g', 'test_unittest_asdf', 'test_unittest_asdf']
        o = Organizer()
        o.commands(user_input='!config')
        self.assertEqual(o.configs, {
            'dot': 'a', 
            'dash': 's', 
            'code_space': 'd', 
            'letter_space': 'f', 
            'word_space': 'g', 
        })
        self.assertEqual(o.config_name, 'test_unittest_asdf')
        
        # this seems like will make every letter a output at a time??
        # mock_input.side_effect = 'test_unittest_asdf'
        
        o.commands(user_input='!delete')
        
    @patch('builtins.input')
    def test_command_config_noname_save_del(self, mock_input):
        mock_input.side_effect = ['p', 'o', 'i', 'u', 'y', 'cancel', 'puipui', 'puipui']
        o = Organizer()
        o.commands(user_input='!config')
        self.assertEqual(o.configs, {
            'dot': 'p', 
            'dash': 'o', 
            'code_space': 'i', 
            'letter_space': 'u', 
            'word_space': 'y', 
        })
        self.assertEqual(o.config_name, None)
        
        o.command_save()
        self.assertEqual(o.config_name, 'puipui')
        
        # unittest must be repeatable
        # cite: https://stackoverflow.com/questions/30148221/python-run-unittests-continuously-or-each-test-multiple-times
        o.commands(user_input='!delete')
    
    
    @patch('builtins.input')
    def test_command_load_firsttry(self, mock_input):
        # .side_effect must be list[str]
        mock_input.side_effect = ['os and ones']
        o = Organizer()
        o.commands(user_input='!load')
        self.assertEqual(o.configs, {
            'dot': '0', 
            'dash': '1', 
            'code_space': '+', 
            'letter_space': '-', 
            'word_space': '*', 
        })
        self.assertEqual(o.config_name, 'os and ones')

    @patch('builtins.input')
    def test_command_load_secndtry(self, mock_input):
        mock_input.side_effect = ['something beyond my vision', 'os and ones', 'endl']
        o = Organizer()
        o.commands(user_input='!load')
        self.assertEqual(o.configs, {
            'dot': '0', 
            'dash': '1', 
            'code_space': '+', 
            'letter_space': '-', 
            'word_space': '*', 
        })
        self.assertEqual(o.config_name, 'os and ones')

    @patch('builtins.input')
    def test_command_rename_firsttry(self, mock_input):
        mock_input.side_effect = ['os and ones', '0&1', '0&1', '0&1', 'os and ones', 'os and ones', 'endl']
        o = Organizer()
        o.commands(user_input='!rename')
        o.command_load()
        
        self.assertEqual(o.configs, {
            'dot': '0', 
            'dash': '1', 
            'code_space': '+', 
            'letter_space': '-', 
            'word_space': '*', 
        })
        self.assertEqual(o.config_name, '0&1')
        
        o.commands(user_input='!rename')
        o.command_load()
        self.assertEqual(o.configs, {
            'dot': '0', 
            'dash': '1', 
            'code_space': '+', 
            'letter_space': '-', 
            'word_space': '*', 
        })
        self.assertEqual(o.config_name, 'os and ones')
        
    @patch('builtins.input')
    def test_command_rename_secndtry(self, mock_input):
        mock_input.side_effect = ['gibby', 'os and ones', '0&1', '0&1', '0&1', 'os and ones', 'os and ones', 'endl']
        o = Organizer()
        o.commands(user_input='!rename')
        o.command_load()
        
        self.assertEqual(o.configs, {
            'dot': '0', 
            'dash': '1', 
            'code_space': '+', 
            'letter_space': '-', 
            'word_space': '*', 
        })
        self.assertEqual(o.config_name, '0&1')
        
        o.commands(user_input='!rename')
        o.command_load()
        self.assertEqual(o.configs, {
            'dot': '0', 
            'dash': '1', 
            'code_space': '+', 
            'letter_space': '-', 
            'word_space': '*', 
        })
        self.assertEqual(o.config_name, 'os and ones')
        