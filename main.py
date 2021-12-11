import argparse
import logging
import time
from os import path

from globals import (
    DEFAULT_TRACKS_FILE,
    DEFAULT_NB_TRACKS,
    DEFAULT_CONCERT_PREMIERE_LENGTH,
    DEFAULT_TOLERANCE,
)
from premiere_generator import PremiereGenerator


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("groover")

# Parsing the command args
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=False)
parser.add_argument("-nt", "--nb_tracks", required=False)
parser.add_argument("-d", "--concert_premiere_length", required=False)
parser.add_argument("-t", "--tolerance", required=False)
parser.add_argument("-a", "--auto", required=False)
args = parser.parse_args()

if __name__ == "__main__":
    # Time stats
    start_time = time.perf_counter()

    track_file = args.file or DEFAULT_TRACKS_FILE
    # ensuring the track file
    if not path.isfile(track_file):
        logger.error(f"{track_file} not found.")
        quit()

    # ensuring args format
    try:
        nb_tracks = int(args.nb_tracks or DEFAULT_NB_TRACKS)
        concert_premiere_length = int(args.concert_premiere_length or DEFAULT_CONCERT_PREMIERE_LENGTH)
        tolerance = int(args.tolerance or DEFAULT_TOLERANCE)
    except ValueError:
        logger.error(
            "nb_tracks, concert_premiere_length and tolerance should be an integers."
        )
        quit()
    auto_choose = bool(args.auto) or False

    premiere_generator = PremiereGenerator(track_file)
    if auto_choose:
        # auto choose get the first suitable set for the given premiere
        set_lists = []
        set_list = premiere_generator.get_first_suitable_set_list(
            concert_premiere_length, tolerance
        )
        if set_list:
            nb_tracks = len(set_list)
            set_lists.append(set_list)
    else:
        set_lists = premiere_generator.get_premiere_set_lists(
            concert_premiere_length, tolerance, nb_tracks
        )
    tolerance_txt = f" (with {tolerance}min tolerance)" if tolerance else ""
    print(
        f"For a premiere of {concert_premiere_length}min{tolerance_txt} we found {len(set_lists)} suitable set list(s) of {nb_tracks} tracks :"
    )
    if set_lists:
        print("*" * 60)
        for i, set in enumerate(set_lists, 1):
            print(
                f"{i} - {', '.join(t.name for t in set.tracks)} - {set.length}min"
            )
        print("*" * 60)
    stop_time = time.perf_counter()

    print(
        f"Results provided by Groover at the lighting fast speed of {stop_time - start_time:0.4f} seconds"
    )
