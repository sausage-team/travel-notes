from core.bean.wrapper import *

class UserWrapper(Wrapper):
    filter = ['id_card', 'password']

    def __init__(self, status=0, data={}):
        if isinstance(data, list):
            for val in data:
                self.remove_key(val)
        else:
            self.remove_key(data)
        super().__init__(status, data)