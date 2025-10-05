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

def makePairs(stuff):
    idk = set()
    for i in range(len(stuff)):
        for j in range(i+1, len(stuff)):
            idk.add((stuff[i], stuff[j]))
    return idk

def findCommon(list1, list2):
    same = []
    for x in list1:
        if x in list2:
            same.append(x)
    return same

pairs = makePairs(sessions[0])
common = []
for i in range(1, K):
    if i!=1:
        pairs = makePairs(sessions[i])
        common = findCommon(pairs, common)
    else:
        pairs2 = makePairs(sessions[i])
        common = findCommon(pairs, pairs2)

count = str(len(common))
f = open("gymnastics.out", "w")
f.write(count)

