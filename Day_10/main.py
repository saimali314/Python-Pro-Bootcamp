def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    """Hi"""
    if year%4 == 0 and year%100 !=0 or year%400 ==0:
        return True
    else:
        return False

print(is_leap_year(int(input("Enter the year you want to check: "))))

