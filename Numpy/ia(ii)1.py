import csv

# Sample data to write to the CSV file
data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
    ["Bob", 28, "Chicago"],
]

# Specify the CSV file's name and open it in write mode
file_name = "sample.csv"

# Open the file and create a CSV writer
with open(file_name, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the data to the CSV file
    for row in data:
        csv_writer.writerow(row)

print(f"Data has been written to {file_name}")

# Open the file and create a CSV reader
with open(file_name, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Loop through each row in the CSV file and print its contents
    for row in csv_reader:
        print(row)

