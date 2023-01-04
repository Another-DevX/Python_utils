def run():  
    value = int(input("Put your number"))
    epsilon = 0.001
    lower_value = 0.0
    higher_value = max(1.0, value)
    result = (higher_value + lower_value) / 2

    while abs(result**2 - value) >= epsilon:
        print(f'Low {lower_value} High{higher_value} Partial_result{result}')
        
        if result ** 2 < value:
            lower_value = result
        else:
            higher_value = result
        result = (higher_value+lower_value)/2

    print(f'The square root of {value} is around {result}')


if __name__ ==  '__main__':
    run()