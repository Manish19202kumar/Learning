# exp 10
# import pandas as pd
# import numpy as np
# import plotly.express as px

# data = {
#     'A': [1, 2, 3, 4, 5],
#     'B': [2, 3, 4, 5, 6],
#     'C': [3, 4, 5, 6, 7],
#     'D': [4, 5, 6, 7, 8],
#     'E': [5, 6, 7, 8, 9],
# }
# df = pd.DataFrame(data)
# corr_matrix = df.corr()

# fig = px.imshow(corr_matrix, x=corr_matrix.columns, y=corr_matrix.columns)
# fig.update_layout(title="Correlation Heatmap")
# fig.show()
  
# #  exp 8a

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range (n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# input_list = [7,3,2,5,9,6,4]
# print("Unsorted list", input_list)
# bubble_sort(input_list)
# print("sorted list: ", input_list)


# ----------------------------------------------EXP 8(B)------------------------------------------------------------------------- 

# input_list = [5,6,75,3,6,7,35,7,5,3,4,5,3,8,9,0,7,9,6,5,4,7,9,0]
# element_frequency ={}

# for element in input_list:
#     if element in element_frequency:
#         element_frequency[element] += 1
#     else:
#         element_frequency[element] = 1

# for element, frequency in element_frequency.items():
#     print(f"element {element} occurs {frequency} times")


# Exp 3

# user_details = {}

# user_id = input ("Enter usr id : ")
# user_name = input ("Enter user name: ")
# user_age = input("Enter User Age: ")

# user_details[user_id] = {"Name": user_name, "Age": user_age}

# search_id = input ("Enter ID to retrive details: ")

# if search_id in user_details: 
#     details = user_details[search_id]
#     print(f"User ID: {search_id}")
#     print(f"Name: {details['Name']}")
#     print(f"Age: {details['Age']}")
# else:
#     print("User ID not found.")

# -------------------------------------------------------------------EXP 9----------------------------------------------- 

# import tkinter as tk
# import time
# import threading
# root = tk.Tk()
# root.title("Process Control")  # Corrected the spelling of 'title'

# running = False  # Initialize the 'running' variable

# def start_process():
#     global running
#     if not running:
#         running = True
#         thread = threading.Thread(target=simulate_process)
#         thread.start()  # Corrected the method name to 'start'

# def stop_process():
#     global running
#     running = False

# def simulate_process():
#     while running:
#         print("Process is running...")
#         time.sleep(1)

# start_button = tk.Button(root, text="Start Process", command=start_process)  # Corrected syntax
# stop_button = tk.Button(root, text="Stop Process", command=stop_process)  # Corrected syntax

# start_button.pack()
# stop_button.pack()

# root.mainloop()


# --------------------------------------------------------EXP 7-------------------------------------------------------------

# import math

# def compute_gcd(a, b):
#     return math.gcd(a, b)

# def compute_lcm(a, b):
#     return a * b // math.gcd(a, b)  # Corrected the LCM calculation

# num1 = int(input("Enter the value of First INT: "))
# num2 = int(input("Enter the second value: "))

# gcd = compute_gcd(num1, num2)
# lcm = compute_lcm(num1, num2)  # Used the corrected compute_lcm function

# print(f"GCD of {num1} and {num2} is {gcd}")
# print(f"LCM of {num1} and {num2} is {lcm}")

# def is_cubical_number(num):
#     num_str = str(num)
#     digit_cubed_sum = sum(int(digit) ** 3 for digit in num_str)  # Corrected the syntax
#     return num == digit_cubed_sum

# smallest_cubical = None
# largest_cubical = None

# for num in range(100, 1001):
#     if is_cubical_number(num):
#         if smallest_cubical is None:  # Corrected the comparison
#             smallest_cubical = num
#         largest_cubical = num
# if smallest_cubical is not None:
#     print(f"Smallest cubical number in the range 100 to 1000: {smallest_cubical}")
# else:
#     print("No cubical number found in the range 100 to 1000")


# -------------------------------------------------------------EXP 6--------------------------------------------------

# import matplotlib.pyplot as plt

# Employe = ['EmpA', 'EmpB', 'EmpC', 'EmpD']
# values = [15, 30, 10, 25]
# plt.bar(Employe,values)

# plt.xlabel('Employe')
# plt.ylabel('values')
# plt.title('Simple bar graph')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Pie Chart
# labels = ['LabelA', 'LabelB', 'LabelC', 'LabelD']  # Corrected the spelling of 'LabelC'
# sizes = [20, 30, 10, 40]  # Corrected the list name 'Sizes'
# plt.pie(sizes, labels=labels, autopct='%1.1f%%')  # Corrected the syntax
# plt.title('Pie Chart')
# plt.show()
# # Line Plot
# x = np.linspace(-5, 5, 100)
# y = x**2
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('y = x^2')
# plt.show()
# ---------------------------------------------------------------Exp 5---------------------------------------------------------------

# import numpy as np

# # Fixing the array initialization
# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# def swap_columns(arr, col1, col2):
#     arr[:, [col1, col2]] = arr[:, [col2, col1]]  # Corrected the order of columns

# swap_columns(data, 0, 2)
# print(data)

# # Fixing the array initialization and data type definition
# data_type = [('number', float), ('text', 'U10')]  # Corrected the data type for 'text'
# data = np.array([(1.2, 'First'), (3.4, 'Second'), (5.6, 'Third')], dtype=data_type)  # Corrected the syntax
# print(data)

# number = data['number']
# texts = data['text']

# print("Number: ", number)
# print("Texts: ",texts)
      
# ------------------------------------------------Exp 2-------------------------------------------------------------------------

# def sum_of_divisors (n):
#     divisors = [1] # start with 1 as a divisor 
#     for i in range(2, int(n**0.5) + 1): 
#         if n % i == 0: 
#             divisors.extend([i, n // i]) 
#     return sum(set(divisors)) # Use a set to eliminate duplicates

# def find_amicable_numbers (start, end):
#     amicable_pairs = [] 
#     for num in range(start, end + 1): 
#         partner = sum_of_divisors (num) 
#         if num != partner and sum_of_divisors (partner) == num:
#             amicable_pairs.append((num, partner))
#     return amicable_pairs

# start_range= int(input("Enter the starting range: ")) 
# end_range= int(input("Enter the ending range: "))

# amicable_numbers = find_amicable_numbers (start_range, end_range)

# if amicable_numbers: print("Amicable Pairs: ") 
# for pair in amicable_numbers: print (pair[0], "-", pair[1])

# else: print("No amicable numbers found in the specified range.")


# --------------------------------------------------------EXP 1(B)-------------------------------------------------------------

# def Factorial (num):
#     if num == 1:
#         return 1
#     else:
#         return num * Factorial (num-1)

# def permutation (n, r): 
#     return int (Factorial (n) / Factorial(n-r))

# def combination (n,r): 
#     return int (Factorial (n) / Factorial (r) * Factorial(n-r))

# print (" Permutation: ", permutation(15,4))
# print ("Combination: ", combination(15,4))

# def is_prime(num):
#     if num < 2:
#         return False

#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True  # Moved outside the loop

# def find_twin_primes(max_num):
#     for first_num in range(2, max_num):
#         second_num = first_num + 2
#         if is_prime(first_num) and is_prime(second_num):
#             print("{0} and {1} are Twin Prime Members".format(first_num, second_num))  # Corrected the formatting

# find_twin_primes(1000)

#  exp 3
# user_details = {}

# # Get user information
# user_id = input("Enter user ID: ")
# user_name = input("Enter user name: ")
# user_age = input("Enter user age: ")

# # Store user information in the dictionary
# user_details[user_id] = {"Name": user_name, "Age": user_age}

# # Get details based on entered ID
# search_id = input("Enter ID to retrieve details: ")

# # Check if the entered ID exists in the dictionary
# if search_id in user_details:
#     details = user_details[search_id]
#     print(f"User {search_id}ID: ",{'jjhd'})
#     print(f"Name: {details['Name']}")
#     print(f"Age: {details['Age']}")
# else:
#     print("User ID not found.")


# exp 4

class Student:
    def _init_(self, rollno, name, class_name):
        self.rollno = rollno
        self.name = name
        self.class_name = class_name

    def display(self):
        print(f"Roll No: {self.rollno}")
        print(f"Name: {self.name}")
        print(f"Class: {self.class_name}")


student_list = []

def add_student():
    rollno = input("Enter Roll No: ")
    name = input("Enter Name: ")
    class_name = input("Enter Class: ")

    student = Student(rollno, name, class_name)
    student_list.append(student)
    print("Student added successfully!")


def display_students():
    if not student_list:
        print("No students found.")
    else:
        print("\nList of Students:")
        for student in student_list:
            student.display()
            print()


while True:
    print("\n===== Student Information System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")