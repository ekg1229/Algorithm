import random

# 20개의 랜덤 숫자 생성
numbers = random.sample(range(1, 101), 20)

# Selection Sort 구현
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

sorted_numbers_selection = numbers.copy()
selection_sort(sorted_numbers_selection)
print("Selection Sort 결과:", sorted_numbers_selection)