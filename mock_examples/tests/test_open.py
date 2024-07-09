import unittest
from unittest.mock import patch

from subject.builtins_open import BuiltinsOpen

path:str = 'C:/Users/88693/Documents/.MyDoc/Projects/#100Days/day-82-morse_code_converter/mock_examples/subject/target.json'



class TestOpen(unittest.TestCase):
    """
    this test will block every attempt of  `with open():` 
    """
    # cite: https://stackoverflow.com/questions/38918748/why-does-mocking-open-and-returning-a-filenotfounderror-raise-attributeerror
    def setUp(self):
        p = patch('builtins.open')
        self.mock_open = p.start()
        self.addCleanup(p.stop)

    def test_filenotfounderror(self):
        """every attempt of  `with open():` will raise error: FileNotFoundError
        """
        self.mock_open.side_effect = FileNotFoundError
        o = BuiltinsOpen()
        self.assertEqual(o.get_data(path), 'not found')


# 以上方法確定可行, 以下方法可能可行, 但由於歷史遺留問題與時間考量未進行測試!
# other solutions(not working): https://stackoverflow.com/questions/1289894/how-do-i-mock-an-open-used-in-a-with-statement-using-the-mock-framework-in-python
# other solutions(not working): https://stackoverflow.com/questions/33184342/how-do-i-mock-an-open-write-without-getting-a-no-such-file-or-directory