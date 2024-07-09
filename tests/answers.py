convert_ans_codes = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...','8': '---..', '9': '----.',
    '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.', '?': '..--..', '=': '-...-',
    "'": '.----.', '/': '-..-.', '!': '-.-.--', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '(': '-.--.', ')': '-.--.-', '$': '...-..-', '&': '.-...', '@': '.--.-.', '+': '.-.-.',
    '.': '.-.-.-',
}

convert_ans_output_default = '-   .   . . .   -       - -   .   . . .   . . .   . -   - - .   .       . - - - -   . . - - -   . . . - -   - . - . - -'
convert_ans_output_mess = 'wrqrqeqeqrwtwewrqrqeqeqrqeqeqrqewrweweqrqtqewewewewrqeqewewewrqeqeqewewrweqeweqewew'



organize_ans_commands_commands = "\
!commands    - to see all the commands.\n\
!explain     - explain what is: `dot`, `dash`, `inter gap`, `short gap`, `medium gap`\n\
!available   - show all available input for convertion\n\
!show        - show the current configuration\n\
!config      - to modify the `dot`, `dash`, `inter gap`, `short gap`, `medium gap`\n\
!save        - save the current configuration made by the !config command\n\
!loadsave   - show all previous saves\n\
!load        - load a previous save\n\
!rename      - rename a previous save\
!exit        - to quit the application\n\
"

organize_ans_commands_explain_text = "International Morse code is composed of five elements:\n\
dot:            short mark, dot or di: one time unit long.\n\
dash:           long mark, dash or dah: three time units long.\n\
inter gap:      inter-element gap between the dots and dashs within a character: one unit long.\n\
short gap:      short gap (between letters): three time units long.\n\
medium gap:     medium gap (between words): seven time units long.\n\
\n\
a `time unit` in this context is a letter.\n\
these five elements will be referred to as `configuration`\n\
when describing multiple set of elements will be referred to as `configurations`\n\
\n\
example:        convert text: 'test msg' into morse code will be:\n\
'-   .   . . .   -       - -   . . .   - - .'\n\
 ^   ^    ^          ^               ^\n\
 |   |    |          |               |\n\
 dashdot  inter gap  medium gap      short gap\n\
\n\
in other words:\n\
'-   .   . . .   -       - -   . . .   - - .'\n\
't...e...  s  ...t....... m ...  s  ...  g  '\n\
(here uses '.' to replace spaces for clarification)\n\
t converts into '-', this is `dash`\n\
e converts into '.', this is `dot`\n\
s converts into '. . .', with a space in between morse codes, the space is `inter gap`\n\
spaces(three) in between two letter(t and e in test) is `short gap`\n\
spaces(seven) in between two word(test and msg) is `medium gap`\n\
"

available_text = "currently support:\n\
letters: A-Z(no difference between upper and lower case)\n\
numbers: 0-9\n\
punctuations: \
"