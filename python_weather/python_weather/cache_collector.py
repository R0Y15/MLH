from gc import collect

class cache_collector(dict):
    __slots__ = ('max_size',)

    def __rep__(self) -> str:
        return f"<Cache size={len(self.keys())} max_size={self.max_size}>"

    def __init__(self, max_size: int = 15) -> dict:
        self.max_size = max_size if isinstance(max_size, int) and (0 < max_size <= 100) else 15
        super().__init__()

    def __set_item__(self, key, value) -> None:
        if len(self.keys()) == self.max_size:
            dict.pop(self, list(self.keys())[0])
        
        dict.__setitem__(self, key, value)
    
    def clean(self) -> None:
        dict.clear(self)
        collect()