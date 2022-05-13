"""
Parking Tracker
------
This program is to track the license plates of cars that park in my spot, the date each occurred, and if it lasted all day.
"""
from csv import writer
from datetime import datetime
import reader

# Use writer() object from csv library to write 
# the data to a new row in the data sheet
def write_new_row(file, new_data):
  with open(file, "a", newline="") as data:
    writer_object = writer(data)
    writer_object.writerow(new_data)

if __name__ == "__main__":

  file = "parking_data.csv"
  date = datetime.today().strftime("%m/%d/%Y")

  # Input or view data?
  user_choice = int(input("Would you like to:\n 1. Input new data\n 2. View existing data\n"))

  if user_choice == 2:
    reader.count_plates(file)
    reader.count_students(file)
    reader.count_ampm(file)

  elif user_choice == 1:
    
    # Gather input data
    license_plate = input("Input plate number: ").upper()
    student = input("Student parking tag? (leave blank if none) Y/N: ").lower()
    am = input("AM? y/n: ").lower()
    pm = input("PM? y/n: ").lower()
  
    # Collect data in a list
    new_data = [date, license_plate, student, am, pm]
  
    # Write data to csv
    write_new_row(file, new_data)
  
    # Print a count of unique plates
    reader.count_plates(file)
    reader.count_students(file)
    reader.count_ampm(file)