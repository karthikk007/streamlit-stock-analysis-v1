from creation_pattern.singletion import SingletonDoubleChecked


class StockEngine(SingletonDoubleChecked):
    def __init__(self) -> None:
        super().__init__()