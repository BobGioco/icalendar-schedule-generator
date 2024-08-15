# iCalendar Schedule Generator

This repository contains a Python script to generate a weekly learning schedule in iCalendar (.ics) format. The schedule includes a variety of fictional events to serve as an example.

## Usage

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

You also need to install the required packages. You can do this using `pip`:

```sh
```

### Running the Script

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/yourusername/icalendar-schedule-generator.git
    cd icalendar-schedule-generator
    ```

2. Run the script:

    ```sh
    python generate_schedule.py
    ```

This will generate an iCalendar file named `Learning_Schedule.ics` in the current directory.

### Project Structure

- `generate_schedule.py`: Main script to generate the schedule.
- `calendar_utils.py`: Contains functions related to calendar creation and saving.
- `events.py`: Defines the events list.
- `config.py`: Contains configuration settings like start date, number of weeks, and timezone.
- `README.md`: This file, providing an overview and usage instructions for the project.

### Customizing the Schedule

You can customize the events and the schedule by editing the `events.py` and `config.py` files.

#### Configurations (`config.py`)

- `START_DATE`: The start date of the schedule in `YYYY-MM-DD` format.
- `WEEKS`: The number of weeks to generate the schedule for.
- `TIMEZONE`: The timezone for the events.

Example `config.py`:
```python
START_DATE = "2024-08-19"  # Starting from a specific Monday
WEEKS = 4
TIMEZONE = "America/New_York"
```

#### Events (`events.py`)

Modify the events list to include the details of each event, including the summary, start time, end time, start date, end date, frequency, byday, and recurrence.

Example `events.py`:
```python
events = [
    {
        "summary": "Project Meeting",
        "description": "Discuss project milestones and deliverables.",
        "location": "Conference Room A",
        "start": "10:00",
        "end": "11:00",
        "start_date": "2024-08-19",
        "end_date": "2024-10-07",
        "uid": "uid1@example.com",
        "status": "CONFIRMED",
        "sequence": 0,
        "frequency": "WEEKLY",
        "byday": ["MO", "WE"],
        "recurrence": 8,
        "attendees": ["mailto:johndoe@example.com"],
        "organizer": "mailto:jane.doe@example.com",
        "priority": 5,
        "categories": ["Meeting", "Work"],
        "color_id": "9",
        "hangout_link": "https://hangouts.google.com/call/abcdefg",
        "geo": "37.386013;-122.082932",
        "transp": "OPAQUE",
        "class": "PUBLIC",
        "attach": "http://example.com/agenda.pdf"
    },
    {
        "summary": "Morning Yoga",
        "description": "Daily morning yoga session.",
        "location": "Gym",
        "start": "07:00",
        "end": "08:00",
        "start_date": "2024-08-20",
        "end_date": "2024-10-09",
        "uid": "uid2@example.com",
        "status": "CONFIRMED",
        "sequence": 0,
        "frequency": "WEEKLY",
        "byday": ["TU", "TH", "SA"],
        "recurrence": 8,
        "attendees": ["mailto:janedoe@example.com"],
        "organizer": "mailto:johndoe@example.com",
        "priority": 3,
        "categories": ["Exercise", "Health"],
        "color_id": "5",
        "hangout_link": "https://hangouts.google.com/call/hijklmn",
        "geo": "40.712776;-74.005974",
        "transp": "OPAQUE",
        "class": "PUBLIC",
        "attach": "http://example.com/yoga.pdf"
    },
    # Add more events as needed
]
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README file provides a comprehensive overview of the project, instructions for usage, and details on how to customize the schedule.