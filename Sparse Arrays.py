n = int(input())
strings = []
for i in range(n):
    strings.append(input())

q = int(input())
queries = []
for i in range(q):
    queries.append(input())

counts = {}
for s in strings:
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1

results = []
for q in queries:
    if q in counts:
        results.append(counts[q])
    else:
        results.append(0)
for i in results:
    print(i)