import csv
import convertor


ft_or_m = input("Enter 'ft' for feet, enter 'm' for meters ")
users_choice = input("Enter 'C' for Celsius, enter 'F' for Fahrenheit ")
converted_rows = []
def main(input_file, output_file):
    with open(input_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skipping the header row

        for row in reader:
            date, distance, reading = row
            _distance = convertor.distance.convert_dist(distance, ft_or_m)
            converted_reading = convertor.temperature.convert_temp(reading.strip(), users_choice)
            converted_rows.append([date,_distance, converted_reading])

    with open(output_file,mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Converted distance', 'Converted Reading'])
        writer.writerows(converted_rows)

if __name__ == "__main__":
    input_file = "example.csv"
    output_file = "outcome.csv"


    main(input_file, output_file)