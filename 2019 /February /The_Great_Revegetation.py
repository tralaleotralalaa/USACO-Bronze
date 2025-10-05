f = open("revegetate.in","r")
f = f.readlines()
f = [x.strip() for x in f]
f = [x.split(' ') for x in f]
N = int(f[0][0])
M = int(f[0][1])
pastures = []
for i in range(1, len(f)):
    thing = [int(x) for x in f[i]]
    pastures.append(thing)

grid = {}
for i in range(1, N+1):
    grid[i]=[]

for x in pastures:
    grid[x[0]].append(x[1])
    grid[x[1]].append(x[0])

seeds = [-1]*N
for i in range(1,N+1):
    used = [False]*5
    for j in grid[i]:
        if seeds[j-1]!=-1:
            used[seeds[j-1]]=True
    for k in range(1, 5):
        if not used[k]:
            seeds[i-1] = k
            break
seeds = "".join([str(x) for x in seeds])

f = open("revegetate.out", "w")
f.write(seeds)
    
