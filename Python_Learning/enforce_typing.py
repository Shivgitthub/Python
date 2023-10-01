def assum_factorial(x:int)->int:
     
    """
    Description: 
    Function for finding factorial for given number

    Parameter:
    1. x:int
    The number is to find factorial value

    Result: int
    Function returns factorial value for given number   
    """

    if x < 0:
        return None
    elif x == 0 or x == 1:
        return 1
    else:
        return x * assum_factorial(x-1)  
    
test_cases = [0,1,2,3,4,5,2.3]

for case in test_cases:
    print(assum_factorial(case))
        
        