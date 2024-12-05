graph= {
	'S':['B','D','A'],
	'A':['C'],
	'B':['D'],
	'C':['G','D'],
	'D':['G'],
	'G':[]
}
visited=[]
queue=[]
def bfs(visited,graph , node):
	visited.append(node)
	queue.append(node)
	while queue:
		m=queue.pop(0)
		print(m,end=" ")
		for n in graph[m]:
			if n not in visited:
				visited.append(n)
				queue.append(n)
			
bfs(visited,graph,'S')
print()
