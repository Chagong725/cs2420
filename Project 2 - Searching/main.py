from random import seed, sample
import math


def make_data(data_size):  # DO NOT REMOVE OR MODIFY THIS FUNCTION
    '''A generator for producing data_size random values
    '''
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    data.sort()
    while True:
        yield data


def linear_search(lyst, target):
    comparisons = 0
    for index, value in enumerate(lyst):
        comparisons += 1
        if value == target:
            return True, comparisons
    return False, comparisons


def binary_search(lyst, target):
    comparisons = 0
    left, right = 0, len(lyst) - 1
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if lyst[mid] == target:
            return True, comparisons
        elif lyst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False, comparisons


def jump_search(lyst, target):
    comparisons = 0
    n = len(lyst)
    jump = int(math.sqrt(n))
    left, right = 0, 0

    while right < n and lyst[right] < target:
        comparisons += 1
        left = right
        right += jump

    for i in range(left, min(right + 1, n)):
        comparisons += 1
        if lyst[i] == target:
            return True, comparisons
    return False, comparisons


def main():
    data_size = 1000
    data_gen = make_data(data_size)
    data = next(data_gen)
    target = 500

    found, comparisons = linear_search(data, target)
    print(f"Linear search: found={found}, comparisons={comparisons}")

    found, comparisons = binary_search(data, target)
    print(f"Binary search:ons={comparisons}")

    found, comparisons = jump_search(data, target)
    print(f"Jump search: found={found}, comparisons={comparisons}")


if __name__ == "__main__":
    main()
