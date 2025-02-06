"""
Write a Python program that:

Accepts a list of numbers from the user (comma-separated input).
Attempts to convert the input to a list of integers.
Then, for each number, attempts to calculate the reciprocal (1 divided by the number).
Handle the following exceptions:
ValueError: If the user enters anything other than numbers.
ZeroDivisionError: If any number is zero (since reciprocal of 0 is undefined).
IndexError: If the list is empty or the user doesn't provide any input.
The program should:

Print the reciprocal of each number if there are no errors.
Print appropriate error messages for each exception, including handling all exceptions gracefully.
If the list is empty, display a message saying "No numbers entered."
"""

def reciprocal(s):
    try:
        if not s:
            print("List is empty")
        for i in s:
            print(1/i)
    except ZeroDivisionError as e2:
        print("Error: Zero don't have any reciprocal")
    except TypeError as e3:
        print("Error:Enter integers")
    finally:
        print("done")

lst=[11,24,'ddsf',45]
reciprocal(lst)

        

