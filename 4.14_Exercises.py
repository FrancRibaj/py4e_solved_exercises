
'''
4.14 Exercises
Exercise 4: What is the purpose of the “def” keyword in Python?
a) It is slang that means “the following code is really cool”
b) It indicates the start of a function
c) It indicates that the following indented section of code is to be stored for later
d) b and c are both true (ANSWER)
e) None of the above
'''
'''
Exercise 5: What will the following Python program print out?
def fred():
print("Zap")
def jane():
print("ABC")
jane()
fred()
jane()
a) Zap ABC jane fred jane
b) Zap ABC Zap
c) ABC Zap jane
d) ABC Zap ABC (ANSWER)
e) Zap Zap Zap
'''
'''
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0#
'''

hours, rate = input("Enter hours and rate:").split()

def computepay(x, y):
   pay = ((float(x)- 40) * (float(y) * 1.5)) + (40 * float(y))
   print(pay)
   return pay

computepay(hours, rate)

'''
Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input.
'''



def computegrade(x):
        if x > 1 : 
            print("Bad score")
        elif x >= 0.9:
            print("A")
        elif x >= 0.8:
            print("B")
        elif x >= 0.7:
            print("C")
        elif x < 0.6:
            print("F")

try: 
    score = float(input('Enter score:'))
    computegrade(score)
except:
    print("Bad score.")




    






