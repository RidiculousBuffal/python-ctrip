class NoDataException(Exception):
    def __init__(self, query:str):
        super().__init__(f"{query} 找不到")