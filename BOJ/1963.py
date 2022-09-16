'''
특정 값 A, B -> A에서 B로 가는 최소길이
각가의 자리별로 만들 수 있는 수 리스트를 모두 구한 뒤 배열에 담고, 나중에
큐에 추가할 때 소수와 방문 여부를 검사하는 방식
'''
T = int(input()) #테스트케이스 개수

def isPrime(k):
    for i in range(3, k//2 + 1, 2):
        if k % i == 0:
            return False
    return True

for _ in range(T):
    answer = 0
    n1, n2 = map(int, input().split())

    if n1 == n2:
        print(0)
        continue







