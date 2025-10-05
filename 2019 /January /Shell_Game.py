f = open("shell.in", "r")
input_s = f.readlines()

N = int(input_s[0])
swaps = []
for i in range(N):
    x = input_s[i+1].split(' ')
    x = [int(i) for i in x]
    swaps.append(x)

shells = [[1,0,0],[0,1,0],[0,0,1]]
guess = [0,0,0]

for i in range(3):
    for x in swaps:
        idk = x[0]
        thing = shells[i][idk-1]
        shells[i][idk-1] = shells[i][x[1]-1]
        shells[i][x[1]-1] = thing
        if 1 == shells[i][x[2]-1]:
            guess[i]+=1

highest_score = max(guess)
with open('shell.out', 'w') as f:
    f.write(f'{highest_score}\n')

