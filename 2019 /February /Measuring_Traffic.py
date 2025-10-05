f = open("traffic.in","r")
f = f.readlines()
f = [x.strip() for x in f]
N = int(f[0])
stuff = []
for i in range(1, N+1):
    x = f[i].split(' ')
    x[1] = int(x[1])
    x[2] = int(x[2])
    stuff.append(x)

none1 = []
none2 = []
i1 = -1
i2 = -1
for i in range(len(stuff)):
    if stuff[i][0]=="none":
        none1=stuff[i]
        i1 = i
        break
for i in range(len(stuff),0,-1):
    if stuff[i-1][0]=="none":
        none2=stuff[i-1]
        i2 = i
        break

possible1 = [none1[1], none1[2]]
possible2 = [none2[1], none2[2]]

for i in range(i1+1, len(stuff)):
    x = stuff[i]
    # print(f'Debug {x=}')
    if x[0]=="none":
        possible1 = [max(possible1[0],x[1]), min(possible1[1],x[2])]
    elif x[0]=="on":
        possible1 = [min(possible1)+min(x[1],x[2]), max(possible1)+max(x[1],x[2])]
    else:
        possible1 = [min(possible1)-max(x[1],x[2]), max(possible1)-min(x[1],x[2])]
    # print(f'    Debug {possible1=}')
    if possible1[0]<0:
        possible1[0] = 0
    if possible1[1]<0:
        possible1[1] = 0

stuff.reverse()
for i in range(len(stuff)):
    if stuff[i][0]=="none":
        i2 = i
        break

for i in range(i2+1, len(stuff)):
    x = stuff[i]
    if x[0]=="none":
        possible2 = [max(possible2[0],x[1]), min(possible2[1],x[2])]
    elif x[0]=="off":
        possible2 = [min(possible2)+min(x[1],x[2]), max(possible2)+max(x[1],x[2])]
    else:
        possible2 = [min(possible2)-max(x[1],x[2]), max(possible2)-min(x[1],x[2])]
    if possible2[0]<0:
        possible2[0] = 0
    if possible2[1]<0:
        possible2[1] = 0

f = open("traffic.out", "w")
f.write(" ".join([str(x) for x in possible2]) + "\n")
f.write(" ".join([str(x) for x in possible1]))
