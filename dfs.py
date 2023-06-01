def dfs(graph, start, finish, len, path=[]):
	if type(start) !=int() and type(finish) !=int():
		return
        if start not in path:
           path.append(start)
           len=len+1
           if start==finish:
               return path
           for neighbour in graph[start]:
               path = dfs(graph, start, finish, len, path)
       return [path, len]
#just, a comment for sure, good job
def init_graph():
	dict = {}
	am = input("Введите количество вершин\n")
	for i in range(1, int(am)+1):
		cur_res = []
		am_of_val = input(f"Сколько вершин связывает вершину {i}?\n")
		for j in range(1, int(am_of_val)+1):
			cur_res.append(int(input(f"Введите вершину {j}\n")))
		dict[i]=cur_res
	return dict

graph = init_graph()
print(graph)
path, len = dfs(graph, 2, 4, 0)
print(path)
print(len)


