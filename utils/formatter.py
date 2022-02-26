"""Only one function that prepares a text string to be sent to the user."""

from typing import Dict, List


def format_dict(data: Dict[str, List[str]]) -> str:
    """Prepare a string to send back to the user.

    Parameters
    ----------
    data : Dict[str, List[str]]
        a dictionary with building names as the keys and empty rooms at those
        buildings as the value

    Returns
    -------
    str
        a text message to be sent back to the user

    >>> format_dict({"ATB": ["ATB209", "ATB214"], "IB": ["IB209"]})
    These rooms are available:
    \nATB
    ATB209, ATB214
    \nIB
    IB209
    """

    text = "These rooms are available:"

    for building, rooms in data.items():
        text += f"\n\n<b>{building}</b>\n{', '.join(rooms)}"

    return text
