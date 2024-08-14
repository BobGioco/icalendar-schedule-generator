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

Modify the `events` list to include the details of each event, including the summary, start time, end time, and the day of the week.

Example `events.py`:
```python
events = [
    {"summary": "Morning Yoga", "start": "07:00", "end": "08:00", "day": 0},
    {"summary": "Project Planning Meeting", "start": "10:00", "end": "11:00", "day": 0},
    {"summary": "Lunch Break", "start": "12:00", "end": "13:00", "day": 0},
    {"summary": "JavaScript Basics", "start": "14:00", "end": "16:00", "day": 0},
    {"summary": "Evening Jog", "start": "18:00", "end": "19:00", "day": 0},
    {"summary": "Cooking Class", "start": "19:30", "end": "21:00", "day": 0},
    # ... Add more events as needed
]
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README file provides a comprehensive overview of the project, instructions for usage, and details on how to customize the schedule.