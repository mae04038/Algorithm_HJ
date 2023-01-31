import copy
n, m, k, c = map(int, input().split()) # 격자 크기, 박멸진행년수, 제초제 범위, 제초제 남아있는 년수
trees = [list(map(int, input().split())) for _ in range(n)]
answer = 0 # m년 동안 박멸한 나무의 그루 
gas_graph = [[-1] * n for _ in range(n)]

gx = [-1, 1, 0, 0]
gy = [0, 0, 1, -1]
dx_dy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def grow():
    for i in range(n):
        for j in range(n):
            if trees[i][j] < -1:
                trees[i][j] += 1
            # if trees[i][j] == -2:
            #     trees[i][j] = 0
            
            if trees[i][j] >= 1:
                cnt = 0
                for k in range(4):
                    x, y = gx[k] + i, gy[k] + j
                    if x < 0 or x >= n or y < 0 or y >= n:
                        continue
                    if trees[x][y] >= 1:
                        cnt += 1
                trees[i][j] += cnt

def spread():
    tmp_tree = copy.deepcopy(trees)
    for i in range(n):
        for j in range(n):
            if tmp_tree[i][j] >= 1:
                cnt = 0
                for k in range(4):
                    x, y = gx[k] + i, gy[k] + j
                    if x < 0 or x >= n or y < 0 or y >= n:
                        continue
                    if tmp_tree[x][y] == 0:
                        cnt += 1
                if cnt != 0:
                    spread_trees = trees[i][j] // cnt
                else:
                    spread_trees = 0
                # print(spread_trees) # 확인용
                for k in range(4):
                    x, y = gx[k] + i, gy[k] + j
                    if x < 0 or x >= n or y < 0 or y >= n:
                        continue
                    if tmp_tree[x][y] == 0:
                        trees[x][y] += spread_trees

def cnt_remove(x, y):
    cnt = 0
    for nx, ny in dx_dy:
        for i in range(1, k+1):
            cx, cy = x + nx*i, y + ny*i
            if cx < 0 or cx >= n or cy < 0 or cy >= n or trees[cx][cy] == -1:
                break
            cnt += trees[cx][cy]
    return cnt

def put_remove(x, y): # 제초제 놓기
    # 도중에 벽(-1)이 있거나 나무가 아예 없는 칸(0)이 있으면 해당 칸까지 뿌리고 멈춤
    # global gas_graph
    # gas_graph[x][y] = c
    # if trees[x][y] != 0:
    #     for nx, ny in dx_dy:
    #         for i in range(1, k+1):
    #             cx, cy = x + nx*i, y + ny*i
    #             if cx < 0 or cx >= n or cy < 0 or cy >= n :
    #                 break
    #             if trees[cx][cy] > 0:
    #                 gas_graph[cx][cy] = c
    #                 trees[cx][cy] = 0
    #             elif trees[cx][cy] == 0:
    #                 gas_graph[cx][cy] = c
    #                 break
    #             elif trees[cx][cy] == -1:
    #                 break

    ##########################
    trees[x][y] = -(c+2)
    for nx, ny in dx_dy:
        for i in range(1, k+1):
            cx, cy = x + nx*i, y + ny*i
            if cx < 0 or cx >= n or cy < 0 or cy >= n :
                break
            # if trees[cx][cy] == 0 or trees[cx][cy] == -1: # 나무가 없는 칸
            if trees[cx][cy] <= 0:
                if trees[cx][cy] != -1 and trees[cx][cy] == 0:
                    trees[cx][cy] = -(c+2)
                if trees[cx][cy] <= -2:
                    trees[cx][cy] -= c
                
                break
            
            trees[cx][cy] = -(c+2)

def remove():
    tmp_tree = copy.deepcopy(trees)
    max_num = 0
    final_x, final_y = 0, 0
    for i in range(n):
        for j in range(n):
            if trees[i][j] == -2: # 제초제 뿌릴 때 이전제초제 제거가능하면 제거
                trees[i][j] = 0

            if trees[i][j] >= 1:
                tmp_tree[i][j] += cnt_remove(i, j) # 제초하게 될 나무 그루 수 계산함수
                # print(tmp_tree[i][j]) # 제초할 나무 개수 확인용
                if tmp_tree[i][j] > max_num:
                    max_num = tmp_tree[i][j]
                    final_x, final_y = i, j # 최종 제초제위치
    put_remove(final_x, final_y)
    
    return max_num

def down_remove():
    for i in range(n):
        for j in range(n):
            if gas_graph[i][j] > -1:
                gas_graph[i][j] -= 1


for _ in range(m):
    # 1. 성장
    grow()
    print(trees) # 확인용

    # 2. 번식
    spread()
    print(trees) # 확인용

    # 3. 제초제 뿌리기
    # 제초제 뿌릴 위치 선택
    # 제초제 뿌리기 - c년 동안 유지 => 해당위치 -(c+2) 로 해주고 -2되면 0으로 바꿔주기
    answer += remove()
    print(trees)
    down_remove() #제초제 유지년수 계산
    
print(answer)

    
