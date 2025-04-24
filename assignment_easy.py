# 1. Calculator:

# Create a function that takes two numbers and an operator (+, -, *, /) as input and returns the result.
# Example Input: numbers = 5, 3, operator = "*"
# Example Output: 15

def calculator(num1, num2, operator):
  if operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  elif operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  else:
    return "Invalid operator"
  
result = calculator(5, 3, "*")
print("Calculator Result: {}".format(result))


# 2. Temperature Converter:

# Write a program to convert temperatures between Celsius and Fahrenheit.
# Example Input: temperature = 25, unit = "Celsius"
# Example Output: 77.0 Fahrenheit

def temperature_converter(temp, unit):
  if unit == "Celsius":
    return f"{(temp * 9/5) + 32} Fahrenheit"
  elif unit == "Fahrenheit":
    return f"{(temp - 32) * 5/9} Celsius"
  else:
    return "Invalid unit"
  
temperature = 25
unit = "Celsius"
result = temperature_converter(temperature, unit)
print("Temperature Converter Result: {}".format(result))



# 3. Vowel Counter:

# Create a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
# Example Input: string = "Hello, world!"
# Example Output: 3

def count_vowels(val):
  vowels = "aeiou"
  vowels = vowels + vowels.upper()
  count = 0
  for char in val:
    if char in vowels:
      count += 1
  return count

result = count_vowels("HellO, world!")
print("Vowel Counter Result: {}".format(result))

'''
4. List Operations:
  * Write functions to perform operations on lists:
    * Calculate the sum, average, and maximum value of a list of numbers.
    * Reverse the elements of a list.

  * Example Input 1: numbers = [1, 5, 3, 8, 2]
  * Example Output 1:
    * Sum: 19
    * Average: 3.8
    * Maximum: 8
  * Example Input 2: my_list = ['a', 'b', 'c']
  * Example Output 2: ['c', 'b', 'a']
'''

numbers = [1, 5, 3, 8, 2]
my_list = ['a', 'b', 'c']

numbers_sum = sum(numbers)
numbers_average = numbers_sum / len(numbers)
numbers_max = max(numbers)

print("List Operations Result:")
print("Sum: {}".format(numbers_sum))
print("Average: {}".format(numbers_average))
print("Maximum: {}".format(numbers_max))

print("Reversed List: {}".format(my_list[::-1]))
# OR
my_list.reverse()
print("Reversed List (option 2): {}".format(my_list))

