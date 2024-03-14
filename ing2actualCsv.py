import argparse
import os
import pandas as pd


def find_header_row(input_file):
    with open(input_file, 'r', encoding='iso-8859-1') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "Buchung;Valuta;Auftraggeber" in line:
                return i
    return 0  # If header not found, assume it's the first row


def main(input_file, start_date):
    # Define desired columns to keep (modify as needed)

    try:
        # print("Current working directory:", os.getcwd())

        # Find the index where the header information ends
        skip_rows = find_header_row(input_file)

        # Read the CSV data with ISO 8859-1 encoding, skipping header rows
        data = pd.read_csv(input_file, sep=";", decimal=",",
                           encoding='iso-8859-1', skiprows=skip_rows)

        # Convert 'Buchung' column to datetime
        data['Buchung'] = pd.to_datetime(data['Buchung'], format='%d.%m.%Y')

        # Filter rows based on start date
        data = data[data['Buchung'] >= start_date]

        # Select desired columns
        columns_to_keep = [
            'Buchung',
            'Auftraggeber/Empfänger',
            'Verwendungszweck',
            'Betrag'
        ]
        data = data[columns_to_keep]

        # Write the modified table to a new CSV file
        output_file = input_file.rsplit('.', 1)[0] + '_modified.csv'
        data.to_csv(output_file, index=False)

        print(f"Modified table has been written to '{output_file}'")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process CSV file and extract specified columns")
    parser.add_argument("input_file", help="Path to input CSV file")
    parser.add_argument(
        "start_date", help="Starting date (format: YYYY-MM-DD)")
    args = parser.parse_args()

    try:
        start_date = pd.to_datetime(args.start_date)
    except ValueError:
        print("Error: Invalid date format. Please use format: YYYY-MM-DD")
    else:
        main(args.input_file, start_date)
