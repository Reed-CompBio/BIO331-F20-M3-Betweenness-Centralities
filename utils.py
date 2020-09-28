'''
Reads a three-column file of (node1,node2,cost) and returns two data structures:
adj_list: dictionary of {node: neighbor_set} (adjacency list as we've described previously)
edge_costs: dictionary of dictionaries.  For a node, the dictionary contains (neighbor,cost)
key-value pairs.  For example, for edge 'A B 1', edge_costs['A']['B'] is 1.
Default behavior is that the network is undirected, so edge_costs['B']['A'] is 1
as well.  If directed=True, the file is considered directed and edge_costs and adj_list
capture directed relationships.
'''
def read_edges(fname,directed=False):
	edge_costs = {}  ## dictionary of dictionaries: {node: {neighbor:cost}}
	adj_list = {} ## adjacency list dictionary: {node: neighbor_set}
	with open(fname) as fin:
		for line in fin:
			row = line.strip().split('\t')
			u = row[0]
			v = row[1]
			weight = float(row[2])
			if u not in edge_costs:
				edge_costs[u] = {}
				adj_list[u] = set()
			if v not in edge_costs:
				edge_costs[v] = {}
				adj_list[v] = set()
			edge_costs[u][v] = weight
			adj_list[u].add(v)
			if not directed: # include the (v,u) edge
				edge_costs[v][u] = weight
				adj_list[v].add(u)
	return adj_list, edge_costs

'''
Given a source node u and a target node v and a dictionary pi of predecessors,
returns the shortest path from u to v.  If there are multiple paths, only
one is returned.  Returned path is a list of nodes.
'''
def get_path(u,v,pi):
	current = v # start at the END of the path.
	path = [] # empty path
	while current != u: # if we're not at the START of the path...
		path = [current] + path ## add element to beginning of path
		current = pi[current] ## update current to be the predecessor.
	path = [u] + path ## add first node to beginning of path
	return path


'''
Posts the graph G to GraphSpace. Copied from Lab 2.
'''
def post(G,gs):
	try:
		graph = gs.update_graph(G)
	except:
		graph = gs.post_graph(G)
	return graph

'''
Returns the hexadecimal color code when given three channels
for red, green, and blue between 0 and 1.  Copied from Lab 3.
'''
def rgb_to_hex(red,green,blue): # pass in three values between 0 and 1
  maxHexValue= 255  ## max two-digit hex value (0-indexed)
  r = int(red*maxHexValue)    ## rescale red
  g = int(green*maxHexValue)  ## rescale green
  b = int(blue*maxHexValue)   ## rescale blue
  RR = format(r,'02x') ## two-digit hex representation
  GG = format(g,'02x') ## two-digit hex representation
  BB = format(b,'02x') ## two-digit hex representation
  return '#'+RR+GG+BB
