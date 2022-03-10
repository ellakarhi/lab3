import math 

def print_division_info(num1, num2):
  #x divided by y is n remainder m
  div = math.floor(num1/num2)
  rem = num1 % num2
  print (str(num1) + " divided by " +   str(num2) + " is " + str(div) + " remainder " + str(rem))

  #attempting to print the value of  the remainder variable outside of   body of the function causes an     error because the computer reads the fuction and won't take into account the remainder variable because it is global and not locally within the function.
  #This causes a runtime error.

print_division_info(4, 3)

