import networkx as nx
import functions as fun
import measures as m
import network
import numpy
import matplotlib.pyplot as plt

nodes = 10
connection = 2

G,actualOrder = network.barabasi_albert_graph(nodes,connection)
H = nx.DiGraph()
Bins_degree = fun.constructBins_Degree(G)
node_pairs = []

for i in range(nodes) :
	for j in range(i,nodes) :
		if i!=j : 
			node_pairs.append((i,j))

count = 0
correct_order = 0
diff = 0.009
Function = nx.pagerank(G)

for i in node_pairs:
	if Function[i[1]]-Function[i[0]] >=diff :
		count+=1
		H.add_edge(i[0],i[1])
		H[i[0]][i[1]]['weight'] = Function[i[1]]-Function[i[0]] 
		if m.order_ijPair(actualOrder,i[1],i[0]):
			correct_order+=1

	elif Function[i[0]]-Function[i[1]]>=diff :
		count+=1
		H.add_edge(i[1],i[0])
		H[i[1]][i[0]]['weight'] = Function[i[0]]-Function[i[1]] 
		if m.order_ijPair(actualOrder,i[0],i[1]):
			correct_order+=1	

H = fun.directedGraphToDAG(H)
predictedOrder = fun.predictedOrderFromDigraph(H)
deduceBinOrder = fun.deduceBinOrderFromDiGraph(H)


print "Percentage of correct order : ", float(correct_order)/count
print "percentage of such pairs : ", float(count)/(nodes*(nodes-1)/2)
print actualOrder
print "Predicted Order Of Nodes : ", predictedOrder
print "Predicted Order Of Nodes after binnning : ",deduceBinOrder
print "Score of Predicted Order Of Nodes : ", m.nc2Measure(actualOrder,predictedOrder)
print "Predicted Order Of Nodes after binnning : ",m.BinningMeasure(actualOrder,deduceBinOrder)

degree_bin = fun.constructBins_Degree(G)
print "Binning based on degree : ",degree_bin
x = [(G.degree(i[0]),len(i)) for i in degree_bin]
x.sort()
y = [i[1] for i in x]
x = [i[0] for i in x] 

plt.plot(x,y,'ro')
plt.plot(x,y)
plt.show()
