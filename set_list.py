from typing import Iterable

from track import Track


class SetList:
    def __init__(self, track_list: Iterable[Track] = None):
        """This class represents a set list"""
        self.tracks = list(track_list)

    @property
    def length(self):
        return sum(self.tracks)

    def __len__(self):
        return len(self.tracks)

    def __repr__(self):
        return f"Set list {sum(self.tracks)}min, {self.__len__()} song(s)"

    def __eq__(self, other):
        if isinstance(other, SetList):
            return set(self.tracks) == set(other.tracks)
        else:
            return False
