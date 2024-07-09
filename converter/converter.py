# test case to match: https://morsecode.world/international/translator.html
# CODE_SPACE = ''
# LETTER_SPACE = ' '
# WORD_SPACE = ' / '

from converter.convert_tables import ConvertTables

class Converter:
    """
    where the convertion is done.
    """
    def __init__(self) -> None:
        """
        Parameters
        ----------
            dot (str): short mark, dot or di: one time unit long. Defaults to ConvertTables.dot.
            dash (str): long mark, dash or dah: three time units long. Defaults to ConvertTables.dash.
            code_space (str): inter-element gap between the dits and dahs within a character: one unit long. Defaults to ConvertTables.CODE_SPACE.
            letter_space (str): short gap (between letters): three time units long. Defaults to ConvertTables.LETTER_SPACE.
            word_space (str): medium gap (between words): seven time units long. Defaults to ConvertTables.WORD_SPACE.
        """
        self.dot = ConvertTables.dot
        self.dash = ConvertTables.dash
        self.code_space = ConvertTables.code_space
        self.letter_space = ConvertTables.letter_space
        self.word_space = ConvertTables.word_space
        
        self.codes = self.morsecode_regulator()
        
    def morsecode_regulator(self) -> dict[str, str]:
        '''
        check if any value in convert table(3 dictionaries: letters, numbers, punctuations) is not
        acceptable codes(2 strings: dot, dash),
        - if any: raise error with message contain code in convert table that will causes error
        - if not: merge letter, numbers and punctuations from convert table into a single dictionary
        
        Returns:
            dict[str, str]: concatenated convert tables, code are all suitable for the following steps.
        '''
        def unpack_dict(**kwargs:dict) -> str:
            """
            take error message from Converter.code_regulator() when ConvertTables contain unsupported code,
            returns formatted string contain the letter, position, morse code of error.

            Returns:
                str: formatted string contain the letter, position, morse code of error
            """
            # cite: https://gaurav-patil21.medium.com/use-of-double-asterisk-in-python-962e83b63768
            unpacked = ''
            for letter in kwargs:
                for position in kwargs[letter].keys():
                    unpacked = unpacked + f"at letter: '{letter}', position(left to right): {position}, unacceptable: '{kwargs[letter][position]}'" + '\n'
            return unpacked
        
        codes = ConvertTables.letters | ConvertTables.numbers | ConvertTables.punctuations
        unacceptable = {}
        # cite: https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python/26853961#26853961
        for key in codes:
            error_place = {}
            for idx, letter in enumerate(codes[key]):
                if letter != self.dot and letter != self.dash:
                    error_place[idx+1] = letter
            if error_place != {}:
                unacceptable[key] = error_place
        if unacceptable != {}:
            raise ValueError(f"the morse code convert tables contain values unacceptable for convertion, acceptable: dot='{self.dot}', dash='{self.dash}'\
                \nall unacceptable:\n{unpack_dict(**unacceptable)}")
        return codes
    
    def update_configs(self, *, configs:dict[str, str] | None) -> None:
        """
        configures the output morse code with nearly every aspect of the code.
        
        configs should only take argument pass in by Organizer.commands()
        
        Parameters
        ----------
        
        configs(dict[str, str]):
            dot (str): short mark, dot or di: one time unit long. Defaults to ConvertTables.dot.
            dash (str): long mark, dash or dah: three time units long. Defaults to ConvertTables.dash.
            code_space (str): inter-element gap between the dits and dahs within a character: one unit long. Defaults to ConvertTables.CODE_SPACE.
            letter_space (str): short gap (between letters): three time units long. Defaults to ConvertTables.LETTER_SPACE.
            word_space (str): medium gap (between words): seven time units long. Defaults to ConvertTables.WORD_SPACE.
        """
        if configs is None:
            return
        
        for key, val in self.codes.items():
            self.codes[key] = val.replace(self.dot, configs['dot']).replace(self.dash, configs['dash'])
        
        self.dot = configs['dot']
        self.dash = configs['dash']
        self.code_space = configs['code_space']
        self.letter_space = configs['letter_space']
        self.word_space = configs['word_space']

    def convert(self, user_input:str) -> str:
        """
        takes user input and convert it into morse code.
        
        Args:
            user_input (str): a text wanted to convert

        Returns:
            str: converted string
        """
        output = ''
        for letter in user_input:
            if letter == ' ':
                output = output.rstrip(self.letter_space) + self.word_space
                continue
            code = list(self.codes[letter.upper()])
            output = output + self.code_space.join(code) + self.letter_space
        return output.rstrip(self.letter_space)
        