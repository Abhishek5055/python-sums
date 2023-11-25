try:
    # Attempt to open and read from the "in.txt" file
    with open("in.txt", "r") as file_input:
        # Attempt to open and write to the "out.txt" file
        with open("out.txt", "w") as file_output:
            # Read the contents of "in.txt" line by line
            for line in file_input:
                # Convert the line to uppercase and write it to "out.txt"
                file_output.write(line.upper())
    
    print("Contents from 'in.txt' have been written to 'out.txt' in uppercase.")

except FileNotFoundError:
    print("Error: 'in.txt' not found.")

except PermissionError:
    print("Error: Permission denied while writing 'out.txt'.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
