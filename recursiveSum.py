# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 23:42:10 2018

@author: SIDHARTH
"""

def recursiveSum(n):
    if n== 0:
        return 0
    else:
        return recursiveSum(n-1) + n
        
def main():
    x = int(input("Please enter a non-negetive integer: "))
    s = recursiveSum(x)
    print("The sum of the first",x,"integers is ", str(s)+".")
    
if __name__ == "__main__":
    main()