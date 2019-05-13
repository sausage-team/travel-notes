from core.bean.wrapper import *

class ArticleWrapper(Wrapper):
    filter = ['user']

    def __init__(self, status=0, data={}):
        if isinstance(data, list):
            for val in data:
                self.remove_key(val)
        else:
            self.remove_key(data)
        super().__init__(status, data)
    
    def remove_key(self, data):
        for k in self.filter:
            if k in data:
               data.__delitem__(k)