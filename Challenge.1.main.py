#1.program for factorial number
"""
formula = n(n-1)!
ex:1! = 1*1
"""
def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)
    
number= int(input("ENTER A VALUE:"))
result= fact_rec(number)

print("The Factorial of {} is {}.".format(number,result))
