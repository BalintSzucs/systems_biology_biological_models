#!/usr/bin/env python

import sys, collections, json, networkx as nx, gzip, shutil, urllib.request as request
from contextlib import closing


#Initializing lists and dicts
geneID_list, duplicatelist, countlist =list(), list(), list()
outerdict, innerdict, dict_list =dict(), dict(), dict()

#Fetching and pre-processing file from NCBI Database
def fetch(file):
    outfile=open('gene2pubmed_processed','w')
    with closing(request.urlopen('ftp://ftp.ncbi.nih.gov/gene/DATA/gene2pubmed.gz')) as r:
        with open('gene2pubmed.gz', 'wb') as f:
            shutil.copyfileobj(r, f)
            with gzip.open('gene2pubmed.gz','rt') as infile:
                for line in infile:
                    if line.startswith(file):
                        outfile.write("\t".join(line.split()[1:]) + "\n")
                sys.stdout.write('A file was generated with the data requested.')  
    outfile.close()

#Counting similarities between GeneIDs based on Pubmed
def count_weight(s):
    #countlist=list()
    for x in s:
        for n in s:
            if x == n:
                countlist.append(0)
            if x != n:
                count=(len(set(s[x]) & set(s[n])))          
                countlist.append(count)

#Adding Pubmed-GeneID counts to nested-dict
def weight_to_dict(k):
    #duplicatelist=list()
    duplicatelist=k 
    list_no=0            
    for h in k:
        for h_1 in duplicatelist:
            outerdict[str(h)][str(h_1)]['weight'] = int(countlist[list_no])        
            list_no+=1

#Search for a given Taxonomy ID from NCBI
TaxID=input('Input an NCBI Taxonomy ID')
fetch(TaxID)
#Open and process GenID and PubmedID's associated with a TaxID
with open('gene2pubmed_processed', 'r') as infile:
    for line in infile:
        tmp=line.split()
        #GeneID - Dict-of-list
        if tmp[0] in dict_list:
            dict_list[tmp[0]] += tmp[1:]
        else:
            dict_list[tmp[0]] = tmp[1:] 
        #GeneID list  
        geneID=tmp[0].strip()
        geneID_list.append(geneID)
        geneID_list = list(dict.fromkeys(geneID_list))
        #Nested dictionary with Gene ID's
        outerdict[geneID]=innerdict
        innerdict[geneID]={}
        outerdict = collections.defaultdict(lambda : collections.defaultdict(dict))                          
count_weight(dict_list)           
weight_to_dict(geneID_list)        

#Write to Graphml
finaldict = json.loads(json.dumps(outerdict))
G=nx.from_dict_of_dicts(finaldict)
nx.readwrite.json_graph.cytoscape_data(G, attrs=None)
#print(G.adj)
nx.write_graphml_lxml(G,'finaltest.graphml')