'''
Exercise 2: Write a program that uses input to prompt a user for their
name and then welcomes them.
'''
name = input("Type your name:")
print("Hello" + name )

'''
Exercise 3: Write a program to prompt the user for hours and rate per
hour to compute gross pay.
'''

hours = input("Enter hours:")
rate = input("ENTER rate:")

gross = int(hours) * float(rate) 
print("Pay:" + str(gross))

'''
Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
converted temperature.
'''

temp_celsius = input("Temperature in Celsius:")
temp_fahrenheit = (float(temp_celsius) * 9/5) + 32 
print("Temperature in Fahrenheit:" + str(temp_fahrenheit))
