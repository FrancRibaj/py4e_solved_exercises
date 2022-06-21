'''
Exercise 1: Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
'''
total = 0
counter = 0

try:
    while True:
        number = input("Enter a number:")
        if number == 'done':
            break
        else:
           total += int(number)
           counter+= 1
           aver = total/counter
    print(total,counter,aver)
except:
    print("Invalid input.")

# '''Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.'''


# largest, smallest = None, None

# while True:
#     prompt = input("Write numbers")
#     if prompt == 'done':
#         break
#     else:
#         try:
#             if largest is None or largest < prompt:
#                 largest = prompt
#             if smallest is None or smallest > prompt:
#                 smallest = prompt
#         except:
#             print("Invalid input.")
# print("largest, smallest = ",largest,smallest)



















