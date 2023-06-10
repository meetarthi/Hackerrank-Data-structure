a,b = map(int, input().split())
seqList = [[] for i in range(a)]
lastAnswer = 0
result = []
for i in range(b):
    query = list(map(int, input().split()))
    type, x, y = query
    
if type == 1:
        idx = (x ^ lastAnswer) % a
        seqList[idx].append(y)
elif type == 2:
        idx = (x ^ lastAnswer) % a
        seq = seqList[idx]
        lastAnswer = seq[y % len(seq)]
        result.append(lastAnswer)
for r in result:
    print(r)