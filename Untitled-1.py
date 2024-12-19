def fac(test):
    if test < 0:
        return
    elif test == 0 or test == 1:
        return 1
    else:
        return test * fac(test - 1)

test = 5
result = fac(test)
print("The factorial of is ",result)
