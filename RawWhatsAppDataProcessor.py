# ==============================================================================
# RawWhatsAppDataProcessor.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from datetime import datetime
import re

from TextMessage import TextMessage


# ------------------------------------------------------------------------------
# Class
# ------------------------------------------------------------------------------

class RawWhatsAppDataProcessor(object):
    """
    Contains methods for processing raw WhatsApp data files.
    """

    def __init__(self):
        """
        Creates a processor that can deal with multiple raw data files.
        """
        pass


    def get_messages(self, file_name):
        """
        Processes a raw data file and returns a list of messages it contains.

        Arguments:
            file_name<string> -- File to process.

        Returns:
            List of TextMessage objects: [TextMessage, ...].
        """
        if file_name == None or file_name == '':
            raise Exception('Empty file name provided: %s' % file_name)

        result = []
        data_file = None

        try:
            data_file = open(file_name)
        except IOError:
            print 'Unable to open file: %s' % file_name
            return result

        for line in data_file:
            date, time, sender, body = self.extract_fields(line)
            year, month, day = self.breakup_date(date)
            hour, minute, second = self.breakup_time(time)

            timestamp = datetime(year, month, day, hour, minute, second)

            message = TextMessage(sender, timestamp, body)
            result.append(message)

        return result


    def extract_fields(self, text):
        """
        Find the date, time, sender, and body of a message from the raw data of
        a single text.

        Arguments:
            text<string> -- Raw data of text.

        Returns:
            Tuple containing the date, time, sender, and body of the text, like
            so: (date<string>, time<string>, sender<string>, body<string>).
        """
        date_re = '(?P<date>[0-9]{1,2}/[0-9]{1,2}/[0-9]{4})'
        time_re = '(?P<time>[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2})'
        sender_re = '(?P<sender>[0-9a-zA-Z ]+)'
        body_re = '(?P<body>.+)'
        full_re = '%s %s: %s: %s' % (date_re, time_re, sender_re, body_re)

        matches = re.search(full_re, text)

        date = matches.group('date')
        time = matches.group('time')
        sender = matches.group('sender')
        body = matches.group('body')

        return (date, time, sender, body)


    def breakup_date(self, date):
        """
        Find the year, month, and day from the date string.

        Arguments:
            date<string> -- Date string of format mm/dd/YYYY.

        Returns:
            Year, month, and day in a tuple, like so:
            (year<int>, month<int>, day<int>).
        """
        year_re = '(?P<year>[0-9]{4})'
        month_re = '(?P<month>[0-9]{1,2})'
        day_re = '(?P<day>[0-9]{1,2})'
        full_re = '%s/%s/%s' % (month_re, day_re, year_re)

        matches = re.search(full_re, date)

        year = int(matches.group('year'))
        month = int(matches.group('month'))
        day = int(matches.group('day'))

        return (year, month, day)


    def breakup_time(self, time):
        """
        Find the hour, minute, and second from the time string.

        Arguments:
            time<string> -- Time string of format hh:mm:ss.

        Returns:
            Hour, minute, and second in a tuple, like so:
            (hour<int>, minute<int>, second<int>).
        """
        hour_re = '(?P<hour>[0-9]{1,2})'
        minute_re = '(?P<minute>[0-9]{1,2})'
        second_re = '(?P<second>[0-9]{1,2})'
        full_re = '%s:%s:%s' % (hour_re, minute_re, second_re)

        matches = re.search(full_re, time)

        hour = int(matches.group('hour'))
        minute = int(matches.group('minute'))
        second = int(matches.group('second'))

        return (hour, minute, second)
