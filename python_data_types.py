"""
Python Data Types Tutorial
Author: Aowlad Bin Afrid
Description: This file explains basic Python data types with examples.
"""

# 1. Integer (int)
age = 25
print("Age:", age)
print("Type of age:", type(age))

# 2. Float (float)
height = 5.8
print("\nHeight:", height)
print("Type of height:", type(height))

# 3. String (str)
name = "Aowlad Bin Afrid"
print("\nName:", name)
print("Type of name:", type(name))

# 4. Boolean (bool)
is_student = True
print("\nIs Student:", is_student)
print("Type of is_student:", type(is_student))

# 5. List
fruits = ["Apple", "Banana", "Mango"]
print("\nFruits:", fruits)
print("Type of fruits:", type(fruits))

# 6. Tuple
coordinates = (10, 20)
print("\nCoordinates:", coordinates)
print("Type of coordinates:", type(coordinates))

# 7. Set
unique_numbers = {1, 2, 3, 3, 4}
print("\nUnique Numbers:", unique_numbers)
print("Type of unique_numbers:", type(unique_numbers))

# 8. Dictionary
student = {
    "name": "Aowlad",
    "age": 22,
    "country": "Bangladesh"
}
print("\nStudent Info:", student)
print("Type of student:", type(student))

# 9. None Type
result = None
print("\nResult:", result)
print("Type of result:", type(result))


"""
Basic Data Types Used in Data Analysis
Note: These are the most common data types used in data analysis.
"""

# 1. Number (int, float)
age = 25
salary = 30500.50

# 2. Text (string)
name = "Aowlad"
city = "Dhaka"

# 3. Yes / No (boolean)
is_student = True
is_paid = False

# 4. List (multiple values)
scores = [80, 85, 90, 88]

# 5. Dictionary (row type data)
person = {
    "name": "Aowlad",
    "age": 22,
    "country": "Bangladesh"
}

# 6. Date (time related data)
import pandas as pd
join_date = pd.to_datetime("2026-01-01")

# 7. Table Data (DataFrame) – most important
data = {
    "Name": ["Aowlad", "Rahim", "Karim"],
    "Age": [22, 25, 23],
    "Score": [88, 92, 79]
}

df = pd.DataFrame(data)

# 8. Missing Data
import numpy as np
missing_value = np.nan

print("Data Analysis Basic Data Types Loaded Successfully")