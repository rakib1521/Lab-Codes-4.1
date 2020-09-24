import queue as q
import gbfsModule as gbfs_q
neighbour = [('i', 'a', 35), ('a', 'i', 35), ('i', 'b', 45), ('b', 'i', 45), ('a', 'c', 22), ('c', 'a', 22),
             ('a', 'd', 32), ('d', 'a', 32),
             ('b', 'd', 28), ('d', 'b', 28), ('b', 'e', 36), ('e', 'b', 36), ('b', 'f', 27), ('f', 'b', 27),
             ('c', 'd', 31), ('d', 'c', 31),
             ('c', 'g', 47), ('g', 'c', 47), ('d', 'g', 30), ('g', 'd', 30), ('e', 'g', 26), ('g', 'e', 26)]

heu_fn = [('i', 80), ('a', 55), ('b', 42), ('c', 34), ('d', 25), ('e', 20), ('f', 17), ('g', 0)]


pq = q.PriorityQueue()
t_nodes = []
path = []


s = str(input('Enter start node:'))
g = str(input('Enter goal node:'))
t_nodes.append((s, 'root'))
visited = {}
next_node = False
for i in range(len(heu_fn)):
    visited[heu_fn[i][0]] = False


for i in range(len(heu_fn)):
    if heu_fn[i][0] ==s:
        pq.put(gbfs_q.NodePriority(s,heu_fn[i][1]))

while not (pq.empty()):
    v = pq.get()
    print(v)
    node = v.node_name
    visited[node] = True
    if (node == g):
        path.append(node)
        break
    else:
        for i in range(len(neighbour)):
            if (neighbour[i][0] == node):
                next_v = neighbour[i][1]
                if (visited[next_v] == False):
                    next_node = True
                    t_nodes.append((node, next_v))
                    for j in range(len(heu_fn)):
                        if heu_fn[j][0] ==next_v:
                            pq.put(gbfs_q. NodePriority(next_v,heu_fn[j][1]))
                else:
                    next_node = False
        if(next_node == True):
            path.append(node)

print('The path is:',end=' ')
for x in path:
    print(x,end=' ')
