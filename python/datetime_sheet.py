# Python DateTime Cheat Sheet

# IMPORT DATETIME MODULE
import datetime

# CURRENT DATE AND TIME
now = datetime.datetime.now()

# DATE
today = datetime.date.today()
specific_date = datetime.date(2023, 11, 24)  # Year, Month, Day

# TIME
specific_time = datetime.time(12, 30, 45)  # Hour, Minute, Second

# DATETIME
specific_datetime = datetime.datetime(
    2023, 11, 24, 12, 30, 45
)  # Year, Month, Day, Hour, Minute, Second

# TIMESTAMP
timestamp_now = datetime.datetime.timestamp(now)

# CONVERT TIMESTAMP TO DATETIME
datetime_from_timestamp = datetime.datetime.fromtimestamp(timestamp_now)

# FORMATTING DATE AND TIME
formatted_date = today.strftime("%Y-%m-%d")
formatted_time = specific_time.strftime("%H:%M:%S")
formatted_datetime = specific_datetime.strftime("%Y-%m-%d %H:%M:%S")

# PARSE STRING TO DATETIME
parsed_datetime = datetime.datetime.strptime("2023-11-24 12:30", "%Y-%m-%d %H:%M")

# TIME DELTA (FOR DATE ARITHMETICS)
one_day = datetime.timedelta(days=1)
one_week = datetime.timedelta(weeks=1)
one_hour = datetime.timedelta(hours=1)

# DATE ARITHMETIC
tomorrow = today + one_day
last_week = today - one_week

# COMPARING DATES AND TIMES
is_today_before_tomorrow = today < tomorrow
is_now_after_past = now > datetime.datetime(2023, 1, 1)

# TIMEZONE HANDLING
from datetime import timezone

utc_time = datetime.datetime.now(timezone.utc)
local_time = utc_time.astimezone()

# REPLACE METHOD
new_date = today.replace(year=2024, month=1)

# EXTRACTING INDIVIDUAL COMPONENTS
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

# WORKING WITH WEEKDAYS
# Monday is 0 and Sunday is 6
weekday = today.weekday()

# TIPS
# - Always handle dates and times in UTC and convert to local timezones when necessary.
# - Be cautious with daylight saving time changes.
# - Use `pytz` or `zoneinfo` for more comprehensive timezone support.
# - For detailed formatting, refer to strftime() and strptime() format codes.
