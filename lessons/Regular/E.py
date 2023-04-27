import re

input_array = input()
def calculate(str):
    str = re.findall(r'\d*\([A-Za-z\d]+\)|\d*[A-Za-z\d]+', input_array)
print(str)