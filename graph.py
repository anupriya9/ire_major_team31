#!/usr/bin/python

with open("article_journal_author.txt") as f:
	content = f.readlines()
graph_article={}

for row in content:
	temp = row.split("#")
	author_id = temp[1].split("|")
	length=len(author_id)
	i=0
	j=i+1
	id_tuple=()
#print "list length is " + str(length)
	while i<=(length-2):
		while (j<=length-1):
			id_tuple=()
			small=min(int(author_id[i]),int(author_id[j]))
			large=max(int(author_id[i]),int(author_id[j]))
			id_tuple=id_tuple+(small,)
			id_tuple=id_tuple+(large,)
#print id_tuple
			if id_tuple in graph_article:
				graph_article[id_tuple]+=10
			else:
				graph_article[id_tuple]=10
			j=j+1
		i=i+1	 		
for key in graph_article:
	print str(key[0])+" , "+str(key[1])+" , "+str(graph_article[key])


