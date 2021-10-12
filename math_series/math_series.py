def fibonacci(n): 
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
def lucas_numbers(n):
    if n==0:
        return 2
    if n==1:
        return 1
    return lucas_numbers(n-1)+lucas_numbers(n-2)
def sum_series(n, num1=0, num2=1):
     if num1 ==0 and num2==1:
        return fibonacci(n)
     if not num1 ==0 or num2==1:
        return lucas_numbers(n)