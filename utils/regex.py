"""Regular expressions to be used as filters for message handlers."""

import re

START_ONLY_RE = re.compile(r"^([01]?\d|2[0-3])$")
START_AND_END_RE = re.compile(r"^([01]?\d|2[0-3])-([01]?\d|2[0-3])$")
DAY_AND_START_RE = re.compile(
    r"^(mon|tue(s)?|wed(nes)?|thu(r(s)?)?|fri|sat(ur)?)(day)?\s+([01]?\d|2[0-3])$",
    re.IGNORECASE,
)
ALL_PARAMS_RE = re.compile(
    r"^(mon|tue(s)?|wed(nes)?|thu(r(s)?)?|fri|sat(ur)?)(day)?\s+([01]?\d|2[0-3])-([01]?\d|2[0-3])$",
    re.IGNORECASE,
)
WEEKDAYS_RE = re.compile(r"^(Mon|Tues|Wednes|Thurs|Fri|Satur)day$")
JOJO_RE = re.compile(r"(JO\s+JO)", re.IGNORECASE)
