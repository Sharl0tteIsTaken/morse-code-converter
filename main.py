from converter.converter import Converter
from converter.organizer import Organizer

converter = Converter()
organizer = Organizer()


while organizer.operate:
    print('========================================================')
    user_input = input("enter text to convert into morse code or command below: (!commands for all commands)\n")
    print("\n")
    converter.update_configs(configs=organizer.commands(user_input=user_input))
    if organizer.user_command:
        continue
    output = converter.convert(user_input)
    print(f"converted morse code:\n{output}")
print('program ended.')
