line = input()
lists = list()

lists = line.split(' ')
n = int(lists[0])
k = int(lists[1])

mux = 1

for i in range(0, k):
  mux = mux * n

print(mux)
