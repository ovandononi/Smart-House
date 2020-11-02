from json import loads
from os.path import join
from os.path import dirname, realpath


class ReaderFile(object):
    def __init__(self):
        self.path = dirname(realpath(__file__))

    def get_config_data(self):
        return loads(open(join(self.path, 'data.json')).read())
