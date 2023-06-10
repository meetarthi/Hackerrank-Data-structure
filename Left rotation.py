Len,rot= list(map(int,input().split()))
d = list(map(int,input().split()))
n = Len-rot
trans = (d[-n:] + d[:-n])
print(*trans)