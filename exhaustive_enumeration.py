def run():
    objetive = int(input("Put an integer: "))
    result = 0

    while result ** 2 < objetive:
        result += 1
    if result**2 == objetive:
        print(f'{result} is the square root of {objetive}')
    else:
        print(f"{objetive} has'nt a integer square root")
        
if __name__ == '__main__':
    run()