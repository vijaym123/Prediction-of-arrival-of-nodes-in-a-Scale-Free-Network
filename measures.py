def order_ijPair(actual,i,j):
	if actual.index(i) < actual.index(j):
		return True
	else :
		return False
		

def nc2Measure(actual_order,L): 
	points = 0
	total = len(L)*(len(L)-1)/2
	for i in range(0,len(L)-1):
		for j in range(i+1,len(L)):	
			if actual_order.index(L[i]) < actual_order.index(L[j]) :
				points+=1
	return float(points)/total

def kendallMeasure(actual_order,L): 
	positive_points = 0
	negative_points = 0
	total = len(L)*(len(L)-1)/2
	for i in range(0,len(L)-1):
		for j in range(i+1,len(L)):	
			if actual_order.index(L[i]) < actual_order.index(L[j]):
				positive_points+=1
			else : 
				negative_points
	return float(positive_points-negative_points)/total

def measure_bin(actual,B1,B2):
	pts=0
	for i in B1:
		for j in B2:
			if(actual.index(i)<actual.index(j)):
				pts+=1
	pts=float(pts)
	return pts/(len(B1)*len(B2))

def BinningMeasure(actual,Bins):
	sum = 0
	l = len(Bins)
	for i in range(0,len(Bins)-1):
		for j in range(i+1,len(Bins)):
			sum+=measure_bin(actual,Bins[i],Bins[j])
	return float(sum*2)/(l*(l-1))

