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
  print("\nUnique Plates:\n")
  for plate in unique_plates:
    print(plate + ": " + str(plates.count(plate)))

def count_students(file):
  with open(file, "r", newline="") as data:
    reader_object = reader(data)
    responses = []
    # Put all responses into a list to be counted
    for row in reader_object:
      responses.append(row[2])
    students = responses.count("y")
    staff = responses.count("n")
    nopass = responses.count("")
    
    print()
    print("Students: " + str(students), "Staff: " + str(staff), "No Pass: " + str(nopass), sep="\n")

def count_ampm(file):
  with open(file, "r", newline="") as data:
    reader_object = reader(data)
    responses = []
    am = 0
    pm = 0
    allday = 0
    for row in reader_object:
      responses.append((row[3],row[4]))
    for i in responses:
      if i[0] == "y" and i[1] == "y":
        allday += 1
      elif i[0] == "y" and i[1] == "n":
        am += 1
      elif i[0] == "n" and i[1] == "y":
        pm += 1
    print()
    print("All Day: " + str(allday), "AM only: " + str(am), "PM only:" + str(pm), sep="\n")