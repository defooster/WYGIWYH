import datetime

from django.forms import widgets
from django.utils import formats, translation, dates
from django.utils.formats import get_format

from apps.common.utils.django import (
    django_to_python_datetime,
    django_to_airdatepicker_datetime,
    django_to_airdatepicker_datetime_separated,
)


class AirDatePickerInput(widgets.DateInput):
    def __init__(
        self,
        attrs=None,
        format=None,
        clear_button=True,
        auto_close=True,
        user=None,
        *args,
        **kwargs,
    ):
        attrs = attrs or {}
        self.user = user
        super().__init__(attrs=attrs, format=format, *args, **kwargs)
        self.clear_button = clear_button
        self.auto_close = auto_close

    @staticmethod
    def _get_current_language():
        """Get current language code in format compatible with AirDatepicker"""
        lang_code = translation.get_language()
        # AirDatepicker uses simple language codes
        return lang_code.split("-")[0]

    def _get_format(self):
        """Get the format string based on user settings or default"""
        if self.format:
            return self.format

        if self.user and hasattr(self.user, "settings"):
            user_format = self.user.settings.date_format
            print(user_format)
            if user_format == "SHORT_DATE_FORMAT":
                return get_format("SHORT_DATE_FORMAT", use_l10n=True)
            return user_format

        return get_format("SHORT_DATE_FORMAT", use_l10n=True)

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs)

        attrs["data-auto-close"] = str(self.auto_close).lower()
        attrs["data-clear-button"] = str(self.clear_button).lower()
        attrs["data-language"] = self._get_current_language()
        attrs["data-date-format"] = django_to_airdatepicker_datetime(self._get_format())

        return attrs

    def format_value(self, value):
        """Format the value for display in the widget."""
        if value:
            self.attrs["data-value"] = value

        if value is None:
            return ""
        if isinstance(value, (datetime.date, datetime.datetime)):
            return formats.date_format(value, format=self._get_format(), use_l10n=True)

        return str(value)

    def value_from_datadict(self, data, files, name):
        """Parse the datetime string from the form data."""
        value = super().value_from_datadict(data, files, name)
        if value:
            try:
                # This does it's best to convert Django's PHP-Style date format to a datetime format and reformat the
                # value to be read by Django. Probably could be improved
                return datetime.datetime.strptime(
                    value.strip(),
                    django_to_python_datetime(self._get_format())
                    or django_to_python_datetime(get_format("SHORT_DATETIME_FORMAT")),
                ).strftime("%Y-%m-%d")
            except (ValueError, TypeError) as e:
                return value
        return None


class AirDateTimePickerInput(widgets.DateTimeInput):
    def __init__(
        self,
        attrs=None,
        format=None,
        timepicker=True,
        clear_button=True,
        auto_close=True,
        user=None,
        *args,
        **kwargs,
    ):
        attrs = attrs or {}
        self.user = user
        super().__init__(attrs=attrs, format=format, *args, **kwargs)
        self.timepicker = timepicker
        self.clear_button = clear_button
        self.auto_close = auto_close

    @staticmethod
    def _get_current_language():
        """Get current language code in format compatible with AirDatepicker"""
        lang_code = translation.get_language()
        # AirDatepicker uses simple language codes
        return lang_code.split("-")[0]

    def _get_format(self):
        """Get the format string based on user settings or default"""
        if self.format:
            return self.format

        if self.user and hasattr(self.user, "settings"):
            user_format = self.user.settings.datetime_format
            if user_format == "SHORT_DATETIME_FORMAT":
                return get_format("SHORT_DATETIME_FORMAT", use_l10n=True)
            return user_format

        return get_format("SHORT_DATETIME_FORMAT", use_l10n=True)

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs)

        date_format, time_format = django_to_airdatepicker_datetime_separated(
            self._get_format()
        )

        # Add data attributes for AirDatepicker configuration
        attrs["data-timepicker"] = str(self.timepicker).lower()
        attrs["data-auto-close"] = str(self.auto_close).lower()
        attrs["data-clear-button"] = str(self.clear_button).lower()
        attrs["data-language"] = self._get_current_language()
        attrs["data-date-format"] = date_format
        attrs["data-time-format"] = time_format

        return attrs

    def format_value(self, value):
        """Format the value for display in the widget."""
        if value:
            self.attrs["data-value"] = datetime.datetime.strftime(
                value, "%Y-%m-%d %H:%M:00"
            )

        if value is None:
            return ""
        if isinstance(value, (datetime.date, datetime.datetime)):
            return formats.date_format(value, format=self._get_format(), use_l10n=True)

        return str(value)

    def value_from_datadict(self, data, files, name):
        """Parse the datetime string from the form data."""
        value = super().value_from_datadict(data, files, name)
        if value:
            try:
                # This does it's best to convert Django's PHP-Style date format to a datetime format and reformat the
                # value to be read by Django. Probably could be improved
                return datetime.datetime.strptime(
                    value.strip(),
                    django_to_python_datetime(self._get_format())
                    or django_to_python_datetime(get_format("SHORT_DATETIME_FORMAT")),
                ).strftime("%Y-%m-%d %H:%M:%S")
            except (ValueError, TypeError) as e:
                return value
        return None


class AirMonthYearPickerInput(AirDatePickerInput):
    def __init__(self, attrs=None, format=None, *args, **kwargs):
        super().__init__(attrs=attrs, format=format, *args, **kwargs)
        # Store the display format for AirDatepicker
        self.display_format = "MMMM yyyy"
        # Store the Python format for internal use
        self.python_format = "%B %Y"

    @staticmethod
    def _get_month_names():
        """Get month names using Django's date translation"""
        return {dates.MONTHS[i]: i for i in range(1, 13)}

    def format_value(self, value):
        """Format the value for display in the widget."""
        if value:
            self.attrs["data-value"] = (
                value  # We use this to dynamically select the initial date on AirDatePicker
            )

        if value is None:
            return ""
        if isinstance(value, str):
            try:
                value = datetime.datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                return value
        if isinstance(value, (datetime.datetime, datetime.date)):
            # Use Django's date translation
            month_name = dates.MONTHS[value.month]
            return f"{month_name} {value.year}"
        return value

    def value_from_datadict(self, data, files, name):
        """Convert the value from the widget format back to a format Django can handle."""
        value = super().value_from_datadict(data, files, name)
        if value:
            try:
                # Split the value into month name and year
                month_str, year_str = value.rsplit(" ", 1)
                year = int(year_str)

                # Get month number from translated month name
                month_names = self._get_month_names()
                month = month_names.get(month_str)

                if month and year:
                    # Return the first day of the month in Django's expected format
                    return datetime.date(year, month, 1).strftime("%Y-%m-%d")
            except (ValueError, KeyError):
                return None
        return None
