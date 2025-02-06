import numberchecker as nc
num=int(input("enter the number:"))
if nc.isPrime(num):
    print("The number is a prime number")
else:
    print("The number is not a prime number")
if nc.isPalindrome(num):
    print("The number is a Palindrome number")
else:
    print("The number is not a Palindrome number")
