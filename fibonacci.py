import functools

n = [0,1]
fibonacci = []


def accum(counter, item):
    if len(n) < 200:
        fibonacci.append(counter)
        n.append(counter)
        return counter + item
    else:
        print(fibonacci)
    

def run():
        functools.reduce(accum,n)


if __name__ ==  '__main__':
    run()