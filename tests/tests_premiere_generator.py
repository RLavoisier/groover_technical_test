import unittest

from premiere_generator import PremiereGenerator
from track import Track


class MyTestCase(unittest.TestCase):
    def test_premiere_generator(self):
        assert len(self.premiere_generator.tracks) == 3

    def test_get_set_lists(self):
        set_lists = self.premiere_generator._get_set_lists(self.premiere_generator.tracks, 2)

        assert len(list(set_lists)) == 6

    def tests_is_suitable(self):
        set_list = [
            Track("track1", 3),
            Track("track2", 2),
        ]

        assert self.premiere_generator._is_suitable(set_list, 5, 0)
        assert self.premiere_generator._is_suitable(set_list, 8, 3)
        assert self.premiere_generator._is_suitable(set_list, 3, 2)

    def test_get_first_suitable_set_list(self):
        set_list = self.premiere_generator.get_first_suitable_set_list(8)
        assert len(set_list.tracks) == 2
        set_list = self.premiere_generator.get_first_suitable_set_list(1)
        assert set_list == None
        set_list = self.premiere_generator.get_first_suitable_set_list(1, 1)
        assert len(set_list.tracks) == 1

    def test_get_premiere_set_lists(self):
        set_lists = self.premiere_generator.get_premiere_set_lists(14, 0, 3)
        assert len(set_lists) == 1
        set_lists = self.premiere_generator.get_premiere_set_lists(10, 2, 2)
        assert len(set_lists) == 3
        set_lists = self.premiere_generator.get_premiere_set_lists(20, 2, 3)
        assert len(set_lists) == 0

    @classmethod
    def setUpClass(cls):
        cls.premiere_generator = PremiereGenerator("tests/test_tracks.csv")


if __name__ == '__main__':
    unittest.main()
