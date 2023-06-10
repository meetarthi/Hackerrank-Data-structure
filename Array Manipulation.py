n, num_queries = map(int, input().split())
queries = []

for i in range(num_queries):
    start, end, value = map(int, input().split())
    queries.append((start, end, value))

arr = [0] * n

for query in queries:
    start, end, value = query
    arr[start - 1] += value
    if end < n:
        arr[end] -= value

prefix_sum = 0
max_value = 0
for i in range(n):
    prefix_sum += arr[i]
    if prefix_sum > max_value:
        max_value = prefix_sum

print(max_value)