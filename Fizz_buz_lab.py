#creating the function fizz_buzz as indicated in the question and assigning it  a parameter n
def fizz_buzz(n):

    if n % 3 == 0 and n % 5 == 0: #if n(number) is divisible by 3 and 5 it should return 'Fizzbuzz'
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n #if all the above conditions are not met, the number it self should be returned

