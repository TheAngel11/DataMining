#!/opt/local/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys
import re
from scipy.sparse import coo_matrix
import numpy
import time


def pagerank(graph, beta=0.85, epsilon=1.0e-8):
	out_degree=numpy.array(graph.sum(axis=1))
	ranks=numpy.ones(graph.shape[0])/graph.shape[0]
	delta = 1.0
	n_iterations = 0

	transition_matrix = graph / numpy.where(out_degree == 0, graph.shape[0], out_degree)

	while delta > epsilon:
		new_ranks = beta * transition_matrix.transpose().dot(ranks)

		offset = (1 - sum(new_ranks)) / graph.shape[0]
		new_ranks += offset

		delta=numpy.sqrt(numpy.sum(numpy.power(ranks-new_ranks,2)))
		ranks,new_ranks=new_ranks,ranks
		print("\nIteration %d has been computed with an delta of %e (epsilon=%e)"%(n_iterations,delta,epsilon), file=sys.stderr)
		n_iterations += 1
	
	print()
	rranks={}
	for i in range(ranks.shape[0]):
		rranks[i]=ranks[i]
	return rranks, n_iterations

def processInput(filename):

	webs={}
	rows=numpy.array([],dtype='int8')
	cols=numpy.array([],dtype='int8')
	data=numpy.array([],dtype='float32')
	for line in open(filename,'r'):
		line=line.rstrip()
		
		m=re.match(r'^n\s([0-9]+)\s(.*)',line)
		if m:
			webs[int(m.groups()[0])]=m.groups()[1]
			continue
		m=re.match(r'^e\s([0-9]+)\s([0-9]+)',line)
		if m:
			rows=numpy.append(rows,int(m.groups()[0]))
			cols=numpy.append(cols,int(m.groups()[1]))
			data=numpy.append(data,1)
			
	graph=coo_matrix((data,(rows,cols)),dtype='float32',shape=(max(webs.keys())+1,max(webs.keys())+1))
	return (webs,graph)

if __name__ == "__main__":
		parser = argparse.ArgumentParser(description="Analyze web data and output PageRank")
		parser.add_argument("file", type=str, help="file to be processed")
		parser.add_argument("--beta", type=float, help="β value to be considered",default=0.8)
		args = parser.parse_args()

		webs,graph=processInput(args.file)
		start = time.time()
		ranks,n_iterations=pagerank(graph,args.beta)
		end = time.time()
		print("It took %f seconds to converge"%(end - start), file=sys.stderr)
		keys=[list(ranks.keys())[x] for x in numpy.argsort(list(ranks.values()))[-1::-1]]
		values=[list(ranks.values())[x] for x in numpy.argsort(list(ranks.values()))[-1::-1]]
		for p,(k,v) in enumerate(zip(keys,values)): 
			print("[%d] %s:\t%e"%(p,webs[k],v))
