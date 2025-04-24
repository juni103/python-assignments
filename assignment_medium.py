'''
1. Fibonacci Sequence:

Write a function to generate the first n numbers of the Fibonacci sequence.
Example Input: n = 8
Example Output: [0, 1, 1, 2, 3, 5, 8, 13]
'''

def fibonacci_sequence(n):
    if n <= 0:
        return []

    if n <= 2:
        return [i for i in range(n)]

    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    return fib_sequence

result = fibonacci_sequence(8)
print("Fibonacci Sequence:", result)


'''
2. Word Frequency:

Create a program that reads a text file and counts the frequency of each word.
Example Input: Text file containing "This is a test. This is only a test."
Example Output: {'This': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
'''

def word_frequency(file_path):
    word_count = {}
    
    with open(file_path, 'r') as file:
      content = file.read()
      words = content.split(' ')

      for word in words:
          if word in word_count:
              word_count[word] += 1
          else:
              word_count[word] = 1
    
    return word_count

word_count = word_frequency('word_frequency_text.txt')
print("Word Frequency:", word_count)


'''
3. Data Validation:

Write a function to validate user input for different data types (e.g., integer, float, email address).
Example Input 1: value = "5", data_type = "integer"
Example Output 1: True
Example Input 2: value = "[email address removed]", data_type = "email"
Example Output 2: True
'''
import re

email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def validate_input(value, data_type):
  if data_type == "integer":
      return value.isdigit()
  elif data_type == "float":
      try:
          float(value)
          return True
      except ValueError:
          return False
  elif data_type == "email":
      return re.match(email_regex, value) is not None
  else:
      return False

data_type = "integer"
result = validate_input("5", data_type.lower())
print("Is valid {}: {}".format(data_type, result))


'''
4. File Handling:

Read a CSV file containing student data and calculate average grades.
Create a text-based address book.
Example Input 1: CSV file with student data
Example Output 1: Prints average grade for each student
Example Input 2: (user interaction)
Add contact: Name: "Alice", Phone: "555-1212"
Search: "Alice"
Example Output 2: Prints Alice's contact information
'''
import csv

score_headers = ['math_score', 'history_score', 'physics_score', 'chemistry_score', 'biology_score', 'english_score', 'geography_score']

def print_avg_grades(file_path):
    with open(file_path, 'r') as file:
      reader = csv.DictReader(file, delimiter=',')

      if not reader.fieldnames:
          print("No students found in the file.")
      else:
          for student in reader:
              total_grades = 0
              for header in score_headers:
                  total_grades += int(student[header])
              average_grade = total_grades / len(score_headers)
              student_name = student['first_name'] + ' ' + student['last_name']
              print(f"Student: {student_name.strip()}, Average Grade: {average_grade:.2f}")

print_avg_grades('student-scores.csv')

