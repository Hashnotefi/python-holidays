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
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    WED,
    SAT,
    SUN,
)
from holidays.financial.federal_reserve import FederalReserve
from tests.common import TestCase


class TestFederalReserve(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(FederalReserve)

    def test_new_years(self):
        for dt in (
            date(1900, JAN, 1),
            date(1930, JAN, 1),
            date(1950, JAN, 2),
            date(1999, JAN, 1),
            date(1999, DEC, 31),
            date(2010, JAN, 1),
            date(2018, JAN, 1),
            date(2019, JAN, 1),
            date(2020, JAN, 1),
            date(2021, JAN, 1),
            date(2021, DEC, 31),
            date(2027, DEC, 31),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(dt + td(days=-1))
            self.assertNoHoliday(dt + td(days=+1))
            self.assertNoHoliday(dt + td(days=+7))

        # observed on previous year Dec 31
        for dt in (
            date(1994, JAN, 1),
            date(2000, JAN, 1),
            date(2005, JAN, 1),
            date(2011, JAN, 1),
            date(2022, JAN, 1),
        ):
            self.assertNoHoliday(dt)
            self.assertHoliday(dt + td(days=-1))

    def test_mlk(self):
        for dt in (
            date(1999, JAN, 18),
            date(2000, JAN, 17),
            date(2010, JAN, 18),
            date(2018, JAN, 15),
            date(2019, JAN, 21),
            date(2020, JAN, 20),
            date(2021, JAN, 18),
            date(2022, JAN, 17),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(dt + td(days=-1))
            self.assertNoHoliday(dt + td(days=+1))
            self.assertNoHoliday(dt + td(days=+7))
            self.assertNoHoliday(dt + td(days=-7))

        for dt in (
            date(1997, JAN, 20),
            date(1985, JAN, 21),
        ):
            self.assertNoHoliday(dt)

    def test_washington(self):
        for dt in (
            date(1900, FEB, 22),
            date(1930, FEB, 21),
            date(1950, FEB, 22),
            date(1960, FEB, 22),
            date(1965, FEB, 22),
            date(1970, FEB, 23),
            date(1971, FEB, 15),
            date(1999, FEB, 15),
            date(2000, FEB, 21),
            date(2010, FEB, 15),
            date(2018, FEB, 19),
            date(2019, FEB, 18),
            date(2020, FEB, 17),
            date(2021, FEB, 15),
            date(2022, FEB, 21),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(dt + td(days=-1))
            self.assertNoHoliday(dt + td(days=+1))
            self.assertNoHoliday(dt + td(days=+7))
            self.assertNoHoliday(dt + td(days=-7))

    def test_memday(self):
        for dt in (
            date(1901, MAY, 30),
            date(1902, MAY, 30),
            date(1930, MAY, 30),
            date(1950, MAY, 30),
            date(1960, MAY, 30),
            date(1965, MAY, 31),
            date(1971, MAY, 31),
            date(1999, MAY, 31),
            date(2000, MAY, 29),
            date(2010, MAY, 31),
            date(2018, MAY, 28),
            date(2019, MAY, 27),
            date(2020, MAY, 25),
            date(2021, MAY, 31),
            date(2022, MAY, 30),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(dt + td(days=-1))
            self.assertNoHoliday(dt + td(days=+1))
            self.assertNoHoliday(dt + td(days=+7))
            self.assertNoHoliday(dt + td(days=-7))

        self.assertNoHoliday(date(1872, MAY, 30))

    def test_juneteenth(self):
        for dt in (
            date(2021, JUN, 18),
            date(2022, JUN, 20),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(dt + td(days=-1))
            self.assertNoHoliday(dt + td(days=+1))
            self.assertNoHoliday(dt + td(days=+7))
            self.assertNoHoliday(dt + td(days=-7))

        for dt in (
            date(1954, JUN, 18),
            date(1967, JUN, 19),
        ):
            self.assertNoHoliday(dt)

    def test_laborday(self):
        for dt in (
            date(1887, SEP, 5),
            date(1901, SEP, 2),
            date(1902, SEP, 1),
            date(1950, SEP, 4),
            date(1999, SEP, 6),
            date(2000, SEP, 4),
            date(2010, SEP, 6),
            date(2018, SEP, 3),
            date(2019, SEP, 2),
            date(2020, SEP, 7),
            date(2021, SEP, 6),
            date(2022, SEP, 5),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(dt + td(days=-1))
            self.assertNoHoliday(dt + td(days=+1))
            self.assertNoHoliday(dt + td(days=+7))
            self.assertNoHoliday(dt + td(days=-7))

        self.assertNoHoliday(date(1886, SEP, 6))

    def test_columbusday(self):
        for dt in (
            date(2023, OCT, 9),
            date(2024, OCT, 14),
            date(2025, OCT, 13),
            date(2026, OCT, 12),
            date(2027, OCT, 11),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(dt + td(days=-1))
            self.assertNoHoliday(dt + td(days=+1))
            self.assertNoHoliday(dt + td(days=+7))
            self.assertNoHoliday(dt + td(days=-7))

        for dt in (date(1908, OCT, 12),):
            self.assertNoHoliday(dt)

    def test_veteransday(self):
        for dt in (
            date(1918, NOV, 11),
            date(1921, NOV, 11),
            date(1934, NOV, 12),
            date(1938, NOV, 11),
            date(1942, NOV, 11),
            date(1946, NOV, 11),
            date(1950, NOV, 10),
            date(1953, NOV, 11),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(dt + td(days=-1))
            self.assertNoHoliday(dt + td(days=+1))
            self.assertNoHoliday(dt + td(days=+7))
            self.assertNoHoliday(dt + td(days=-7))

        for dt in (
            date(1917, NOV, 12),
            date(1919, NOV, 11),
            date(1920, NOV, 11),
            date(1922, NOV, 10),
            date(1933, NOV, 10),
        ):
            self.assertNoHoliday(dt)

    def test_thxgiving(self):
        for dt in (
            date(1901, NOV, 28),
            date(1902, NOV, 27),
            date(1950, NOV, 23),
            date(1999, NOV, 25),
            date(2000, NOV, 23),
            date(2010, NOV, 25),
            date(2018, NOV, 22),
            date(2019, NOV, 28),
            date(2020, NOV, 26),
            date(2021, NOV, 25),
            date(2022, NOV, 24),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(dt + td(days=-1))
            self.assertNoHoliday(dt + td(days=+1))
            self.assertNoHoliday(dt + td(days=+7))
            self.assertNoHoliday(dt + td(days=-7))

    def test_christmas_day(self):
        for dt in (
            date(1901, DEC, 25),
            date(1902, DEC, 25),
            date(1950, DEC, 25),
            date(1999, DEC, 24),
            date(2000, DEC, 25),
            date(2010, DEC, 24),
            date(2018, DEC, 25),
            date(2019, DEC, 25),
            date(2020, DEC, 25),
            date(2021, DEC, 24),
            date(2022, DEC, 26),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(dt + td(days=-1))
            self.assertNoHoliday(dt + td(days=+1))
            self.assertNoHoliday(dt + td(days=-7))

    def test_all_modern_holidays_present(self):
        self.assertHolidays(
            ("2021-01-01", "New Year's Day"),
            ("2021-01-18", "Martin Luther King Jr. Day"),
            ("2021-02-15", "Washington's Birthday"),
            ("2021-05-31", "Memorial Day"),
            ("2021-06-18", "Juneteenth National Independence Day (Observed)"),
            ("2021-07-05", "Independence Day (Observed)"),
            ("2021-09-06", "Labor Day"),
            ("2021-10-11", "Columbus Day"),
            ("2021-11-11", "Veteran's Day"),
            ("2021-11-25", "Thanksgiving Day"),
            ("2021-12-24", "Christmas Day (Observed)"),
            ("2021-12-31", "New Year's Day (Observed)"),
        )
