"""
Reader
-------
This is a space for functions
that manipulate data from csv
files to display statistics of
parking violations.
"""

from csv import reader

def count_plates(file):
  with open(file,"r", newline="") as data:
    reader_object = reader(data)
    plates = []
    unique_plates = []
    # List all plate names from data sheet
    for row in reader_object:
      plates.append(row[1])
  # List all unique plates
  for plate in plates:
    if plate not in unique_plates and plate != "license plate" and plate != "":
      unique_plates.append(plate)
  # For each unique plate, count and print 
  # the occurrences in the data sheet
  print()
  for plate in unique_plates:
    print(plate + ": " + str(plates.count(plate)))
  data.close()

def count_students(file):
  with open(file, "r", newline="") as data:
    reader_object = reader(data)
    responses = []
    # Put all responses into a list to be counted
    for row in reader_object:
      responses.append(row[2])
    print(responses)
    students = responses.count("y")
    staff = responses.count("n")
    responses = responses.remove("student")
    print(responses)
    unknown = len(responses)
    
    print()
    print("Students: " + str(students))
    print("Staff: " + str(staff))
    print("Unknown: " + str(unknown))
  data.close()