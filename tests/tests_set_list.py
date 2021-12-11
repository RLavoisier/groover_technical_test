import unittest

from set_list import SetList
from track import Track


class MyTestCase(unittest.TestCase):
    def test_set_list(self):
        track1 = Track("track1", 10)
        track2 = Track("track2", 10)

        set_list = SetList([track1, track2])

        assert len(set_list) == 2
        assert set_list.length == 20


if __name__ == '__main__':
    unittest.main()
