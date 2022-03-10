import math

def say_math(math_func, number):
  
  result = math_func(number)
  print("The results of " +    str(math_func) + " applied to "  + str(number) + " is " + str(result))


say_math(math.sqrt, 9)