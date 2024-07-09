import json

from converter.convert_tables import ConvertTables
from converter.help_texts import command_text, explain_text, available_text



# path = '#100Days/day-82-morse_code_converter/converter/config.json'
# TODO: change path potentionally with `os`
path = 'C:/Users/88693/Documents/.MyDoc/Projects/#100Days/day-82-morse_code_converter/converter/config.json'

class Organizer():
    """
    organize everything from configure convertion to process text and commands.
    """
    def __init__(self) -> None:
        """
        get history saved configs form config.json, if config.json doesn't exis, create one
        and set default values.
        """
        self.operate: bool = True
        try:
            with open(path, mode="r") as save_file:
                self.saved_configs:dict[str, dict[str, str]] | dict = json.load(save_file)
            self.configs:dict[str, str] = self.saved_configs['default']
            self.config_name:str | None = 'default'
        except FileNotFoundError:
            self.setup_json()
        except KeyError:
            self.setup_json()

    def setup_json(self):
        """
        get data from ConvertTables(), and setup attributes required by __init__,
        and recreate config.json with value from ConvertTables().
        """
        print("there is a problem with saved configurations, setting up default configuration...")
        self.saved_configs = {}
        with open(path, mode="w") as save_file:
            json.dump(obj=self.saved_configs, fp=save_file, indent=4)
        self.configs = {
            'dot': ConvertTables.dot,
            'dash': ConvertTables.dash,
            'code_space': ConvertTables.code_space,
            'letter_space': ConvertTables.letter_space,
            'word_space': ConvertTables.word_space,
        }
        self.config_name:str | None  = 'default'
        self._save_current_config(config_name=self.config_name)
        print("configuration setup successfully.")

    def commands(self, *, user_input:str) -> dict[str, str] | None:
        """
        base on user input:
            - command will be executed
            - text will be ignored
        
        Args:
            user_input (str): text or command

        Returns:
            dict[str, str] | None: if command changes config of convertion, returns the config, otherwise None
        """
        
        self.user_command: bool = True # skips convert input part of code.
        match user_input:
            case '!commands':
                print(command_text)
            case '!explain':
                print(explain_text)
            case '!available':
                puns:dict[str, str] = ConvertTables.punctuations
                print(available_text, end="")
                print(list(puns.keys()))
            case '!show':
                self.command_show()
            case '!config':
                self.command_config()
            case '!save':
                self.command_save()
            case '!loadsave':
                self.command_loadsave()
            case '!load':
                self.command_load()
            case '!rename':
                self.command_rename()
            case '!delete':
                self.command_delete()
            case '!exit':
                self.operate = False
            case _:
                self.user_command = False
                
    def command_show(self) -> None:
        """
        print out the current configs.
        """
        print(f"current configuration name: '{self.config_name:}'")
        for cfgs in self.configs:
            print(f"{cfgs}: '{self.configs[cfgs]}',")
    
    def command_config(self) -> dict[str, str]:
        """
        set config and name it(if desire), config and name will be saved after naming.
        note that config name must be unique.

        Returns:
            dict[str, str]: config to pass on to converter
        """
        self.configs:dict[str, str] = {
            'dot': input(f"letter for `dot`(currently: '{self.configs['dot']}'): "),
            'dash': input(f"letter for `dash`(currently: '{self.configs['dash']}'): "),
            'code_space': input(f"letter for `inter gap`(currently: '{self.configs['code_space']}'{self._get_aka(self.configs['code_space'])}): "),
            'letter_space': input(f"letter for `short gap`(currently: '{self.configs['letter_space']}'{self._get_aka(self.configs['letter_space'])}): "),
            'word_space': input(f"letter for `medium gap`(currently: '{self.configs['word_space']}'{self._get_aka(self.configs['word_space'])}): "),
        }
        if not self._exist_by_name():
            print('configuration changed successfully.')
            name = input(f"set a name for this configuration? (will save this configuration, or enter 'cancel' to use !save to name and save configuration later.) ")
            if name == "cancel" or name =="'cancel'":
                print('canceled.')
                config_name = None
                self.config_name:str | None = config_name
            else:
                config_name = self._unique_name_check(confirm_name=name)
                self.config_name:str | None = config_name
                self._save_current_config(config_name=config_name)
                self._update_saved_configs()
                print(f"you can access this configuration by name: '{config_name}'.")
        return self.configs
    
    def command_save(self) -> None:
        """
        name and save the current config, show config name if the current config already exist.
        note that config name must be unique.
        """
        if self._exist_by_name():
            return None
        name = input("enter name to save configurations(or enter 'cancel' to cancel.): ")
        if name == "cancel" or name =="'cancel'":
            print('canceled.')
            return None
        config_name = self._unique_name_check(confirm_name=name)
        self.config_name = config_name
        self._save_current_config(config_name=config_name)
        self._update_saved_configs()
        print(f"you can access this configuration by !loadsave with name: '{config_name}'")
            
    def command_loadsave(self) -> None:
        """
        print out every config name of history save.
        """
        for config_name in self.saved_configs.keys():
            print(f"{config_name}: " + "{")
            for cfgs in self.saved_configs[config_name]:
                print(f"    {cfgs}: '{self.saved_configs[config_name][cfgs]}',")
            print("}")
    
    def command_load(self) -> dict[str, str] | None:
        """
        set config to a history save by config name.
        
        Returns:
            dict[str, str]: the chosen config
            None: process canceled
        """
        load_name = input(f"enter configuration name: ")
        load_name = self._name_exist(load_name, default_check=False)
        if load_name is None:
            return
        load = self.saved_configs[load_name]
        self.configs = {
            'dot': load['dot'],
            'dash': load['dash'],
            'code_space': load['code_space'],
            'letter_space': load['letter_space'],
            'word_space': load['word_space'],
        }
        self.config_name = load_name
        print(f"configuration loaded: ", end="")
        self.command_show()
        return self.configs
        
    def command_rename(self) -> None:
        """
        rename a history config name

        Args:
            old_key (str): old config name
            new_key (str): new config name
        """
        old_key = input("enter the old configuration name: ")
        
        old_key = self._name_exist(old_key, default_check=True)
        if old_key is None:
            return
                
        name = input("enter the new configuration name: ")
        new_key = self._unique_name_check(confirm_name=name)
        
        current_config, self.configs = self.configs, self.saved_configs[old_key]
        del self.saved_configs[old_key]
        
        self._save_current_config(config_name=new_key)
        self.configs = current_config
        self._update_saved_configs()
        print(f"configuration renamed, from '{old_key}' to '{new_key}'")
        
    def command_delete(self) -> None:
        """
        delete a config by name, if current config(self.configs) is also deleted,
        current config will become default config.

        Returns:
            _type_: _description_
        """
        name = input("enter the configuration name: ")
        name = self._name_exist(name, default_check=True)
        if name is None:
            return
        if self.configs == self.saved_configs[name]:
            self.configs = self.saved_configs['default']
            self.config_name = 'default'
        del self.saved_configs[name]
        with open(path, mode="w") as save_file:
            json.dump(obj=self.saved_configs, fp=save_file, indent=4)
        print(f"configuration deleted: '{name}'")

        
    # other functions, get called during commands()
    def _get_aka(self, string:str) -> str:
        """
        if the string passed in consists of the same characters, return what character and how much.

        Args:
            string (str): any string

        Returns:
            str: what character and how much.
            
        Examples:
            get_aka('1111111') -> ", a.k.a: '1' * 7"
            get_aka('1112111') -> ""
        """
        for letter in string:
            if len(set(list(letter))) == 1:
                return f", a.k.a: '{letter[0]}' * {len(string)}"
        return ""
    
    def _unique_name_check(self, confirm_name:str) -> str:
        """
        make sure the name pass in is unique(compare to history saves).

        Args:
            confirm_name (str): name wanted to check

        Returns:
            str: name not in history saves
        """
        while self._config_name_exist(confirm_name=confirm_name):
            print(f"all previous saved names: {self._get_saved_names()}")
            confirm_name = input('configuration name occupied, enter something else: ')
        return confirm_name

    def _config_name_exist(self, confirm_name:str) -> bool:
        """
        check if config name exist in history saves.

        Args:
            confirm_name (str): config name wanted to load

        Returns:
            bool: True if config name exist
        """
        exist:list[str] = [key for key in self.saved_configs if key == confirm_name]
        if exist == []:
            return False
        return True
    
    def _exist_by_name(self, ) -> bool:
        """
        check if the current config already exist in history saves,

        Returns:
            bool: if current config already exist
        """
        exist:list[str] | list = [key for (key, val) in self.saved_configs.items() if val == self.configs]
        if exist:
            print(f"this configuration already exist by name: '{exist[0]}', you can use !load and enter the name next time instead.")
            return True
        return False
    
    def _save_current_config(self, config_name:str) -> None:
        """
        save config with name(to access later) in json file.

        Args:
            config_name (str): name of config
        """
        store_data:dict[str, dict[str, str]] | dict = self.saved_configs
        store_data.update({config_name: self.configs})
        with open(path, mode="w") as save_file:
            json.dump(obj=store_data, fp=save_file, indent=4)
        print(f"configuration saved successfully.")

    def _update_saved_configs(self) -> None:
        """
        update json file with modified history saves
        """
        with open(path, mode="r") as save_file:
            self.saved_configs:dict[str, dict[str, str]] | dict = json.load(save_file)
    
    def _get_saved_names(self) -> list[str]:
        """
        returns every history save config names

        Returns:
            list[str]: list of save config names
        """
        return [key for key in self.saved_configs]

    def _name_exist(self, name:str, default_check:bool) -> str | None:
        """
        make user enter config name that exist in history saves.

        Args:
            name (str): config name
            default_check (bool): whether to check if user enter default

        Returns:
            str | None: str, when user enter config name exist,
                        None, when user try modify default.
        """
        # ignore the logic of the code in Organizer(), i know it's nonsence.(this is ver.2 btw lmao)
        if self._config_name_exist(name):
            return name
        while name not in self._get_saved_names():
            print(f"name didn't exist, all previous saved names: {self._get_saved_names()}")
            name = input("enter another iput: ")
            if default_check and name == 'default':
                print('input most not be default.')
                name = "this placeholder surely will not be in config.json right?!~"
        return name
