class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value!r})"
    
    def __str__(self) -> str:
        return f"{self.value}"
