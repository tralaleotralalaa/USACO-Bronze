f = open("gymnastics.in", "r")
f = f.readlines()
f = [x.strip() for x in f]
f = [x.split(" ") for x in f]
K = int(f[0][0])
N = int(f[0][1])
sessions = []
for x in f[1::]:
    x = [int(i) for i in x]
    sessions.append(x)
#print(sessions)

possible = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if i!=j:
            possible.append([i,j])
#print(possible)

order = []
for i  in range(K):
    thing = {}
    for j in range(N):
        thing[sessions[i][j]]=j
    order.append(thing)
#print(order)

def checkOrder(a,b,o):
    if o[a]<o[B]:
        return True
    else:
        return False

result = 0
for p in possible:
    A, B = (p[0], p[1])
    count = 0
    for i in range(K):
        if checkOrder(A, B, order[i]):
            count+=1
    if count==K:
        result+=1
#print(result)

f = open("gymnastics.out", "w")
f.write(str(result))
