import sys

from uvpm_core import packer, IslandFlag, Box, Point, IslandSet, fixed_scale_enabled, ScaleMode


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def flag_islands(input_islands, flagged_islands):
    if len(flagged_islands) == 0:
        return

    input_islands.clear_flags(IslandFlag.SELECTED)
    flagged_islands.set_flags(IslandFlag.SELECTED)

    to_send = input_islands.clone()
    to_send += flagged_islands
    packer.send_out_islands(to_send, send_flags=True)


def box_from_coords(coords):
    return Box(Point(coords[0], coords[1]), Point(coords[2], coords[3]))


def area_to_string(area):
    return "{:.3f}".format(area)


def split_islands(islands, pred):
    set1 = IslandSet()
    set2 = IslandSet()

    for island in islands:
        (set1 if pred(island) else set2).append(island)

    return set1, set2


def adjust_scale_mode(scale_mode, tdensity_value):
    if (tdensity_value > 0) and not fixed_scale_enabled(scale_mode):
        scale_mode = ScaleMode.FIXED_SCALE
        
    return scale_mode
