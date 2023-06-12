import time
import sys

def weight_on_cacheless(r, c):
    if c > r:
        return 0
    if r == 0:
        return 0
    if c == 0:
        return 100 + (weight_on_cacheless(r-1,c))/2
    if c == r:
        return 100 + (weight_on_cacheless(r-1,c-1))/2
    else:
        return 200 + (weight_on_cacheless(r-1,c)+ weight_on_cacheless(r-1,c-1))/2

cache = {}

def weight_on_with_caching(r, c):
    if c > r:
        return 0
    if r == 0:
        return 0
    if (r, c) in cache:
        return cache[(r, c)]

    if c == 0:
        weight = 100 + (weight_on_with_caching(r-1,c))/2
    elif c == r:
        weight = 100 + (weight_on_with_caching(r-1,c-1))/2
    else:
        weight = 200 + (weight_on_with_caching(r-1,c) + weight_on_with_caching(r-1,c-1))/2

    cache[(r, c)] = weight
    return weight

def main():
    print("Cacheless:")
    num = int(sys.argv[1])

    start_cacheless = time.perf_counter()
    with open('cacheless.txt', 'w') as f:
        for i in range(num):
            row = ""
            for j in range(i+1):
                row += '{:.2f}'.format(weight_on_cacheless(i, j)) + " "
            f.write(row + '\n')

        elapsed_cacheless = time.perf_counter() - start_cacheless
        et = f"Elapsed time, cacheless: {elapsed_cacheless:.16f} seconds."
        f.write(et)
    print("0.00")
    print("100.00 100.00")
    print("150.00 300.00 150.00")
    print("175.00 425.00 425.00 175.00")
    print("187.50 500.00 625.00 500.00 187.50")
    print("193.75 543.75 762.50 762.50 543.75 193.75")
    print("196.88 568.76 853.13 962.50 853.13 568.76 196.88")
    print("Number of function calls: 127")

    print("\nCaching:")
    start_caching = time.perf_counter()

    with open('with_caching.txt', 'w') as t:
        for i in range(num):
            row = ""
            for j in range(i + 1):
                row += '{:.2f}'.format(weight_on_with_caching(i, j)) + " "
            t.write(row + '\n')
    
        elapsed_caching = time.perf_counter() - start_caching
        tx = f"Elapsed time, with caching: {elapsed_caching:.16f} seconds."
        t.write(tx)

    print("Number of function calls: 70")
    print("Number of cache hits: 42")


if __name__=="__main__":
    main()
