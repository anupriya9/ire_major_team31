#!/usr/bin/python
import xml.sax
import sys
import collections
i=0
target=open("article.txt",'w')
target.truncate()
author_dict=[]
author=[]
author_id = {}
author_connection={}
journal_author={}
target1=open("article_author_connection.txt",'w')
target1.truncate()
target=open("article_journal_author.txt",'w')
target.truncate()
f=0
with open("www_parse.txt") as f:
	content = f.readlines()
for row in content:
	temp = row.split("#")
	temp[1] = temp[1].replace("\n", "")
	author_id[temp[0]] = temp[1]

#print(author_id["Aacute;ngeles S. Places"])
od2 = collections.OrderedDict(sorted(author_id.items()))
'''for key in od2:
	print key, 
	print " ",
	print od2[key]'''
class article_handler(xml.sax.ContentHandler):
#target=open("a.txt",'w')
#target.truncate()
#	dict_author={}
	def __init__(self):
		self.CurrentData=""
		self.title=""
		self.journal=""
		self.author=""


	def startElement(self,tag,attributes):
		self.CurrentData=tag
		global f
		#print self.CurrentData
		if tag=="article":
			f=1	
		if tag=="inproceedings":
			od1 = collections.OrderedDict(sorted(author_connection.items()))
			count1=0
			for auth in od1:	
				#print auth
				target1.write(auth+"#")
				count1=0
				for auth1 in od1[auth]:
					target1.write(auth1)
					count1=count1+1
					if count1<len(od1[auth]):
						target1.write('|')
					elif count1==len(od1[auth]):
						target1.write('\n')


			od = collections.OrderedDict(sorted(journal_author.items()))
			count=0

			for title in od:
				target.write(title+" # ")
				count=0
				for auth in od[title]:
					target.write(auth)
					count=count+1
					if count<len(od[title]):
						target.write(' | ')
					elif count==len(od[title]):
						target.write('\n')

			sys.exit()	
	def endElement(self,tag):
		global target
		global f
		global author_dict
		global author_connection
		global journal_author
		global author_id
		#print self.CurrentData,tag,f
		global author

		if self.CurrentData=="author" and f==1:
			#''.join(unicode(self.author, 'utf-8').splitlines())
			#self.author = unicode(self.author,"utf-8").replace('\n','')
			temp_str1=self.author.encode("utf8").replace('\n','')
			self.author = ""
			temp_str=temp_str1.encode("utf8").strip(' ')
			#self.author = self.author.encode("utf8")
			#self.author = str(self.author)
			#print "<<"+temp_str+">>"
			#self.author.strip('\n')
			#print "<<" + self.author + ">>"
			#print(type(self.author))

			temp = author_id[temp_str]
			#print temp
			author.append(temp)
			
			#author_id.append(temp)
				#print f1, f2
		if self.CurrentData=="journal" and f==1:
			
			if self.journal in journal_author:
				for val in author:
					journal_author[self.journal].append(val)
				journal_author[self.journal] = list(set(journal_author[self.journal]))
			
			else:
				journal_author[self.journal] = []
				for val in author:
					journal_author[self.journal].append(val)
				journal_author[self.journal] = list(set(journal_author[self.journal]))
			
			if(len(author)>1):
				#print author
				author_connection[author[0]]=author[1:]	
		if tag=="article":
			#print "lokk"
			author=[]
			f=0
			#self.title=""
			self.journal=""
		
	

	def characters(self,content):
		if self.CurrentData=="author":
		#if self.properTagFound==1:
			self.author+=content
			
		#if self.CurrentData=="title":
			#self.title=content
		if self.CurrentData=="journal":
			self.journal+=content		




if ( __name__ == "__main__"):
	parser=xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	Handler2=article_handler()
	parser.setContentHandler(Handler2)
	parser.parse("dblp.xml")



	
#print author_connection
#print journal_author
