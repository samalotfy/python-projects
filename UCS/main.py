graph2=	{
	'S':[('A',2),('B',3),('D',5)],
	'A':[('C',4)],
	'B':[('D',4)],
	'C':[('D',1),('G',2)],
	'D':[('G',5)],
	'G':[]
}	

def pathcost(path):
	totalcost=0
	for (node,cost) in path:
		totalcost+=cost
	return totalcost, path[-1][0]
def ucs(graph, start,goal):
	visited=[]
	queue=[[(start,0)]]
	while queue:
		queue.sort(key=pathcost)
		path=queue.pop(0)
		node=path[-1][0]
		if node in visited:
			continue
		visited.append(node)
		if node==goal:
			return path
		else:
			adjacent=graph.get(node,[])
			for (node2,cost) in adjacent:
				newpath=path.copy()
				newpath.append((node2,cost))
				queue.append(newpath)
			
sol=ucs(graph2, 'S','G')
print ('the solution is ',sol)	
print ('cost is ', pathcost(sol)[0])
