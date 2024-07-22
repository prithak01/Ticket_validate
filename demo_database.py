import psycopg2

def insert_demo_data():
    conn = psycopg2.connect(
        dbname="ticketdb",
        user="user",
        password="password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Create the tickets table with the specified columns
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        uts_no VARCHAR(15) PRIMARY KEY,
        booking_type VARCHAR(10) CHECK (booking_type IN ('journey', 'platform', 'season')),
        source_station_1 VARCHAR(100),
        source_station_2 VARCHAR(100),
        source_station_3 VARCHAR(100),
        destination_station_1 VARCHAR(100),
        destination_station_2 VARCHAR(100),
        destination_station_3 VARCHAR(100),
        via VARCHAR(100),
        adult_no INTEGER CHECK (adult_no BETWEEN 0 AND 4),
        child_no INTEGER CHECK (child_no BETWEEN 0 AND 4),
        escort_no INTEGER CHECK (escort_no BETWEEN 0 AND 4),
        ticket_type CHAR(1) CHECK (ticket_type IN ('J', 'R')),
        booking_date DATE,
        booking_time TIME,
        validity VARCHAR(23),  -- Format "dd/mm/yyyy - dd/mm/yyyy"
        train_type VARCHAR(3) CHECK (train_type IN ('O', 'M/E', 'S', 'U', 'A')),
        class CHAR(2) CHECK (class IN ('II', 'FC')),
        concession_type VARCHAR(10) CHECK (concession_type IN ('None', 'BLESC', 'BLIND', 'DFDESC', 'DFDM', 'HNDCAP', 'HNDESC', 'MENESC', 'MENTAL', 'SHNDCA', 'SMENTA'))
    );
    """)

    # Insert demo data (example)
    cursor.execute("""
    INSERT INTO tickets (uts_no, booking_type, source_station_1, source_station_2, destination_station_1, via, adult_no, child_no, escort_no, ticket_type, booking_date, booking_time, train_type, validity, class, concession_type) VALUES
    ('X079DUJ0G1', 'journey', 'PANVEL', NULL, 'BORIVALI', 'Via KOPR-BSR', 0, 1, 0, 'J', '2024-07-21', '19:32', 'M/E', NULL, 'II', 'None'),
    ('X07ADUJ0GB', 'journey', 'PANVEL', NULL, 'BORIVALI', 'Via JNJ-TUH-TNA-DR', 0, 1, 0, 'J', '2024-07-21', '18:52', NULL, 'O', 'II', 'None'),
    ('X01ODUJ1HF', 'platform', 'BORIVALI', NULL, NULL, NULL, 1, 0, 0, NULL, '2024-07-21', '19:09', NULL, NULL, NULL, 'None'),
    ('X0RNDUJ059', 'journey', 'C SHIVAJI MAH T', NULL, 'BORIVALI', 'Via VDLR-MM', 1, 0, 0, 'J', '2024-07-21', '15:28', 'O', NULL, 'II', 'None'),
    ('X07ADUJ0GB', 'season', 'C SHIVAJI MAH T', 'CHURCH GATE', 'BORIVALI', 'Via 3RT>>DDR-DR-SNRD/MM-VLDR', 1, 0, 0, 'J', '2024-07-08', '10:59', 'O', '09/07/2024 - 08/08/2024', 'FC', 'None');
    """)

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_demo_data()

