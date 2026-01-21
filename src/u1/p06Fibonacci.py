#Python code for fibonacci Series
def fibonacci(n):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
   n = 0
   print("Number is ", n)
   print("Fibonacci series upto number ",n, "are: ")
   for i in range(n):
      print(fibonacci(i) , end = " ")

