# -*- coding: utf-8 -*-
from json import loads,JSONEncoder

class TweetsEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return loads(str(obj, encoding='utf-8'))
        return JSONEncoder.default(self, obj)
