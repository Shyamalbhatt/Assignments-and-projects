def fact_r(num):
    if num < 0:
        print('Factorial does not exist')
    elif num == 0:
        print('The Factorial of 0 is 1')
    else:
        if num == 1:
            return num
        else:
            return num * fact_r(num-1) 

print(fact_r(5))