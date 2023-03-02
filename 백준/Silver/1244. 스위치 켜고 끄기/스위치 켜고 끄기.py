import sys
input = sys.stdin.readline

def boy(num):
    check = []
    cnt = 0
    while num*cnt <= n:
        cnt += 1
        check.append(cnt)
        if n // num == cnt:
            break
    return sorted(check)

def girl(num):
    check = []
    cnt = 0
    if len(state[1:num+1]) < len(state[num:]):
        while (num-cnt) > 1:
            cnt += 1
            check.append(cnt)
            if num == cnt:
                break
    else:
        while (num+cnt) < n:
            cnt += 1
            check.append(cnt)
            if num == cnt:
                break
    return sorted(check)

def switch(idx):
    if state[idx] == 0:
        state[idx] = 1
    else:
        state[idx] = 0
    return state[idx]


n = int(input())
state = [0] + list(map(int, input().split()))
student_num = int(input())

for _ in range(student_num):
    gen, num = map(int, input().split())
    if gen == 1:
        check = boy(num)
        for idx in check:
            idx = idx * num
            switch(idx)
    elif gen == 2:
        check = girl(num)
        for idx in check:
            if state[num - idx] == state[num + idx]:
                switch(num - idx)
                switch(num + idx)
            else:
                break
        switch(num)

for i in range(1, n, 20):
    print(*state[i:i+20])