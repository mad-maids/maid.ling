"""Simple GET request to the API."""

import logging
from typing import Dict, List, Optional, Union

import aiohttp.client_exceptions as exceptions

from data.constants import GET_ROOMS_URL
from loader import session


async def get_empty_rooms(
    start: int, end: Optional[int] = None, weekday: Optional[str] = None
) -> Union[List[str], None]:
    """Make a GET request to the API to find empty rooms.

    Parameters
    ----------
    start : int
        start hour provided by the user
    end : Optional[int]
        end hour if provided by the user, if not provided the API will return
        all empty rooms for the [start - start + 1 hour] time slot
    weekday : Optional[str]
        day of the week for which an empty room is needed, if not provided by
        the user, the API will take today's weekday as a default

    Returns
    -------
    Union[List[str], None]
        list of empty rooms or None if the request failed
    """

    params: Dict[str, Union[str, int]] = {"start": start}

    if end:
        params["end"] = end
    if weekday:
        params["day"] = weekday

    try:
        async with session.get(GET_ROOMS_URL, params=params) as resp:
            empty_rooms = await resp.json(encoding="utf-8")
            try:
                resp.raise_for_status()
            except exceptions.ClientResponseError:
                logging.exception(
                    f"GET request failed: {empty_rooms['errorMsg']}"
                )
            else:
                return empty_rooms
    except exceptions.ClientConnectorError as e:
        logging.exception(e)
