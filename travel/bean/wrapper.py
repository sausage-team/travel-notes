from rest_framework.response import Response
"""
Wrapper for formating json response
"""
class Wrapper(dict):
    """
    Wrapper Dict
    """
    def __init__(self, status=0, data={}, default=None):
        """
        Initializer
        """
        super().__init__(self)
        self.__setitem__('status', status)
        self.__setitem__('data', data)
        self.default = default

    def __getitem__(self, key):
        """
        Overide __getitem__
        """
        try:
            return self.__getitem__('key')
        except KeyError:
            return self.default

SUCCESS = Response(Wrapper(0, data={'msg':'ok'}))
FAIL = Response(Wrapper(-1, data={'msg':'error'}))
