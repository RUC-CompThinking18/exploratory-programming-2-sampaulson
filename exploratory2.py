# this function counts up the number of positive numbers in a list of integers
# and returns that number

def posNumbers(numbers):
    count = 0
    # the following if/else statement will raise an error if the argument
    # is not a list of integers & tally each positive number in the list
    if type(numbers) != list:
        raise TypeError("The argument was not a list.")
    for element in numbers:
        if type(element) != int:
            raise TypeError("The list includes an element that is not type int.")
        if element > 0:
            count += 1
    return count

print posNumbers([-1,-4,6,78,0,-90])
print posNumbers("i love chris :)")
