import csv
import requests
import sys
import homeconnectapi

def name():
  file = open("Appliance.csv", "a")
  number = input("Date: ")
  writer = csv.writer(file)
  writer.writerow((name, number))
  file.close()
  return

def yorn():
    ans = input("yes or no? ")
    if ans != "yes":
        sys.exit("re-enter") # replace with API
    else:
        return

#### is door open function
def open1():
  print("open") #replace with API
  return

def change_temp():
  answer = input("Would you like to change the Freezer temperature or the Fridge Temperature? ")
  if answer.lower() == 'freezer':
    # Change Freezer Temp
    homeconnectapi.change_freezer_temp()
  elif answer.lower() == 'fridge':
    # Change Fridge Temp
    homeconnectapi.change_fridge_temp()
  else:
    print('ok')
