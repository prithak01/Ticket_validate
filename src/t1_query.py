import psycopg2
from contextlib import closing

# Define the mapping dictionaries
train_type_mapping = {
    'O': 'Ordinary',
    'M': 'Mail/Express',
    'E': 'Mail/Express',
    'S': 'Superfast',
    'U': 'AC EMU Train',
    'A': 'Antyodaya SF'
}

class_mapping = {
    'II': 'Second Class',
    'FC': 'First Class'
}

concession_type_mapping = {
    'None': 'None',
    'BLESC': 'Blind with Escort',
    'BLIND': 'Blind Alone',
    'DFDESC': 'Deaf and Dumb with Escort',
    'DFDM': 'Deaf and Dumb',
    'HNDCAP': 'Physically Handicapped',
    'HNDESC': 'Escort for Physically Handicapped',
    'MENESC': 'Escort for Mentally Retarded',
    'MENTAL': 'Mentally Retarded',
    'SHNDCA': 'Physically Handicapped (Severe)',
    'SMENTA': 'Mentally Retarded (Severe)'
}

def fetch_ticket_details(uts_no):
    try:
        with closing(psycopg2.connect(
            dbname="ticketdb",
            user="user",
            password="password",
            host="localhost",
            port="5432"
        )) as conn:
            with conn.cursor() as cursor:
                # Fetch the ticket details
                cursor.execute("SELECT * FROM tickets WHERE uts_no = %s", (uts_no,))
                ticket = cursor.fetchone()

                if ticket:
                    # Convert the abbreviated forms to full forms
                    ticket_dict = {
                        'uts_no': ticket[0],
                        'booking_type': ticket[1],
                        'source_station_1': ticket[2],
                        'source_station_2': ticket[3],
                        'source_station_3': ticket[4],
                        'destination_station_1': ticket[5],
                        'destination_station_2': ticket[6],
                        'destination_station_3': ticket[7],
                        'via': ticket[8],
                        'adult_no': ticket[9],
                        'child_no': ticket[10],
                        'escort_no': ticket[11],
                        'ticket_type': 'Journey' if ticket[12] == 'J' else 'Return',
                        'booking_date': ticket[13],
                        'booking_time': ticket[14],
                        'validity': ticket[15],
                        'train_type': train_type_mapping.get(ticket[16], ticket[16]),
                        'class': class_mapping.get(ticket[17], ticket[17]),
                        'concession_type': concession_type_mapping.get(ticket[18], ticket[18])
                    }
                    return ticket_dict
                else:
                    return None
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return None

# Example usage
uts_no = 'X0RUDU6038'
ticket_details = fetch_ticket_details(uts_no)
if ticket_details:
    print("Ticket Details:")
    for key, value in ticket_details.items():
        print(f"{key}: {value}")
else:
    print("Ticket not found.")
