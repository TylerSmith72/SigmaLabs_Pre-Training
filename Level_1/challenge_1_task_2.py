allowedNames = ['Alice','Bob']

name = input("What is your name? ")

if(name in allowedNames):
  print("Hello " + name + "!")
else:
  print("Sorry... You're not authorised to be greeted!")
