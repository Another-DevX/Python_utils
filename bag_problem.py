
def solve_problem(values, weights, bag,n):
    if bag == 0 or n == 0:
        return 0
    elif weights[n-1] > bag:
        return solve_problem(values, weights, bag, n - 1)
    return max(values[n-1] + solve_problem(values, weights, bag - weights[n-1], n-1),
            solve_problem(values, weights,bag, n-1))



def run():
    values = [60,100,200]
    weights = [10,20,30]
    bag_capacity = 50
    n = len(values)
    print(solve_problem(values,weights,bag_capacity, n))

if __name__ == '__main__':

    run()