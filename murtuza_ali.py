# 1.Check if a number is positive or negative.

num=int(input("enter a number : "))

if num>=0:
    print("Number is Positive")
else:
    print("Number is negavtive")

# 2.Determine if a number is even or odd.

num=int(input("enter a number : "))

if num%2==0:
    print("number is even")
else:
    print("number is odd")

# 3.Check if a year is a leap year.

num=int(input("enter a year : "))

if num%4==0:
    print(num," is a leap year")
else:
    print(num,"is not leap year")

# 5.Compare two numbers and find the greater.

num1=int(input("enter first number : "))
num2=int(input("enter second number : "))

if num1>num2:
    print(num1," is a greater number")
elif num2>num1:
    print(num2,"is a greater number")

# 6.Check if a character is a vowel or consonant.
 
char = input("Enter a character: ")
for i in char:
    if i in 'aeiou':
        print(i,"is a vowel")
    else:
        print(i,"is a Consonant")

# 7.Determine if a number is divisible by 5 and 11.
 
num=int(input("enter a number : "))

if num%5==0 and num%11==0:
    print(num,"is divisible by 5 and 11")
else:
    print(num,"is not divisible by 5 and 11")

# 8. Check if a number is a multiple of both 3 and 7.
 
num=int(input("enter a number : "))

if num%3==0 and num%7==0:
    print(num,"is a multiple of both 3 and 7")
else:
    print(num,"is not a multiple of both 3 and 7")

# 9. Determine if a character is uppercase or lowercase.
 
char = input("Enter a character: ")

if char.isupper():
    print(char,"is a uppercase")
elif char.islower():
    print(char,"is a lowercase")


# 10. Check if a number is a perfect square.
 
num=int(input("enter a number : "))

if num>=0:
    i=0
    while i*i<=num:
        if i*i==num:
            print("is a perfect square")
            break
        i+=1
    else:
        print("is not a perfect square")
else:
    print("Negative numbers cannot be perfect squares.")
    
# 11. Determine if a number is a palindrome.
 
num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is NOT a palindrome.")

# 12. Check if a number is an Armstrong number.
 
num = int(input("Enter a number: "))

original = num
power = len(str(num))
total = 0
temp = num
while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is NOT an Armstrong number.")

# 13. Determine if a number is prime.
 
num = int(input("Enter a number: "))

if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"enter number greater than 1")

# 14. Check if a triangle is valid with given sides.

a = int(input("Enter first side of a triangle: "))
b = int(input("Enter second side of a triangle: "))
c = int(input("Enter third side of a triangle: "))


if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
            print(a,b,c,"triangle is valid with given sides")
    else:
        print(a,b,c,"the given sides of triangle is not valid ")
else:
    print("enter number greater than 0")

# 15. Determine the type of triangle (equilateral, isosceles, scalene).

