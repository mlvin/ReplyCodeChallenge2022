import math
def solve():
    [n_user , m] = list(map(int, input().strip().split()))
    p = list(map(int, input().strip().split()))
    daycount = 0
    calendar = [0]*m

    for user in p:
        for i in range(0, m, user):
            calendar[i] += 1
            #if i*user > m:
            #c#alendar[i*user] += 1
    for i in calendar:
        if i == n_user:
            daycount += 1
    return daycount

        




T = int(input())
with open("output.txt", "w") as f:
    for i in range(T):
        f.write(f"Case #{i+1}: {solve()}\n")
