import random

# 20개의 랜덤 숫자 생성
numbers = random.sample(range(1, 101), 20)

# Insertion Sort 구현
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

sorted_numbers_insertion = numbers.copy()
insertion_sort(sorted_numbers_insertion)
print("Insertion Sort 결과:", sorted_numbers_insertion)