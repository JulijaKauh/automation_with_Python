#!/usr/bin/env python3
import os

def new_directory(directory, filename):
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  os.chdir(directory)
  with open (filename, "w") as file:
    pass

  return os.listdir(".")

directory = input("Enter a new directory: ")
filename = input("Enter a new file name and type: ")

print(new_directory(directory,filename))           
