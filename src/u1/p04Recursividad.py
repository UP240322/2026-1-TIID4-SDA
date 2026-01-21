# Factorial recursive function implementation

def factorial(n): # sin recursividad
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorialR(n):
    if n <= 1:  # base case
        return 1
    else:
        return n * factorialR(n - 1)

def contadorDescendente(n):
    for i in range(n, -1, -1):
        print(i)
    print("Booom")

def contadorDescendenteR(n):
    if n < 0:
        print("Booom")
    else:
        contadorDescendenteR(n-1)
        print(n)


    '''
    public static int factor(int limit) {
        int number = 5, result = 0;
        for (int i = 0; i < limit; i++) {
            result += number;
        }
        return result;
    }
    '''
    # metodo que indique que hay un return indicando en el def 
def factor(n) -> int:   
    number = 5
    result = 0
    for i in range(n):
        result += number
    return result


# Example usage
if __name__ == "__main__":
    '''
    number = 4
    print(f"The factorial of {number} is {factorial(number)}")
    r = factorialR(number)
    print(f"The factorialR of {number} is {r}")

    print ("Contador Descendente:")
    '''
    #contadorDescendenteR(5)
    number = 4
    r = factorialR(number)
    print (f"Factor method result: {r}")
    contadorDescendenteR(number)
