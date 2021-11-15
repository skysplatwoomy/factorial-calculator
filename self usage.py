#set 'n' variable before call

def factorial(n):
    #preperation
    answer = 1
    
    #calculation
    for x in range(1, n+1):
      answer = x*answer
    
    #to be used through returning, if you want an answer add
    #factorialanswer = factorial(n)
    return answer
  
#now run whenever
