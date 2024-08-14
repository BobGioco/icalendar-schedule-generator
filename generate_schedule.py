from datetime import datetime
from calendar_utils import create_calendar, save_calendar
from events import events
import config

if __name__ == "__main__":
    start_date = datetime.strptime(config.START_DATE, "%Y-%m-%d")
    weeks = config.WEEKS
    timezone = config.TIMEZONE

    calendar = create_calendar(events, start_date, weeks, timezone)
    save_calendar(calendar, 'Generated_Schedule.ics')