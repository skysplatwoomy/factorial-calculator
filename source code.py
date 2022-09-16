def factorial(n):
    answer = 1
    for x in range(1, n+1):
        answer = x*answer
    return answer
try:
    n = int(input("factorial calculator: "))
except ValueError:
    print("word!, me too")
    from sys import exit
    input("press enter to exit ")
    exit(0)
print(f"{n} factorial = {factorial(n)}")
input("press enter to exit ")
