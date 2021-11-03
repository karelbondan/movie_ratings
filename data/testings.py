# implementation of stack in python using list and pop() list method.
import time

thisislist = []

thisislist.append(1)
thisislist.append('thisisstring')
thisislist.append(3)

print(thisislist)

thisislist.pop()

print(thisislist)
print(thisislist.pop())
print(thisislist)

start = time.time()
for i in range(540650):
    a = 1
print(time.time() - start)