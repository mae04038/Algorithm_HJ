N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
cards.sort()
result = []
left, right = 0, N-1

def binary_search(cards, target, left, right):

    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == target:
            return mid
        elif cards[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return None

for i in range(M):
    if binary_search(cards, check[i], 0, N-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')