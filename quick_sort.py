import random

# 20개의 랜덤 숫자 생성
numbers = random.sample(range(1, 101), 20)

# Quick Sort 구현
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    smaller = []
    equal = []
    larger = []

    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    return quick_sort(smaller) + equal + quick_sort(larger)

sorted_numbers_quick = quick_sort(numbers)
print("Quick Sort 결과:", sorted_numbers_quick)