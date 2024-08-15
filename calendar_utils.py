from datetime import datetime
import pytz
from icalendar import Calendar, Event
from icalendar.prop import vRecur

def create_calendar(events, timezone):
    cal = Calendar()
    tz = pytz.timezone(timezone)

    for event in events:
        event_start_date = datetime.strptime(event["start_date"], "%Y-%m-%d")
        start = tz.localize(datetime.combine(event_start_date, datetime.strptime(event["start"], "%H:%M").time()))
        end = tz.localize(datetime.combine(event_start_date, datetime.strptime(event["end"], "%H:%M").time()))

        cal_event = Event()
        cal_event.add('summary', event["summary"])
        cal_event.add('dtstart', start)
        cal_event.add('dtend', end)
        cal_event.add('dtstamp', datetime.now(tz))

        if "description" in event:
            cal_event.add('description', event["description"])
        if "location" in event:
            cal_event.add('location', event["location"])
        if "uid" in event:
            cal_event.add('uid', event["uid"])
        if "status" in event:
            cal_event.add('status', event["status"])
        if "sequence" in event:
            cal_event.add('sequence', event["sequence"])
        if "frequency" in event and "byday" in event and "recurrence" in event:
            rrule = {
                'FREQ': event['frequency'],
                'COUNT': event['recurrence'],
                'BYDAY': event['byday']
            }
            cal_event.add('rrule', rrule)
        if "attendees" in event:
            for attendee in event["attendees"]:
                cal_event.add('attendee', attendee)
        if "organizer" in event:
            cal_event.add('organizer', event["organizer"])
        if "priority" in event:
            cal_event.add('priority', event["priority"])
        if "categories" in event:
            cal_event.add('categories', ",".join(event["categories"]))
        if "color_id" in event:
            cal_event.add('X-GOOGLE-CALENDAR-COLOR-ID', event["color_id"])
        if "hangout_link" in event:
            cal_event.add('X-GOOGLE-HANGOUT-LINK', event["hangout_link"])
        if "geo" in event:
            cal_event.add('geo', event["geo"])
        if "transp" in event:
            cal_event.add('transp', event["transp"])
        if "class" in event:
            cal_event.add('class', event["class"])
        if "attach" in event:
            cal_event.add('attach', event["attach"])

        cal.add_component(cal_event)

    return cal

def save_calendar(calendar, filename):
    with open(filename, 'wb') as f:
        f.write(calendar.to_ical())