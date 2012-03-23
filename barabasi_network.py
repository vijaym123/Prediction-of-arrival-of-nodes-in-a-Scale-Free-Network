import functions
import random
import networkx as nx

def _random_subset(seq,m):
	    """ Return m unique elements from seq.
	
	    This differs from random.sample which can return repeated
	    elements if seq holds repeated elements.
	    """
	    targets=set()
	    while len(targets)<m:
	        x=random.choice(seq)
	        targets.add(x)
	    return targets

def _network(n,m):
	    # Add m initial nodes (m0 in barabasi-speak)
	    array_nodes = functions.permutation(range(n))
       	    G=nx.complete_graph(m)
	    dic = {}
            for i in range(m):
		dic[i]=array_nodes[i]
	    G=nx.relabel_nodes(G,dic)
	    # Target nodes for new edges
	    targets=list(array_nodes[:m])
	    # List of existing nodes, with nodes repeated once for each adjacent edge
	    repeated_nodes=[]
	    for i in range(m):	    
		repeated_nodes.extend([array_nodes[i]]*(m-1))          
	    # Start adding the other n-m nodes. The first node is m.
	    source=array_nodes[m]
            count = m			
	    while count<n: 
	        # Add edges to m nodes from the source.
	        G.add_edges_from(zip([source]*m,targets)) 
	        # Add one node to the list for each new edge just created.
	        repeated_nodes.extend(targets)
	        # And the new node "source" has m edges to add to the list.
	        repeated_nodes.extend([source]*m) 
	        # Now choose m unique nodes from the existing nodes
	        # Pick uniformly from repeated_nodes (preferential attachement)
	        targets = _random_subset(repeated_nodes,m)
		count +=1		
		if(count<n):
			source = array_nodes[count]	        
            return G,array_nodes
