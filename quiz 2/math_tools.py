def check_even_odd(number):
    """Check if a number is even or odd.
    """
    input_number = int(number)
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
def calc_sum(numbers):
    """Calculate the sum of a list of numbers.
    """
    total = 0
    for num in numbers:
        total += num
    return total
def analyze_sum(numbers):
    """Analyze the sum of a list of numbers to determine if it's even or odd.
    """
    total_sum = calc_sum(numbers)
    return check_even_odd(total_sum)

print("Sum of 5 and 3 is ", calc_sum([5,3]),  ", and the sum is", analyze_sum([5, 3]),".")  