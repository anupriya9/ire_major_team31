#!/usr/bin/python
import xml.sax
import sys
import collections
i=0
inproceedings_dict={}
target=open("inproceedings.txt",'w')
target.truncate()

f=0
l=[]
author_id={}
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
		self.booktitle=""
		self.author=""
		self.editor=""

	def startElement(self,tag,attributes):
		global f
		self.CurrentData=tag
		if tag=="inproceedings":
			self.author=""
			self.editor=""
			self.booktitle=""
		#	print "inproceedings"
			f=1		
		elif tag=="proceedings":
			self.author=""
			self.editor=""
			self.booktitle=""
		#	print "proceedings"
			f=2	
		elif tag=="incollection":
			self.author=""
			self.editor=""
			self.booktitle=""
			f=3	

	def endElement(self,tag):
		global f
		global l
		#print self.CurrentData,tag
		if self.CurrentData=="author" and f==1:
			temp_str1=self.author.encode("utf8").replace('\n','')
			temp_str=temp_str1.encode("utf8").strip(' ')
			self.author=""
			if temp_str in author_id:
				l.append(author_id[temp_str])
		#	print self.author
		if self.CurrentData=="booktitle" and f==1:
			temp_str1=self.booktitle.encode("utf8").replace('\n','')
			temp_str=temp_str1.encode("utf8").strip(' ')
			self.booktitle=""
			if temp_str not in inproceedings_dict:
				if (len(l))>0:
					inproceedings_dict[temp_str]=l
			elif temp_str in inproceedings_dict:
				if len(l)>0:
					for item in l:
						inproceedings_dict[temp_str].append(item)
		if self.CurrentData=="editor" and f==2:
			temp_str1=self.editor.encode("utf8").replace('\n','')
			temp_str=temp_str1.encode("utf8").strip(' ')
			self.editor=""
			if temp_str in author_id:
				l.append(author_id[temp_str])
		#	print "ed ",self.editor
		if self.CurrentData=="booktitle" and f==2:	
			temp_str1=self.booktitle.encode("utf8").replace('\n','')
			temp_str=temp_str1.encode("utf8").strip(' ')
			self.booktitle=""
			if temp_str not in inproceedings_dict:
				if (len(l))>0:
					inproceedings_dict[temp_str]=l
			elif temp_str in inproceedings_dict:
				if len(l)>0:
					for item in l:
						inproceedings_dict[temp_str].append(item)
		if self.CurrentData=="author" and f==3:
			temp_str1=self.author.encode("utf8").replace('\n','')
			temp_str=temp_str1.encode("utf8").strip(' ')
			self.author=""
			if temp_str in author_id:
				l.append(author_id[temp_str])
		#	print self.author
		if self.CurrentData=="booktitle" and f==3:
			temp_str1=self.booktitle.encode("utf8").replace('\n','')
			temp_str=temp_str1.encode("utf8").strip(' ')
			self.booktitle=""
			if temp_str not in inproceedings_dict:
				if (len(l))>0:
					inproceedings_dict[temp_str]=l
			elif temp_str in inproceedings_dict:
				if len(l)>0:
					for item in l:
						inproceedings_dict[temp_str].append(item)		
		if tag=="inproceedings":
			f=0
			l=[]
		elif tag=="proceedings":
			f=0
			l=[]	
		elif tag=="incollection":
			f=0
			l=[]	
			#print f1


	def characters(self,content):
		if self.CurrentData=="editor" and (f==1 or f==2 or f==3):
		#if self.properTagFound==1:
			self.editor+=content
		if self.CurrentData=="booktitle" and (f==1 or f==2 or f==3):
			self.booktitle+=content
		if self.CurrentData=="author" and (f==1 or f==2 or f==3):
			self.author+=content



if ( __name__ == "__main__"):
	parser=xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	Handler=book_handler()
	parser.setContentHandler(Handler)
	parser.parse("dblp.xml")

#print dict_book

od = collections.OrderedDict(sorted(inproceedings_dict.items()))
count=0

for title in od:
	if title=='\n':
		continue
	target.write(title +" >> ")
	count=0
	for auth in od[title]:
		target.write(auth)
		count=count+1
		if count<len(od[title]):
			target.write(' | ')
		elif count==len(od[title]):
			target.write('\n')

