num = int(input())
line = input()
lists = list()

lists = line.split(' ')

first = lists[0]
last = lists[num-1]

m_num = (num-1) /2

mid = lists[int(m_num)]

a = str(first) + " " + str(mid) + " " + str(last)

print(a)
