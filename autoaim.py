import math
def solve():
    global h, dead_enemies, enemies, r,s,d,c, n, he, shots
    [r, c, n, s, d, h] = list(map(int, input().strip().split()))
    enemies = []
    for _ in range(n):
        [id, he, x, y] = list(map(int, input().strip().split()))
        enemies.append([id, he, x, y])

    dead_enemies = 0 
    shots = 0

    def algorithm():
        global rounds, h, dead_enemies, enemies, r, c, s, d, n, he, shots
        nearest_enemy_coordinates = 1000000
        nearest_enemy_id = []
        for _ in range(s):
            shots += 1
            for enemy in enemies:
               # print(nearest_enemy_coordinates)
                if enemy[2] < nearest_enemy_coordinates and enemy[1] > 0:
                    nearest_enemy_coordinates = enemy[2]
                    nearest_enemy_id = [enemy[0]]
                elif enemy[2] == nearest_enemy_coordinates and enemy[1] > 0 and enemy[0] not in nearest_enemy_id:
                     nearest_enemy_id.append(enemy[0])

            damage = d - (nearest_enemy_coordinates * h)
            if damage < 1:
                damage = 0
            nearest_enemy_erased = 0
            for enemy_id in nearest_enemy_id:
                enemies[enemy_id][1] = enemies[enemy_id][1] - damage
                if enemies[enemy_id][1] <= 0: ####!
                    nearest_enemy_erased += 1
                    dead_enemies += 1
            if nearest_enemy_erased == len(nearest_enemy_id):
                nearest_enemy_coordinates = 1000000
                nearest_enemy_id = []

        for i in range(len(enemies)):
            if enemies[i][2] == 0:
                enemies[i][2] = r
            else:
                enemies[i][2] = enemies[i][2] - 1

    while not dead_enemies == n:
        algorithm()
    return shots

    


T = int(input())

with open("output.txt", "w") as f:
    for i in range(T):
        f.write(f"Case #{i+1}: {solve()}\n")
