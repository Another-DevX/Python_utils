def run():
    objetive = int(input("Put an integer: "))
    epsilon = 0.01
    step = epsilon ** 2
    result = 0.0
    
    #Take care about epsilon, python is not very optimized for this kind of process.
    
    while abs(result **2 - objetive) >= epsilon and result <= objetive:
        result += step
    print(f'{result} is the aproximated square root of {objetive}')


if __name__ == '__main__':
    run()