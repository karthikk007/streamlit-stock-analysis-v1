import datetime


class DataModel(object):

    def __init__(self) -> None:
        self.timestamp = datetime.datetime.now().date()

    @staticmethod
    def from_json(dict):
        return DataModel()