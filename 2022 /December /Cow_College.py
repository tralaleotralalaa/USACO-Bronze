N = int(input())
cows = input()
cows = cows.split()
cows = [int(i) for i in cows]
cows.sort()

max_tuition = 0
max_money = 0
for i in range(N):
    tuition = cows[i]
    money = tuition*(N-i)
    if money>max_money:
        max_money = money
        max_tuition = tuition

print(str(max_money), str(max_tuition))
