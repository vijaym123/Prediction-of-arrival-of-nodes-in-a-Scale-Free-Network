import random
import matplotlib.pyplot as plt
import networkx as nx
import functions
import copy 

def constructBins_Degree(G):	
	degree_dic = {}
	for i in G.nodes():
		try :
			degree_dic[G.degree(i)].append(i)
		except KeyError :
			degree_dic[G.degree(i)] = [i]	
	return degree_dic.values()				

def dictonary_Sorting(d):
	items = [(k,v) for v,k in d.items()]
        items.sort()
        items.reverse()
        array = [ v for k, v in items]	
	return array

def plotNetwork(G):
	nx.draw(G)			
	plt.show()

def function_Map(Main_Vector,Sample_Vector):
	Map = []
	s_v = []
	for i in range(0,len(Sample_Vector)):
		s_v.append((Sample_Vector[i],i))
	s_v.sort()
	s_v.reverse()

	m_v = []	
	for j in range(0,len(Main_Vector)):
		m_v.append((Main_Vector[j],j))
	m_v.sort()
	m_v.reverse()	
	for i in range(0,len(Main_Vector)):
		Map.append((s_v[i][1],m_v[i][1]))
	Map.sort()
	New_Array=[]
	for i in range(0,len(Main_Vector)):
		New_Array.append(Map[i][1])	
	return 	New_Array


def swap(L,i,j):
	temp=L[i]
	L[i]=L[j]
	L[j]=temp
	return L	

def permutation(L):
	'''This is a function which returns the permutation of a list'''
	n=len(L)
	
	for i in range(n-1):
		L1=swap(L,i,random.randint(i+1,len(L)-1))
	
	return L1

def predictedOrderFromDigraph(GDirected):
	Deg = []
	for i in range(GDirected.number_of_nodes()):
		Deg.append((GDirected.in_degree(i),GDirected.out_degree(i),i))
	Deg.sort()
	Deg.reverse()
	inDegrees = list(set([x for x,y,v in Deg]))
	predictedOrder = []
	for i in inDegrees:
		sublist = []
		for j in Deg:
			if j[0] == i:
				sublist.append(j[2])
		sublist.reverse()
		predictedOrder.extend(sublist)
	return predictedOrder

def deduceBinOrderFromDiGraph(GDirected):
	DeducingGraph = copy.deepcopy(GDirected)
	Bins = []
	while DeducingGraph.number_of_nodes() > 0:
		Bin = []
		Dict = DeducingGraph.in_degree()
		List = [(k,v) for v,k in Dict.items()]
		List.sort()	
		k = List[0][0]	
		for i in List:
			if i[0] == k:
				Bin.append(i[1])
		Bins.append(Bin)
		DeducingGraph.remove_nodes_from(Bin)
	return Bins

def directedGraphToDAG(D_Graph):
	Weight_EdgeList = []
	for i in D_Graph.edges():
		Weight_EdgeList.append((D_Graph[i[0]][i[1]]['weight'],i[0],i[1]))
	Weight_EdgeList.sort()
	Weight_EdgeList.reverse()		
	while(not nx.is_directed_acyclic_graph(D_Graph)):
		k = Weight_EdgeList.pop()
		D_Graph.remove_edge(k[1],k[2])
	return D_Graph