a = int(input("Enter first side of a triangle: "))
b = int(input("Enter second side of a triangle: "))
c = int(input("Enter third side of a triangle: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print(a, b, c, "triangle is valid with given sides")
        if a == b == c:
            print("Equilateral triangle")
        elif a == b or b == c or a == c:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
    else:
        print(a, b, c, "the given sides of triangle is not valid")
else:
    print("enter number greater than 0")

# 16. Check if a character is an alphabet or not.

ch = input("Enter a character: ")

if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print(ch, "is an alphabet")
else:
    print(ch, "is NOT an alphabet")


# 17. Determine the grade based on percentage marks.

marks = float(input("Enter percentage marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
elif marks >= 60 and marks < 70:
    print("Grade: D")
elif marks >= 40 and marks < 60:
    print("Grade: E")
elif marks >= 0 and marks < 40:
    print("Grade: F")
else:
    print("Invalid marks entered")


# 18. Check if a person is eligible to vote.

age = int(input("Enter age: "))

if age >= 18:
    print("Person is eligible to vote")
else:
    print("Person is NOT eligible to vote")


# 19. Check if a person is eligible for driving license.

age = int(input("Enter age: "))

if age >= 18:
    print("Person is eligible for driving license")
else:
    print("Person is NOT eligible for driving license")


# 20. Determine the quadrant of a point in 2D plane.

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("Point lies in 1st Quadrant")
elif x < 0 and y > 0:
    print("Point lies in 2nd Quadrant")
elif x < 0 and y < 0:
    print("Point lies in 3rd Quadrant")
elif x > 0 and y < 0:
    print("Point lies in 4th Quadrant")
elif x == 0 and y != 0:
    print("Point lies on Y axis")
elif y == 0 and x != 0:
    print("Point lies on X axis")
else:
    print("Point is at the origin")


# 21. Check if a given year is a century year.

year = int(input("Enter year: "))

if year % 100 == 0:
    print(year, "is a century year")
else:
    print(year, "is NOT a century year")


# 22. Determine if the temperature is hot, cold, or moderate.

temp = float(input("Enter temperature in Celsius: "))

if temp >= 30:
    print("It's hot")
elif temp >= 15 and temp < 30:
    print("It's moderate")
else:
    print("It's cold")


# 23. Find the absolute value of a number.

num = float(input("Enter a number: "))

if num < 0:
    num = -num

print("Absolute value is", num)

# 24. Check if a person is tall, average, or short based on height.

height = float(input("Enter height in cm: "))

if height >= 180:
    print("Person is tall")
elif height >= 150:
    print("Person is average")
else:
    print("Person is short")


# 25. Compare three numbers and find the smallest.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <= b and a <= c:
    print(a, "is the smallest number")
elif b <= a and b <= c:
    print(b, "is the smallest number")
else:
    print(c, "is the smallest number")


# 26. Check if a number is within a specific range.

num = float(input("Enter a number: "))
low = float(input("Enter lower bound: "))
high = float(input("Enter upper bound: "))

if num >= low and num <= high:
    print(num, "is within the range", low, "to", high)
else:
    print(num, "is NOT within the range", low, "to", high)


# 27. Check if a day number (1-7) is a weekday or weekend.

day = int(input("Enter day number (1-7): "))

if day >= 1 and day <= 5:
    print("Weekday")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Invalid day number")


# 28. Check if a number is a single digit, two-digit, or more.

num = int(input("Enter a number: "))
num = abs(num)

if num < 10:
    print("Single digit number")
elif num < 100:
    print("Two-digit number")
else:
    print("Number has more than two digits")


# 29. Determine the electricity bill based on usage.

units = float(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Electricity bill is:", bill)


# 30. Check if a password is strong based on simple rules.

password = input("Enter password: ")

if (len(password) >= 8 and
    any(c.islower() for c in password) and
    any(c.isupper() for c in password) and
    any(c.isdigit() for c in password)):
    print("Password is strong")
else:
    print("Password is weak")


# 31. Determine if a year is a leap year using nested if.

year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is NOT a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is NOT a leap year")


# 32. Check if a number is even and divisible by 4.

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 4 == 0:
    print(num, "is even and divisible by 4")
else:
    print(num, "is NOT even and divisible by 4")


# 33. Determine if a student passed or failed.

marks = float(input("Enter marks out of 100: "))

if marks >= 40:
    print("Student passed")
else:
    print("Student failed")


# 34. Check if a number ends with a specific digit.

num = int(input("Enter a number: "))
digit = input("Enter a digit to check: ")

if str(num).endswith(digit):
    print(num, "ends with", digit)
else:
    print(num, "does NOT end with", digit)


# 35. Determine if a month number has 30 or 31 days.

month = int(input("Enter month number (1-12): "))

if month in [4, 6, 9, 11]:
    print("Month has 30 days")
elif month == 2:
    print("Month has 28 or 29 days")
elif 1 <= month <= 12:
    print("Month has 31 days")
else:
    print("Invalid month number")


# 36. Compare strings and check if they are equal.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 == str2:
    print("Strings are equal")
else:
    print("Strings are NOT equal")


# 37. Check if a string is empty or not.

s = input("Enter a string: ")

if s == "":
    print("String is empty")
else:
    print("String is NOT empty")


# 38. Determine if a character is a digit or not.

ch = input("Enter a character: ")

if ch.isdigit():
    print(ch, "is a digit")
else:
    print(ch, "is NOT a digit")


# 39. Check if the sum of two numbers is even or odd.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

total = a + b

if total % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")


# 40. Determine if the input is an integer or not.

inp = input("Enter something: ")

if inp.lstrip('-').isdigit():
    print("Input is an integer")
else:
    print("Input is NOT an integer")


# 41. Compare the lengths of two strings.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) > len(s2):
    print("First string is longer")
elif len(s1) < len(s2):
    print("Second string is longer")
else:
    print("Both strings are of equal length")


# 42. Check if the first and last digit of a number are the same.

num = input("Enter a number: ")

if num[0] == num[-1]:
    print("First and last digit are the same")
else:
    print("First and last digit are NOT the same")


# 43. Determine if a number is a Fibonacci number.

num = int(input("Enter a number: "))

def is_perfect_square(x):
    return int(x**0.5)**2 == x

if is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4):
    print(num, "is a Fibonacci number")
else:
    print(num, "is NOT a Fibonacci number")


# 44. Check if the given time is AM or PM.

hour = int(input("Enter hour (0-23): "))

if 0 <= hour < 12:
    print("AM")
elif 12 <= hour <= 23:
    print("PM")
else:
    print("Invalid hour")


# 45. Determine the season from the month number.

month = int(input("Enter month number (1-12): "))

if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month number")


# 46. Check if a given angle is acute, right, or obtuse.

angle = float(input("Enter angle in degrees: "))

if angle > 0 and angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
elif angle > 90 and angle < 180:
    print("Obtuse angle")
else:
    print("Invalid angle")


# 47. Determine if a number is a power of 2.

num = int(input("Enter a number: "))

if num > 0 and (num & (num - 1)) == 0:
    print(num, "is a power of 2")
else:
    print(num, "is NOT a power of 2")


# 48. Check if a character is a special symbol.

ch = input("Enter a character: ")

if not (ch.isalnum() or ch.isspace()):
    print(ch, "is a special symbol")
else:
    print(ch, "is NOT a special symbol")


# 49. Determine eligibility for a scholarship based on marks and income.

marks = float(input("Enter marks out of 100: "))
income = float(input("Enter family income: "))

if marks >= 85 and income < 500000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")


# 50. Check if sum of any two numbers is greater than the third.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a + b > c or a + c > b or b + c > a:
    print("Sum of any two numbers is greater than the third")
else:
    print("Sum of any two numbers is NOT greater than the third")

