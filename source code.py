#whole stand-alone calculator
import sys
def calc():
  def loop():
    retry = input("Do you want to exit? Type 'Y' or 'N'. ").upper()
    if retry == "N":
      print("Retrying...")
      calc()
    elif retry == "Y":
      sys.exit(0)
    else:
      print("Invalid option.")
      loop()
  def factorial(n):
    answer = 1
    for x in range(1, n+1):
      answer = x*answer
    return answer
  try:
    n = int(input("factorial calculator: "))
  except:
    print("Error found")
    loop()
  print(f"{n} factorial = {factorial(n)}")
  loop()
calc()
