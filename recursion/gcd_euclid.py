# def f(n): 
#     if n<=1: 
#         return 1 
#     if n%2==0: 
#         return f(n//2) 
#     return f(n//2) + f(n//2+1) 
# print(f(11)) 

def function(n):
    if n>0: 
        return (n+function(n-2)) 
    else:
        return 0 
print(function(10))