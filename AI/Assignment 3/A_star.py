import queue as q
import sModule as pri_queue

neighbour = [('i', 'a', 35), ('a', 'i', 35), ('i', 'b', 45), ('b', 'i', 45), ('a', 'c', 22), ('c', 'a', 22),
             ('a', 'd', 32), ('d', 'a', 32),
             ('b', 'd', 28), ('d', 'b', 28), ('b', 'e', 36), ('e', 'b', 36), ('b', 'f', 27), ('f', 'b', 27),
             ('c', 'd', 31), ('d', 'c', 31),
             ('c', 'g', 47), ('g', 'c', 47), ('d', 'g', 30), ('g', 'd', 30), ('e', 'g', 26), ('g', 'e', 26)]

heu_fn = [('i', 80), ('a', 55), ('b', 42), ('c', 34), ('d', 25), ('e', 20), ('f', 17), ('g', 0)]

priority_queue = q.PriorityQueue()
t_nodes = []
path = []

# main
s = str(input('Enter start node:'))
g = str(input('Enter goal node:'))


visited = {}
tn_index = {}
parrent_node = {}
h_value = 0
next_node = False
for i in range(len(heu_fn)):
    visited[heu_fn[i][0]] = False
for i in range(len(heu_fn)):
    if heu_fn[i][0] ==s:
        h_value = heu_fn[i][1]
        priority_queue.put(pri_queue.NodePriority(s, 0, 'root', h_value))
t_nodes.append((s, 0, 'root', h_value))
index = 0
tn_index[s] = 0
parrent_node[0] = s
parrent_node['root'] = 'root'
n_h_value = 0

while not (priority_queue.empty()):
    v = priority_queue.get()
    node = v.name
    visited[node] = True
    if (node == g):
        path.append(node)
        break
    else:
        i = 0
        for i in range(len(neighbour)):
            if (neighbour[i][0] == node):
                next_v = neighbour[i][1]
                index = index + 1
                tn_index[next_v] = index
                parrent_node[index] = node
                cost = neighbour[i][2]
                if (visited[next_v] == False):
                    next_node = True
                    t_nodes.append((node, next_v))
                    for j in range(len(heu_fn)):
                        if heu_fn[j][0] ==next_v:
                            priority_queue.put(pri_queue. NodePriority(next_v,tn_index[next_v],tn_index[node],heu_fn[j][1]+cost))

                else:
                    next_node = False
        if(next_node == True):
            path.append(node)

print('The path is:')
for x in path:
    print(x,end=' ')
