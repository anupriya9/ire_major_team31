#!/usr/bin/python
import xml.sax
import sys
import collections
i=0
dict_book={}
author_connection={}
target=open("book_match1.txt",'w')
target.truncate()
target1=open("auth_co.txt",'w')
target1.truncate()
author_id={}
f=0
l=[]
with open("www_parse.txt") as f:
	content = f.readlines()
for row in content:
	temp = row.split("#")
	temp[1] = temp[1].replace("\n", "")
	author_id[temp[0]] = temp[1]
class book_handler(xml.sax.ContentHandler):
#target=open("a.txt",'w')
#target.truncate()
#	dict_author={}
	def __init__(self):
		self.CurrentData=""
		self.editor=""
		self.title=""
		self.author=""

	def startElement(self,tag,attributes):
		global f
		self.CurrentData=tag
		if tag=="book":
			#print "inside"
			f=1		

	def endElement(self,tag):
		global f
		global l
		global dict_book 	
		global author_id
		#print tag,f
		if (self.CurrentData=="editor" or self.CurrentData=="author") and f==1:
			if(self.CurrentData=="editor"):
				temp_str1=self.editor.encode("utf8").replace('\n','')
				temp_str=temp_str1.encode("utf8").strip(' ')
				self.editor=""
				l.append(author_id[temp_str])
			if (self.CurrentData=="author"):
				temp_str1=self.author.encode("utf8").replace('\n','')
				self.author = ""
				temp_str=temp_str1.encode("utf8").strip(' ')
				l.append(author_id[temp_str])	
		if self.CurrentData=="title" and f==1:	
			temp_str1=self.title.encode("utf8").replace('\n','')
			temp_str=temp_str1.encode("utf8").strip(' ')	
			dict_book[temp_str]=l
			self.title=""
			if len(l)>1:
				author_connection[l[0]]=l[1:]
		if tag=="title":
			self.title=""
			f=0	
			l=[]
			#print f1


	def characters(self,content):
		global f
		if self.CurrentData=="editor" and f==1:
		#if self.properTagFound==1:
			self.editor+=content
		if self.CurrentData=="title" and f==1:
			self.title+=content
		if self.CurrentData=="author" and f==1:
			self.author+=content



if ( __name__ == "__main__"):
	parser=xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	Handler=book_handler()
	parser.setContentHandler(Handler)
	parser.parse("dblp.xml")

#print dict_book

od = collections.OrderedDict(sorted(dict_book.items()))
count=0
print "writing to book book_match1"
for title in od:
	if len(title)==0:
		continue
	target.write(title+">>")
	count=0
	for auth in od[title]:
		target.write(auth)
		count=count+1
		if count<len(od[title]):
			target.write('|')
		elif count==len(od[title]):
			target.write('\n')

od1 = collections.OrderedDict(sorted(author_connection.items()))
count1=0
print "write to auth_co"
for auth in od1:
	if len(auth)==0:
		continue
	target1.write(auth+"#")
	count1=0
	for auth1 in od1[auth]:
		target1.write(auth1)
		count1=count1+1
		if count1<len(od1[auth]):
			target1.write('|')
		elif count1==len(od1[auth]):
			target1.write('\n')