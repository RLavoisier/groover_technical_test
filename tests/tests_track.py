import unittest

from track import Track


class MyTestCase(unittest.TestCase):
    def test_sum(self):
        track1 = Track("track1", 10)
        track2 = Track("track2", 10)

        assert sum([track1, track2]) == 20

    def test_comparison(self):
        track1 = Track("track1", 10)
        track2 = Track("track2", 10)
        track3 = Track("track1", 10)

        track_set = {track1, track2, track3,}

        assert len(track_set) == 2

    def test_add(self):
        track1 = Track("track1", 15)
        track2 = Track("track2", 10)

        assert track1 + track2 == 25

if __name__ == '__main__':
    unittest.main()
