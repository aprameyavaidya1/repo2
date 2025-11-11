try:
  num=int(input("Enter your age:"))
  if num>=18:
    print("you are eligible")
  else:
    print("you are not eligible")

except ValueError:
  print("Please enter a valid integer for age.")
