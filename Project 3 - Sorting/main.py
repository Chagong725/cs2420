def is_sorted(lyst):
    if not isinstance(lyst, list):
        raise TypeError("lyst must be a list")
    
    for item in lyst:
        if not isinstance(item, int):
            raise TypeError("All elements in lyst must be integers")
    
    return all(lyst[i] <= lyst[i+1] for i in range(len(lyst)-1))

def quicksort(lyst):
    if not isinstance(lyst, list):
        raise TypeError("lyst must be a list")

    def partition(lyst, low, high):
        i = low - 1
        pivot = lyst[high]
        comparisons = 0
        swaps = 0

        for j in range(low, high):
            comparisons += 1
            if lyst[j] <= pivot:
                i += 1
                lyst[i], lyst[j] = lyst[j], lyst[i]
                swaps += 1

        lyst[i + 1], lyst[high] = lyst[high], lyst[i + 1]
        swaps += 1

        return i + 1, comparisons, swaps

    def quicksort_helper(lyst, low, high):
        comparisons = 0
        swaps = 0

        if low < high:
            pi, c1, s1 = partition(lyst, low, high)
            c2, s2 = quicksort_helper(lyst, low, pi - 1)
            c3, s3 = quicksort_helper(lyst, pi + 1, high)

            comparisons = c1 + c2 + c3
            swaps = s1 + s2 + s3

        return comparisons, swaps

    comparisons, swaps = quicksort_helper(lyst, 0, len(lyst) - 1)
    return lyst, comparisons, swaps

def mergesort(lyst):
    if not isinstance(lyst, list):
        raise TypeError("lyst must be a list")

    def merge(left, right):
        merged = []
        i = j = 0
        comparisons = 0
        swaps = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                swaps += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, comparisons, swaps

    def mergesort_helper(lyst):
        if len(lyst) <= 1:
            return lyst, 0, 0

        mid = len(lyst) // 2
        left, comparisons_left, swaps_left = mergesort_helper(lyst[:mid])
        right, comparisons_right, swaps_right = mergesort_helper(lyst[mid:])
        merged, comparisons_merge, swaps_merge = merge(left, right)

        comparisons = comparisons_left + comparisons_right + comparisons_merge
        swaps = swaps_left + swaps_right + swaps_merge

        return merged, comparisons, swaps

    sorted_list, comparisons, swaps = mergesort_helper(lyst)
    return sorted_list, comparisons, swaps

def selection_sort(lyst):
    if not isinstance(lyst, list):
        raise TypeError("lyst must be a list")

    comparisons = 0
    swaps = 0

    for i in range(len(lyst)):
        min_idx = i
        for j in range(i + 1, len(lyst)):
            comparisons += 1
            if lyst[j] < lyst[min_idx]:
                min_idx = j

        lyst[i], lyst[min_idx] = lyst[min_idx], lyst[i]
        swaps += 1

    return lyst, comparisons, swaps

def insertion_sort(lyst):
    if not isinstance(lyst, list):
        raise TypeError("lyst must be a list")

    comparisons = 0
    swaps = 0

    for i in range(1, len(lyst)):
        key = lyst[i]
        j = i - 1

        while j >= 0 and lyst[j] > key:
            comparisons += 1
            lyst[j + 1] = lyst[j]
            swaps += 1
            j -= 1

        lyst[j + 1] = key

    return lyst, comparisons, swaps

def main():
    import random
    import time

    DATA_SIZE = 100000
    random.seed(0)
    DATA = random.sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    test = DATA.copy()

    print("Starting insertion_sort")
    start_time = time.time()
    results = insertion_sort(test)
    end_time = time.time()
    print("Sorted list:", results[0])
    print("Number of comparisons:", results[1])
    print("Number of swaps:", results[2])
    print("Execution time:", end_time - start_time, "seconds")

    # Run other sorting algorithms in a similar way

if __name__ == "__main__":
    main()
