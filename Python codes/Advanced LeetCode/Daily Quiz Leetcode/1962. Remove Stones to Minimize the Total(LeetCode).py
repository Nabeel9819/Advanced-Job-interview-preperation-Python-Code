from heapq import heapify, heapreplace
#input
k = 2
piles = [5,4,9]

#Program 
pq = [-x for x in piles]
heapify(pq)
for _ in range(k): heapreplace(pq, pq[0]//2)
print(-sum(pq))


#Expected Output 
#  12