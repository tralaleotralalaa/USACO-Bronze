f = open("guess.in", "r")
f = f.readlines()
N = int(f[0])
animals = []
for i in range(1, N+1):
    x = f[i].split(" ")
    x[-1] = x[-1].strip()
    animals.append(set(x[2:]))

#print(animals)
max_shared = 0
for i in range(N):
    for j in range(i, N):
        if i == j: continue
        shared = animals[i] & animals[j]
        if len(shared)> max_shared:
            max_shared = len(shared)

f = open("guess.out", "w")
f.write(str(max_shared+1))

