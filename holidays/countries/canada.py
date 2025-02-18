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
from gettext import gettext as tr

from holidays.calendars.gregorian import MAR, APR, JUN, JUL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    ALL_TO_NEAREST_MON,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
    SUN_TO_NEXT_MON,
)


class Canada(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    country = "CA"
    default_language = "en"
    # %s (Observed).
    observed_label = tr("%s (Observed)")
    subdivisions = (
        "AB",
        "BC",
        "MB",
        "NB",
        "NL",
        "NS",
        "NT",
        "NU",
        "ON",
        "PE",
        "QC",
        "SK",
        "YT",
    )
    supported_languages = ("ar", "en", "fr", "th")

    def __init__(self, *args, **kwargs):
        # Default subdivision to ON; prov for backwards compatibility
        if not kwargs.get("subdiv", kwargs.get("prov")):
            kwargs["subdiv"] = "ON"
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(observed_rule=SAT_SUN_TO_NEXT_MON, *args, **kwargs)

    def _get_nearest_monday(self, *args) -> date:
        return self._get_observed_date(date(self._year, *args), rule=ALL_TO_NEAREST_MON)

    def _populate(self, year):
        if year <= 1866:
            return None

        super()._populate(year)

        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))
        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        if year <= 1982:
            # Dominion Day.
            self._add_observed(self._add_holiday_jul_1(tr("Dominion Day")))

        if self._year >= 1894:
            # Labour Day.
            self._add_holiday_1st_mon_of_sep(tr("Labour Day"))

        self._add_observed(
            # Christmas Day.
            self._add_christmas_day(tr("Christmas Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

        self._add_observed(
            # Boxing Day.
            self._add_christmas_day_two(tr("Boxing Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

    def _add_family_day(self):
        # Family Day.
        self._add_holiday_3rd_mon_of_feb(tr("Family Day"))

    def _add_thanksgiving(self):
        if self._year >= 1931:
            # Thanksgiving.
            name = tr("Thanksgiving")
            # in 1935, Canadian Thanksgiving was moved due to the General
            # Election falling on the second Monday of October
            # http://tiny.cc/can_thkgvg
            if self._year == 1935:
                self._add_holiday_oct_25(name)
            else:
                self._add_holiday_2nd_mon_of_oct(name)

    def _add_queens_funeral(self):
        if self._year == 2022:
            # Funeral of Queen Elizabeth II.
            self._add_holiday_sep_19(tr("Funeral of Her Majesty the Queen Elizabeth II"))

    def _add_subdiv_holidays(self):
        if self._year >= 1983:
            self._add_observed(
                self._add_holiday_jul_1(
                    (
                        # Memorial Day.
                        tr("Memorial Day")
                        if self.subdiv == "NL"
                        # Canada Day.
                        else tr("Canada Day")
                    )
                )
            )

        super()._add_subdiv_holidays()

    def _add_subdiv_ab_holidays(self):
        if self._year >= 1990:
            self._add_family_day()

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        # https://en.wikipedia.org/wiki/Civic_Holiday#Alberta
        if self._year >= 1974:
            # Heritage Day.
            self._add_holiday_1st_mon_of_aug(tr("Heritage Day"))

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _add_subdiv_bc_holidays(self):
        if self._year >= 2013:
            name = tr("Family Day")
            if self._year >= 2019:
                self._add_holiday_3rd_mon_of_feb(name)
            else:
                self._add_holiday_2nd_mon_of_feb(name)

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        # https://en.wikipedia.org/wiki/Civic_Holiday#British_Columbia
        if self._year >= 1974:
            # British Columbia Day.
            self._add_holiday_1st_mon_of_aug(tr("British Columbia Day"))

        self._add_queens_funeral()

        if self._year >= 2023:
            # National Day for Truth and Reconciliation.
            self._add_holiday_sep_30(tr("National Day for Truth and Reconciliation"))

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _add_subdiv_mb_holidays(self):
        if self._year >= 2008:
            # Louis Riel Day.
            self._add_holiday_3rd_mon_of_feb(tr("Louis Riel Day"))

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 1900:
            name = (
                # Terry Fox Day.
                tr("Terry Fox Day")
                if self._year >= 2015
                # Civic Holiday.
                else tr("Civic Holiday")
            )
            self._add_holiday_1st_mon_of_aug(name)

        if self._year >= 2021:
            # National Day for Truth and Reconciliation.
            self._add_holiday_sep_30(tr("National Day for Truth and Reconciliation"))

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _add_subdiv_nb_holidays(self):
        if self._year >= 2018:
            self._add_family_day()

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        # https://en.wikipedia.org/wiki/Civic_Holiday#New_Brunswick
        if self._year >= 1900:
            # New Brunswick Day.
            self._add_holiday_1st_mon_of_aug(tr("New Brunswick Day"))

        self._add_queens_funeral()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _add_subdiv_nl_holidays(self):
        if self._year >= 1900:
            # St. Patrick's Day.
            self._add_holiday(tr("St. Patrick's Day"), self._get_nearest_monday(MAR, 17))

        if self._year >= 1990:
            # Nearest Monday to April 23
            # 4/26 is the Monday closer to 4/23 in 2010
            # but the holiday was observed on 4/19? Crazy Newfies!
            dt = date(2010, APR, 19) if self._year == 2010 else self._get_nearest_monday(APR, 23)
            # St. George's Day.
            self._add_holiday(tr("St. George's Day"), dt)

        if self._year >= 1997:
            # Discovery Day.
            self._add_holiday(tr("Discovery Day"), self._get_nearest_monday(JUN, 24))

        self._add_queens_funeral()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(
                self._add_remembrance_day(tr("Remembrance Day")), rule=SUN_TO_NEXT_MON
            )

    def _add_subdiv_ns_holidays(self):
        # http://novascotia.ca/lae/employmentrights/NovaScotiaHeritageDay.asp
        if self._year >= 2015:
            # Heritage Day.
            self._add_holiday_3rd_mon_of_feb(tr("Heritage Day"))

        self._add_queens_funeral()

        if self._year >= 2021:
            # National Day for Truth and Reconciliation.
            self._add_holiday_sep_30(tr("National Day for Truth and Reconciliation"))

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(
                self._add_remembrance_day(tr("Remembrance Day")), rule=SUN_TO_NEXT_MON
            )

    def _add_subdiv_nt_holidays(self):
        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 1996:
            # National Aboriginal Day.
            self._add_holiday_jun_21(tr("National Aboriginal Day"))

        if self._year >= 1900:
            # Civic Holiday.
            self._add_holiday_1st_mon_of_aug(tr("Civic Holiday"))

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(
                self._add_remembrance_day(tr("Remembrance Day")), rule=SUN_TO_NEXT_MON
            )

    def _add_subdiv_nu_holidays(self):
        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 2000:
            dt = (APR, 1) if self._year == 2000 else (JUL, 9)
            # Nunavut Day.
            self._add_observed(self._add_holiday(tr("Nunavut Day"), dt), rule=SUN_TO_NEXT_MON)

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _add_subdiv_on_holidays(self):
        if self._year >= 2008:
            self._add_family_day()

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 1900:
            # Civic Holiday.
            self._add_holiday_1st_mon_of_aug(tr("Civic Holiday"))

        self._add_thanksgiving()

    def _add_subdiv_pe_holidays(self):
        if self._year >= 2009:
            # Islander Day.
            name = tr("Islander Day")
            if self._year >= 2010:
                self._add_holiday_3rd_mon_of_feb(name)
            else:
                self._add_holiday_2nd_mon_of_feb(name)

        self._add_queens_funeral()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(
                self._add_remembrance_day(tr("Remembrance Day")), rule=SUN_TO_NEXT_MON
            )

    def _add_subdiv_qc_holidays(self):
        if self._year >= 2003:
            # National Patriots' Day.
            self._add_holiday_1st_mon_before_may_24(tr("National Patriots' Day"))

        if self._year >= 1925:
            self._add_observed(
                # St. Jean Baptiste Day.
                self._add_saint_johns_day(tr("St. Jean Baptiste Day")),
                rule=SUN_TO_NEXT_MON,
            )

        self._add_thanksgiving()

    def _add_subdiv_sk_holidays(self):
        if self._year >= 2007:
            self._add_family_day()

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        # https://en.wikipedia.org/wiki/Civic_Holiday#Saskatchewan
        if self._year >= 1900:
            # Saskatchewan Day.
            self._add_holiday_1st_mon_of_aug(tr("Saskatchewan Day"))

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(
                self._add_remembrance_day(tr("Remembrance Day")), rule=SUN_TO_NEXT_MON
            )

    def _add_subdiv_yt_holidays(self):
        # start date?
        # https://www.britannica.com/topic/Heritage-Day-Canadian-holiday
        # Heritage Day was created in 1973
        # by the Heritage Canada Foundation
        # therefore, start date is not earlier than 1974
        # http://heritageyukon.ca/programs/heritage-day
        # https://en.wikipedia.org/wiki/Family_Day_(Canada)#Yukon_Heritage_Day
        # Friday before the last Sunday in February
        if self._year >= 1974:
            self._add_holiday_2_days_prior_last_sun_of_feb(tr("Heritage Day"))

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 1912:
            # Discovery Day.
            self._add_holiday_3rd_mon_of_aug(tr("Discovery Day"))

        self._add_queens_funeral()

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))


class CA(Canada):
    pass


class CAN(Canada):
    pass
