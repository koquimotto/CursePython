# -----------Fibonacci basic level-----------------------
# def Fibonacci(n):
#     if n<0:
#         print('Incorrect input')
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# print(Fibonacci(10))
# -----------------------------------------------


# -----------Fibonacci nivel intermedio----------
# FibArray = [0,1]

# def fibonnacci(n):
#     if n<0:
#         print ('Incorrect input')
#     elif n<=len(FibArray):
#         return FibArray[n-1]
#     else:
#         temp_fib = fibonnacci(n-1) + fibonnacci(n-2)
#         FibArray.append(temp_fib)
#         return temp_fib

# print(fibonnacci(120))
# ---------------------------------------------------

# -----------------------Fibonacci hard level--------
def Fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a, b = b, a + b
n=100000
print(list(Fibonacci(n)) [n-1]) 
# ---------------------------------------------------