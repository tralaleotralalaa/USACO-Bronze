file = open('mowing.in')
lines = file.readlines()
N = int(lines[0])
lines = [line.split() for line in lines]
for i in range(1,N+1):
    lines[i][1] = int(lines[i][1])
print(lines)

x, y = 0,0
x2,y2 = 0,0
places = {}
cnt = 0
max_x = 1001
for i in range(1,N):
    print(lines[i])
    if lines[i][0]=='N':
        x2,y2 = 0,1
    if lines[i][0]=='S':
        x2,y2 = 0,-1
    if lines[i][0]=='E':
        x2,y2 = 1,0
    if lines[i][0]=='W':
        x2,y2 = -1,0
        
    for j in range(lines[i][1]):
        x+=x2
        y+=y2
        cnt+=1
        if (x,y) in places:
            t = places[(x,y)]
            if cnt-t<max_x:
                max_x = cnt-t
        places[(x,y)]=cnt
    print(places)

print(max_x)
if max_x==1001:
    max_x = -1
file = open('mowing.out','w')
file.write(f'{max_x}')
