'''
1번 테스트케이스 - 시간초과 오류 해결 : 소수찾을 때 제곱근 사용
'''
import math
def isPrime(k):

    if k == 1:
        return False
    if k == 2:
        return True
    for i in range(3, int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0

    result = []
    while n > k:
        result.append(n%k)
        n //= k
    result.append(n)
    result.reverse()
    print(result)

    primes = []

    num = ''
    for i in range(len(result)):
        if result[i] != 0:
            num += str(result[i])
        else:
            primes.append(num)
            num = ''
            continue
    primes.append(num)
    print(primes)

    for j in range(len(primes)):
        if primes[j] != '':
            if isPrime(int(primes[j])):
                answer += 1
        # if isPrime(n):
        #     print("소수")
        #     answer += 1

    return answer



'''다른 사람 풀이
# n을 k진법으로 나타낸 문자열 반환
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

# n이 소수인지 판정
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    s = conv(n,k)
    cnt = 0
    for num in s.split('0'):
        if not num: continue # 빈 문자열에 대한 예외처리
        if isprime(int(num)): cnt += 1
    return cnt


'''