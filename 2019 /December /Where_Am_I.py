f = open("whereami.in" , "r")
f = f.readlines()
N = int(f[0])
road = f[1].strip()

def checkDuplicates(x, n):
    possible = set()
    for i in range(0, N-n+1):
        mailboxes = x[i:i+n]
        if mailboxes in possible:
            return False
        possible.add(mailboxes)
    return True

result = N-1
for i in range(1, N-1):
    if checkDuplicates(road, i):
        result = i
        break

f = open("whereami.out" , "w")
f.write(str(result))
