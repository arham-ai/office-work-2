#as the size grows the time will also grow
#time=a*n+b
def get_squared_numbers(number):
    squared_numbers=[]
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers = [2,5,8,9]
get_squared_numbers(numbers)