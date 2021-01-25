def FibRecursion(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibRecursion(n-1) + FibRecursion(n-2))  
terms = int(input("Enter the terms? ")) 
  
if terms <= 0:  
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(terms):  
       print(FibRecursion(i))
