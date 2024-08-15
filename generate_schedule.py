from datetime import datetime
from calendar_utils import create_calendar, save_calendar
from events import events
import config

if __name__ == "__main__":
    timezone = config.TIMEZONE

    calendar = create_calendar(events, timezone)
    save_calendar(calendar, 'Generated_Schedule.ics')