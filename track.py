class Track:
    def __init__(self, name: str, length: int):
        """This class represent a particular track

        For convenience it implements the __add__ and __eq__ methods
        """
        self.name = name
        self.length = length

    def __add__(self, other):
        if isinstance(other, Track):
            return self.length + other.length
        elif isinstance(other, type(self.length)):
            return self.length + other

    def __radd__(self, other):
        if other == 0:
            return self.length
        else:
            return self.__add__(other)

    def __eq__(self, other):
        if isinstance(other, Track):
            return (self.name == other.name) and (self.length == other.length)
        else:
            return False

    def __repr__(self):
        return f"{self.name} - {self.length}min"

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
