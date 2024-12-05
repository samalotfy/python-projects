graph= {
	'S':['B','D','A'],
	'A':['C'],
	'B':['D'],
	'C':['G','D'],
	'D':['G'],
	'G':[]
}
def dfs(graph,start,goal):
	visited=[] 
	stack=[[start]]
	while stack: 
		path=stack.pop()

		node=path[-1] 
		if node in visited: 
			continue 
		visited.append(node) 
		if node==goal: 
			return path 
		else:
			adjacentnodes=graph.get(node,[]) 
			for node2 in adjacentnodes:
				newpath=path.copy() 
				newpath.append(node2)
				stack.append(newpath) 

solution2=dfs(graph,'S','G') 
print('the solution of dfs is ' , solution2)
