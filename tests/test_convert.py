import unittest


from converter.convert_tables import ConvertTables
from converter.converter import Converter

from tests.answers import convert_ans_codes, convert_ans_output_default, convert_ans_output_mess


cfg_mess = {
    'dot': 'q',
    'dash': 'w',
    'code_space': 'e',
    'letter_space': 'r',
    'word_space': 't',
}


# cite: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNoLogs

class TestConvert(unittest.TestCase):
    def test_init(self):
        c = Converter()
        # cite: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
        self.assertEqual(c.dot, ConvertTables.dot)
        self.assertEqual(c.dash, ConvertTables.dash)
        self.assertEqual(c.code_space, ConvertTables.code_space)
        self.assertEqual(c.letter_space, ConvertTables.letter_space)
        self.assertEqual(c.word_space, ConvertTables.word_space)
        
        # skipped test of raised ValueError in morsecode_regulator()
        
        self.assertEqual(c.codes, convert_ans_codes)
        
    def test_update_configs_and_convert(self):
        c = Converter()
        
        output_1 = c.convert('test message 123!')
        self.assertEqual(output_1, convert_ans_output_default)
        
        c.update_configs(configs=cfg_mess)
        self.assertEqual(c.dot, cfg_mess['dot'])
        self.assertEqual(c.dash, cfg_mess['dash'])
        self.assertEqual(c.code_space, cfg_mess['code_space'])
        self.assertEqual(c.letter_space, cfg_mess['letter_space'])
        self.assertEqual(c.word_space, cfg_mess['word_space'])
        
        output_2 = c.convert('test message 123!')
        self.assertEqual(output_2, convert_ans_output_mess)
