import csv


# Function to process the CSV file
def remove_columns_except_word(input_file, output_file):
    # Open the input CSV file in read mode
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        # Read the header and skip it
        header = next(reader)

        # Ensure 'word' is the first column
        word_index = header.index('word')

        # Open the output CSV file in write mode
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # Write header with only the 'word' column
            writer.writerow([header[word_index]])

            # Write the word column for each row
            for row in reader:
                writer.writerow([row[word_index]])


# Call the function with the input and output file names
remove_columns_except_word('oxford5k.csv', 'oxford500.csv')
