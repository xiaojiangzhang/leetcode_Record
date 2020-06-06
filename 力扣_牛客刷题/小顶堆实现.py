"""
求一个数列前K大数的问题经常会遇到，在程序中一般用小顶堆可以解决
"""
import heapq

n = [3, 2, 1, 0]
heapq.heapify(n)
print(heapq.heappop(n))
# heapq.heappush(n, -1)
print(heapq.nsmallest(n, key=lambda n: n[0]))
