# Groover technical test

## Usage
**Simple usage :**

```
python main.py
```
This will launch the premiere generator with the following default parameters:
```
premiere_duration: 10min
nb_track: 3
track_file: data/tracks.csv
```
 **Available parameters**
```
-a or --auto 
```
Set it to one to automatically fetch the first set list suitable for the premiere. 

Default: False

```
-f or --file 
```
Set a path to a csv file containing your own list of tracks. The format should be : name;duration (ex: Whole lotta love;3)

Default: data/tracks.csv

```
-nt or --nb_tracks 
```
Set the number of tracks you wish to see in the generated set lists. Note that this parameter is disabled if you set --auto

Default: 3 

```
-d or --concert_premiere_length 
```
Set the length in minutes of the premiere

Default: 11

```
-t or --tolerance
```
Set the tolerance in minutes. This will alllow for a broader search of suitable set list.

Default: 0



## Problem to solve:

In Groover, we are creating more and more concerts / open stages as the first part of partner concerts to introduce talents from our platform!

However these first parts often have a limited time constraint *concert_premiere_length* in minutes and we must make sure to offer a succession of songs whose sum of the individual durations in minutes *Σtrack_length* = *concert_premiere_length*, *exactly*! 

Given a list of lengths (in minutes) of pieces of music [*track_length*] propose a function that returns a *Boolean True / False* indicating if there are 3 tracks whose sum duration is exactly the duration of *concert_premiere_length*.

We consider that  *concert_premiere_length*  and the durations  *track_length* are positive integers.

## Constraints:

- The spectators expect exactly 3 pieces in this concert first part *concert_premiere*
- We cannot offer the same song in double or triple, each song must be offered only once
- Optimize the runtime over the memory in the solution

# Technical specifications :

- Imposed technical stack:
    - Python 3
    - Third-party libraries, usage of threads/processes are not allowed
    - itertools is forbidden in this exercice, we want you to try building an approach using simple datastructures

**The final work needs to be accessible in a GitHub repository. Having a nice commit history is always a plus.**

## Bonus questions (not required!, you can pick one or try both, or none):

- generalizing: what if we remove the limit of 3 tracks, and want to find the first match for  *concert_premiere_length*? *it can be 1,2,3,4..* or more tracks in [track_lengths].
- what if we stuck to exactly 3 tracks but allowed the sum to be close enough to *concert_premiere_length* with a 5 min -/+ tolerance?

