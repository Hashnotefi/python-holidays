#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td

from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAY,
    JUN,
    JUL,
    NOV,
    DEC,
    MON,
    _get_nth_weekday_of_month,
)
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class FederalReserve(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Official regulations:
    - https://www.federalreserve.gov/aboutthefed/k8.htm
    """

    market = "FEDRESERVE"
    special_holidays = {}

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed_holiday(self, name: str, dt: date) -> None:
        if self._is_saturday(dt):
            dt += td(days=-1)
            name = f"{name} (Observed)"
        elif self._is_sunday(dt):
            dt += td(days=+1)
            name = f"{name} (Observed)"

        self._add_holiday(name, dt)

    def _populate(self, year):
        super()._populate(year)

        # New Year Day.
        jan_1 = date(year, JAN, 1)
        if not self._is_saturday(jan_1):
            self._add_observed_holiday("New Year's Day", jan_1)

        # https://www.nyse.com/publicdocs/nyse/regulation/nyse/NYSE_Rules.pdf
        # As per Rule 7.2.: check if next year's NYD falls on Saturday and
        # needs to be observed on Friday (Dec 31 of previous year).
        dec_31 = date(year, DEC, 31)
        if self._is_friday(dec_31):
            self._add_observed_holiday("New Year's Day", dec_31 + td(days=+1))

        # MLK, 3rd Monday of January.
        if year >= 1998:
            self._add_holiday_3rd_mon_of_jan("Martin Luther King Jr. Day")

        # WASHINGTON'S BIRTHDAY: Feb 22 (obs) until 1971, then 3rd Mon of Feb
        self._add_observed_holiday(
            "Washington's Birthday",
            date(year, FEB, 22)
            if year <= 1970
            else _get_nth_weekday_of_month(3, MON, FEB, self._year),
        )

        # MEM DAY (May 30) - closed every year since 1873
        # last Mon in May since 1971
        if year >= 1873:
            self._add_observed_holiday(
                "Memorial Day",
                date(year, MAY, 30)
                if year <= 1970
                else _get_nth_weekday_of_month(-1, MON, MAY, self._year),
            )

        # JUNETEENTH: since 2021
        if year >= 2021:
            self._add_observed_holiday("Juneteenth National Independence Day", date(year, JUN, 19))

        # INDEPENDENCE DAY (July 4) - history suggests closed every year
        self._add_observed_holiday("Independence Day", date(year, JUL, 4))

        # LABOR DAY - first mon in Sept, since 1887
        if year >= 1887:
            self._add_holiday_1st_mon_of_sep("Labor Day")

        # COLUMBUS DAY/INDIGENOUS PPL DAY
        if 1909 <= year:
            self._add_holiday_2nd_mon_of_oct("Columbus Day")

        # VETERAN'S DAY
        if year in {1918, 1921} or 1934 <= year:
            self._add_observed_holiday("Veteran's Day", date(year, NOV, 11))

        # THXGIVING DAY: 4th Thurs in Nov - closed every year
        self._add_holiday_4th_thu_of_nov("Thanksgiving Day")

        # XMAS DAY: Dec 25th - every year
        self._add_observed_holiday("Christmas Day", date(year, DEC, 25))


class FEDRESERVE(FederalReserve):
    pass


class FRES(FederalReserve):
    pass
