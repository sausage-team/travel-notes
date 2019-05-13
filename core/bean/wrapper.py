from rest_framework.response import Response
"""
Wrapper for formating json response
"""
class Wrapper(dict):
    """
    Wrapper Dict
    """
    STATUS = 'status'
    DATA = 'data'
    filter = []
    def __init__(self, status=0, data={}, default=None):
        """
        Initializer
        """
        super().__init__(self)
        super().__setitem__(Wrapper.STATUS, status)
        super().__setitem__(Wrapper.DATA, data)
        self.default = default

    def __getitem__(self, key):
        """
        Overide __getitem__
        """
        print("我被调用啦 Wrapper")
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.default
    
    def remove_key(self, data):
        for k in self.filter:
            if k in data:
               data.__delitem__(k)

SUCCESS = Response(Wrapper(0, data={'msg':'ok'}))
FAIL = Response(Wrapper(-1, data={'msg':'error'}))
