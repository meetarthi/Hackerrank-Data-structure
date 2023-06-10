len_of_num = int(input())
numbers = input().split(' ')
reverse = numbers[::-1]
r = ''

for i in range(len_of_num):
    r = r + str(reverse[i]) + ' '

print(''.join(r))