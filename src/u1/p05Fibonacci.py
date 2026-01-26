#Python code for fibonacci Series

def fibonacci(n):
   prev2 = 0
   prev1 = 1

   if n < 0:
      print("Incorrect input")
   elif n == 0:
      return prev2
   elif n == 1:
      return prev1
   else:
      for i in range(1, n):
         fib = prev1 + prev2
         prev2 = prev1
         prev1 = fib
      return fib

def fibonacciR(n):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacciR(n-1) + fibonacciR(n-2)

if __name__ == "__main__":
   # se cuenta a partir de la posicion 0
   # pos:       0  1  2  3  4  5  6
   # fib(pos):  0  1  1  2  3  5  8
   n = 6
   
   print("Fibonacci series upto number",n, "are:")
   print("0 1 2 3 4 5 6")
   for i in range(n+1):
      print(fibonacciR(i) , end = " ")
   print()   

   print(fibonacciR(6))
   print(fibonacci(6))
