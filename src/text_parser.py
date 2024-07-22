import re
from datetime import datetime

def parse_ticket_data(text):
    ticket_data = {}

    # Extract UTS number
    uts_no_match = re.search(r'UTS No:\s*(\w+)', text)
    if uts_no_match:
        ticket_data['uts_no'] = uts_no_match.group(1)
    else:
        ticket_data['uts_no'] = None

    # # Extract date (assuming format is DD-MM-YYYY)
    # date_match = re.search(r'\b(\d{2}-\d{2}-\d{4})\b', text)
    # if date_match:
    #     date_str = date_match.group(1)
    #     try:
    #         ticket_data['date'] = datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
    #     except ValueError:
    #         ticket_data['date'] = None

    # # Extract time (assuming 24-hour format HH:MM)
    # time_match = re.search(r'\b(\d{2}:\d{2})\b', text)
    # if time_match:
    #     ticket_data['time'] = time_match.group(1)

    # # Extract station (assuming it's always preceded by "Station: ")
    # station_match = re.search(r'Station:\s*(.+)', text)
    # if station_match:
    #     ticket_data['station'] = station_match.group(1).strip()

    # # Extract class (assuming it's either "First" or "Second")
    # class_match = re.search(r'\b(First|Second)\s+Class\b', text, re.IGNORECASE)
    # if class_match:
    #     ticket_data['class'] = class_match.group(1).lower()

    # # If any required field is missing, set it to None
    # for field in ['uts_no', 'date', 'time', 'station', 'class']:
    #     if field not in ticket_data:
    #         ticket_data[field] = None

    return ticket_data

