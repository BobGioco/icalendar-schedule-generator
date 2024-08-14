from datetime import datetime, timedelta
import pytz
from icalendar import Calendar, Event

def create_calendar(events, start_date, weeks, timezone):
    cal = Calendar()
    tz = pytz.timezone(timezone)

    for event in events:
        event_start_date = datetime.strptime(event["start_date"], "%Y-%m-%d")
        event_end_date = datetime.strptime(event["end_date"], "%Y-%m-%d")

        for day in event["days"]:
            for i in range(weeks):
                event_date = start_date + timedelta(days=day + i * 7)
                if event_start_date <= event_date <= event_end_date:
                    start = tz.localize(datetime.combine(event_date, datetime.strptime(event["start"], "%H:%M").time()))
                    end = tz.localize(datetime.combine(event_date, datetime.strptime(event["end"], "%H:%M").time()))

                    cal_event = Event()
                    cal_event.add('summary', event["summary"])
                    cal_event.add('dtstart', start)
                    cal_event.add('dtend', end)
                    cal_event.add('dtstamp', datetime.now(tz))
                    cal.add_component(cal_event)

    return cal

def save_calendar(calendar, filename):
    with open(filename, 'wb') as f:
        f.write(calendar.to_ical())