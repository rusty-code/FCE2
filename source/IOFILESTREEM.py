
import os

class FileInstance:
    """File instance interface"""

    def __init__(
            self, 
            path : str, 
        ):

        self._PATH = path

        self._FILE_DATA = [] # ['strings']
        with open(self._PATH, 'r') as file:
                for string in file.readlines():
                    self._FILE_DATA.append(
                            # remove '\n'
                            self._remove_new_str_symb(string)
                        )

    def _remove_new_str_symb(self, string):
        out = ''
        for wd in string:
            if wd == '\n':
                return out
            out = out + wd

        return out # string hasn`t '\n'
            
    # getters
    def get_path(self):
        return self._PATH
    
    def write(
            self, 
            data : list, 
            mode = 'a',
            beginstr = '',
            endstr = '\n'
        ):
        if mode == 'w': # rewrite file
            self._FILE_DATA = []
        try:
            with open(self._PATH, mode) as file:
                for string in data:
                    file.write(
                        f'{beginstr}{string}{endstr}')

                    self._FILE_DATA.append(
                        f'{string}')

        except FileNotFoundError:
            print(f"(ERROR) no such of file: '{self._PATH}'")

    def read(self):
        print(f"(OUTPUT) from file: {self._PATH}") 
        for string in self._FILE_DATA:
            print(string)

    def data(self):
        return self._FILE_DATA

    def delete(self):
        pass    




































































































































































































































































































































"""
by Batrakov Yaroslav
"""