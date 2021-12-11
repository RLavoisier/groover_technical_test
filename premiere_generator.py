import csv
import logging
from typing import List, Iterator

from globals import (
    DEFAULT_TOLERANCE,
    DEFAULT_NB_TRACKS,
    DEFAULT_CONCERT_PREMIERE_LENGTH,
    DEFAULT_TRACKS_FILE,
)
from set_list import SetList
from track import Track


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("groover")


class PremiereGenerator:
    def __init__(self, track_file: str = DEFAULT_TRACKS_FILE):
        """This class handle the generation of a set list for a premiere at groover concert
        Though, it will not handle guitar feedback problems and musicians beeing late
        """
        self.tracks = self._get_tracks_from_file(track_file)

    def _get_tracks_from_file(self, track_file: str) -> List[Track]:
        """This method parse a list of tracks with the following format :
        {track_name};{duration_in_minutes}

        :param track_file: the local file where the track cans be found
        :return: A list of Track objects
        """
        tracks = set()
        with open(track_file, "r") as f:
            file_reader = csv.reader(f, delimiter=";")
            for track in file_reader:
                try:
                    tracks.add(Track(track[0], int(track[1])))
                except ValueError:
                    logger.error(f"Invalid length for track {track[0]}")
                except IndexError:
                    logger.error(
                        "Incomplete track entry, format must be: track_name;duration_in_minutes"
                    )

        logger.info(f"{len(tracks)} tracks found in {track_file}")
        return list(tracks)

    def get_premiere_set_lists(
        self,
        concert_premiere_length: int = DEFAULT_CONCERT_PREMIERE_LENGTH,
        tolerance: int = DEFAULT_TOLERANCE,
        nb_tracks: int = DEFAULT_NB_TRACKS,
    ) -> List[SetList]:
        """Returns a list of set_list of size nb_tracks
        and for a length that fits the premiere length with optionnal tolerance modifier

        :param concert_premiere_length: max length for the 3 tracks selected
        :param tolerance: filter a set of tracks which is total length +/- tolerance
        :param nb_tracks: number of tracks that should be contained in a set
        :return: a list of 3 tracks suited for the premiere parameters
        """
        set_lists = self._get_set_lists(self.tracks, nb_tracks)
        filtered_set_lists = []

        # Filtering the set lists
        processed_set = []
        for set_list in set_lists:
            if set(set_list) in processed_set:
                continue
            else:
                processed_set.append(set(set_list))

            if self._is_suitable(set_list, concert_premiere_length, tolerance):
                filtered_set_lists.append(SetList(set_list))

        return filtered_set_lists

    def get_first_suitable_set_list(
        self,
        concert_premiere_length: int = DEFAULT_CONCERT_PREMIERE_LENGTH,
        tolerance: int = DEFAULT_TOLERANCE,
    ) -> SetList or None:
        """This method returns the first suitable set list for the given length and tolerance"""
        nb_tracks = len(self.tracks)
        for i in range(1, nb_tracks):
            too_long = []
            for set_list in self._get_set_lists(self.tracks, i):
                if self._is_suitable(set_list, concert_premiere_length, tolerance):
                    return SetList(set_list)
                else:
                    too_long.append(sum(set_list) > concert_premiere_length + tolerance)
            # To avoid useless loop, we return none if all the last set
            # are timed above concert_premiere_length + tolerance
            if too_long and all(too_long):
                return None

    def _is_suitable(
        self, set_list: List[Track], concert_premiere_length: int, tolerance: int
    ) -> bool:
        """This method check if a set is suitable uppon the parameters"""
        set_list_duration = sum(set_list)

        if not tolerance and set_list_duration == concert_premiere_length:
            return True
        else:
            if (
                concert_premiere_length + tolerance
                >= set_list_duration
                >= concert_premiere_length - tolerance
            ):
                return True
        return False

    def _get_set_lists(
        self, track_list: List[Track], nb_tracks: int
    ) -> Iterator[List[Track]]:
        """This method build recursively the list of all the set_list from the current track list

        :param track_list: the list of tracks from which set°list are generated
        :param nb_tracks: the number of tracks that should be contained in a set
        :return: a list of set list of nb_tracks tracks
        """
        if nb_tracks == 1:
            for track in track_list:
                yield [
                    track,
                ]
        else:
            for i in range(len(track_list)):
                for yielded_set_list in self._get_set_lists(
                    track_list[:i] + track_list[i + 1 :], nb_tracks - 1
                ):
                    # Each level of recursion provides 1 + x tracks (max of nbtracks)
                    # Just a reinterpretation of itertools.combinations
                    yield [track_list[i]] + yielded_set_list
