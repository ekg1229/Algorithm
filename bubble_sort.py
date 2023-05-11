import random

# 20개의 랜덤 숫자 생성
numbers = random.sample(range(1, 101), 20)

# 버블 정렬 구현
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

sorted_numbers_bubble = numbers.copy()
bubble_sort(sorted_numbers_bubble)
print("Bubble Sort 결과:", sorted_numbers_bubble)