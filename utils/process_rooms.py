"""Categorizing rooms to their respective buildings here.

Hopefully this will make the user experience slightly less worse.
"""

from typing import Dict, List


def process_rooms(rooms: List[str]) -> Dict[str, List[str]]:
    """Categorize rooms into their buildings.

    Parameters
    ----------
    rooms : List[str]
        the list of empty rooms

    Returns
    -------
    Dict[str, List[str]]
        a dictionary with the building name as the key and list of that
        building's room as the value

    >>> process_rooms(["ATB209", "ATB214", "IB209"])
    {'ATB': ['ATB209', 'ATB214'], 'IB': ['IB209']}
    """

    processed_rooms = dict()

    for room in rooms:
        if room.startswith("ATB") or room in ("Blue room", "Harvard306"):
            atb = processed_rooms.setdefault("ATB", [])
            atb.append(room)
        elif room.startswith("IB"):
            ib = processed_rooms.setdefault("IB", [])
            ib.append(room)
        elif room.startswith("LRC"):
            lrc = processed_rooms.setdefault("LRC", [])
            lrc.append(room)
        elif room.startswith("New"):
            new_building = processed_rooms.setdefault("NEW", [])
            new_building.append(room)
        else:
            unknown = processed_rooms.setdefault("unknown", [])
            unknown.append(room)

    return processed_rooms
