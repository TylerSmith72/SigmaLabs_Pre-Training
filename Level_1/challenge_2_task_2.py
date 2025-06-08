import random
import string

def reverse_name(name):
  nameList = []
  reverse_name = ""
  
  for i in name:
    nameList.append(i)

  #print("NameList: " + str(nameList))
  
  while nameList:
    reverse_name += nameList.pop()
  
  return reverse_name

def intersperse_name(name, surname):
  interspersed = ""
  
  # Loop through the longest name
  for i in range(max(len(name), len(surname))): 
    if i < len(name):
      interspersed += name[i]
    if i < len(surname):
      interspersed += surname[i]

  return interspersed

def format_name(name, capitalize=True):
  # Split name in half
  first_half = name[:len(name)//2]
  second_half = name[len(name)//2:]

  if capitalize:
    first_half = first_half.capitalize()
    second_half = second_half.capitalize()
  else:
    first_half = first_half.lower()
    second_half = second_half.lower()

  return first_half + " " + second_half

def create_username():
  first_name = input("Enter your first name here: ")
  r_name = reverse_name(first_name)

  #print("Reversed name: " + r_name)

  surname = input("Enter your surname here: ")

  i_name = intersperse_name(r_name, surname)
  f_name = format_name(i_name)

  print("Your username is: " + f_name)

  return

def create_random_username():
  random_name = ''.join(random.choices(string.ascii_lowercase, k=10))

  f_name = format_name(random_name, False)

  print("Your random username is: " + f_name)

while(True):
  print("1. Create a username based on a name")
  print("2. Generate a random username")

  choice = input("Enter your choice here: ")

  if choice == '1':
    create_username()
    exit()
  elif choice == '2':
    create_random_username()
    exit()
  else:
    print("Invalid choice. Please try again.")