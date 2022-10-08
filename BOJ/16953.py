start, finish = map(int, input().split())
ans = 1


while finish != start:
    tmp = finish
    ans += 1
    if tmp%10 == 1:
        finish //= 10
    elif finish%2 == 0:
        finish //= 2
    
    if tmp == finish:
        ans = -1
        break


print(ans)