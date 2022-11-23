#program determine if a given year is a common or a leap year or doesn't fall within the Gregorian calender
# As you surely know, due to some astronomical reasons, years may be leap or common. 
# The former are 366 days long, while the latter are 365 days long.

# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.


year = int(input("Enter a year: "))

# Write your code here.
if year < 1582:
    print ("Not within the Gregorian calender period.")
elif (year%4) != 0 | (year%400) != 0:
    print ("Common year")
elif (year%100) != 0:
    print ("Leap year")
else:
    print ("Leap year")