from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import utils

def main():
	# connect to GraphSpace
	graphspace = GraphSpace('YOUR_EMAIL','YOUR_PASSWORD')

    # uncomment when you need it
	#run_example(graphspace)
	#run_yellowstone(graphspace)
	#run_badgers(graphspace)

	return

## calculate and post centralities for UNWEIGHTED & WEIGHTED example graph.
def run_example(graphspace):
	fname = 'example-edges.txt'
	adj_list, edge_costs = utils.read_edges(fname)

	return

## calculate and post centralities for UNWEIGHTED yellowstone food web
def run_yellowstone(graphspace):
	fname = 'yellowstone-edges.txt'
	adj_list, edge_costs = utils.read_edges(fname)

	return

## calculate and post centralities for WEIGHTED badger graph
def run_badgers(graphspace):
	fname = 'badger-edges.txt'
	adj_list, edge_costs = utils.read_edges(fname)

	return

## Start by copying shortest_paths() from Lab 3 and modify it.
def unweighted_shortest_paths(adj_list, n):
    dist = None # this will be a dictionary of (node,dist from n) key-value pairs.
    pi = None # this will be a dictionary of (node,predecessor) key-value pairs.

	return dist, pi

## Start by copying unweighted_shortest_paths() above and modify it.
def weighted_shortest_paths(edge_costs, n):
	dist = None # this will be a dictionary of (node,dist from n) key-value pairs.
    pi = None # this will be a dictionary of (node,predecessor) key-value pairs.

	return dist, pi

## get a dictionary of (node,betweenness_centrality) key-value pairs for all nodes in the graph.
## Handle the case where weighted = False and weighted = True.
def get_centralities(adj_list,edge_costs,weighted):
    centralities = None # this will be a dictionary of (node,centrality) key-value pairs.

	return centralities

if __name__ == '__main__':
	main()
