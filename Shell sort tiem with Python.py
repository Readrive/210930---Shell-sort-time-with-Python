import time
from random import randint

#쉘 정렬
array_b = []
#for _ in range(10000):
#    array.append(randint(1, 100))

#최악
for i in range(1000000, 1, -1):
    array_b.append(i)

start_time = time.time()

N = len(array_b)
h = N // 2

for i in range(h, N):
    temp = array_b[i]
    j = i - h
    while j >= 0 and array_b[j] > temp:
        array_b[j + h] = array_b[j]
        j -= h
        array_b[j + h] = temp
    h //= 2

end_time = time.time()
print("쉘 정렬 최악 성능 측정:", end_time - start_time)



#최선
array_g = []

for i in range(1, 1000000):
    array_g.append(i)

start_time = time.time()

N = len(array_g)
h = N // 2

for i in range(h, N):
    temp = array_g[i]
    j = i - h
    while j >= 0 and array_g[j] > temp:
        array_g[j + h] = array_g[j]
        j -= h
        array_g[j + h] = temp
    h //= 2

end_time = time.time()
print("쉘 정렬 최선 성능 측정:", end_time - start_time)
