"""
Reader
-------
This is a space for functions
that manipulate data from csv
files to display statistics of
parking violations.
"""

from csv import reader
from pprint import pp

def count_plates(file):
  with open(file, "r") as f:
    data = reader(f)
    unique_plates = {}
    # For all the plates in the data sheet, if they
    # are not in the dictionary, add them with a
    # value of 1.  If they are in the dictionary,
    # increment the value by 1.
    for row in data:
      if row[1] not in unique_plates and row[1] != "license plate" and row[1] != "":
        unique_plates[row[1]] = 1
      elif row[1] in unique_plates:
        unique_plates[row[1]] += 1
  pp(unique_plates)

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