def loopfactorial(n):
  factorial = 1
  for i in range(1 , n + 1): #Tem que ter o n+1 por que o range NAO INCLUI o numero que passa p ele
    factorial *= i
  return factorial


print (loopfactorial(5))