import requests
import csv
import functions

name = input("If not entering an Applaince ID leave a blank, Appliance ID: ")

if name != "":
  functions.name()

command = input("Command? ")

if command.lower() == "open":
  functions.open1()
  
elif command.lower() == "change temperature" or "change temp":
  functions.change_temp()
  
else:
  print("oops")
