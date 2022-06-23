'''Exercise 1: Write a program to read through a file and print the contents
of the file (line by line) all in upper case. Executing the program will
look as follows:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
You can download the file from www.py4e.com/code3/mbox-short.txt'''

fhand = open("mbox-short.txt")
for lines in fhand:
    lines = lines.rstrip().upper()
    print(lines)

'''Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence values from these lines. 
When you reach the end of the file, print out
the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519'''

prompt = input("Enter file name:")
try:
    fhand = open(prompt)
except:
    print("Sorry this file doesn't exist, try again.")
    exit()
count = 0
total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        number = line[line.find(":"):len(line)]
        float_number = float(number[1:])
        total += float_number

average = total / count
print("Average spam confidence:", average)



