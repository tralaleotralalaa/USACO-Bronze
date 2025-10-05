f = open('sleepy.in','r')
f = f.readlines()
N = int(f[0])
#print(N)
cows = f[1].split(' ')
cows = [int(x) for x in cows]
#print(cows)

x = 1
for i in range(N-1,-1,-1):
    if cows[i]>cows[i-1]:
        x+=1
    else:
        break
#print(x)

result = N-x
#print(idk)

f = open('sleepy.out', 'w')
f.write(str(result))
