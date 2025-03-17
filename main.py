import json

class Chess:
    def __init__(self, filename):
        with open(filename) as f:
            self.__dict__ = json.loads(f.read())

chess = Chess('settings.json')
print (chess.__dict__)