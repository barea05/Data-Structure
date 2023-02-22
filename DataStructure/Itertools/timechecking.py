import itertools as its
import time

n = 200000000
start = time.time()
for i in its.count(start = 0, step = 1):
    if i < n:
        i
    else:
        break
end = time.time()
print("Difference in time", start, end)
print("time to run ", end - start)
print("***********************************")

start = time.time()
for i in range(n):

    if i < n:
        i
    else:
        break
end = time.time()
print("Difference in time", start, end)
print("time to run ", end - start)