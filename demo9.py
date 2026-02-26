#priority queue
#removes element based on priority instead of order


#highest priority removed first
#not normal fifo
#smaller number=highest  priority

#task-1
#task-3
#task-2

#real-time eg:
# hospital emergency room
# cpu task scheduling
# printer task proority
# network packet routing


# pseudocode

# insert
# create empty priority queue-create empty list
# heap arranges automatically

#remove
#remove samllest priority element



import heapq


pq=[]

heapq.heappush(pq,3)
heapq.heappush(pq,1)
heapq.heappush(pq,2)

print("priority Queue",pq)

print("removed",heapq.heappop(pq))
print("removed",heapq.heappop(pq))
print("removed",heapq.heappop(pq))









