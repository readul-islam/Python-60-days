def sum_recursion (n):
    if(n > 0):
        return n + sum_recursion(n-1);
    else:
        return 0
    
    


print(sum_recursion(6))   