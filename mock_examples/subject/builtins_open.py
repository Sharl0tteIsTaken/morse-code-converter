import json

class BuiltinsOpen():
    """
    the purpose of the package is to test a try except block from day82,
    the try except block will catch error without problem,
    after some digging on the internet I found out that there's nearly no point
    to unittest this part of code, so there goes that.
    
    this package also have working example of mocking default keyword `open`,
    so it's not deleted, but preserved.
    
    """
    # cite: https://stackoverflow.com/questions/57978703/python-unit-test-for-try-except-block
    # cite: https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
    def get_data(self, filepath):
        print('obj called')
        try:
            with open(filepath) as f:
                data = json.load(f)
                print('file exist')
                print(data['b'])
                return 'file exist'
        except FileNotFoundError:
            print('not found')
            return 'not found'
        except KeyError:
            print('ker error')
            return 'ker error'
