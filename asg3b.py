#check if leap year using ternary operator
year=int(input("Enter year:"))
print(f"The year {year} is a leap year") if (year%400==0 or (year%100!=0 and year%4==0)) else print(f"The year {year} is not a leap year")
