#!/usr/bin/python
import xml.sax
import sys
import collections
f=0
author_title={}
school_author_title={}
target=open("phd_masters1.txt",'w')
#target1=open("temp.txt",'w')
#target1.truncate()
temp_author=""
temp_title=""
target.truncate()
author_id={}
with open("www_parse.txt") as f:
	content = f.readlines()
for row in content:
	temp = row.split("#")
	temp[1] = temp[1].replace("\n", "")
	author_id[temp[0]] = temp[1]


class authors_handler(xml.sax.ContentHandler):
#target=open("a.txt",'w')
#target.truncate()
#	dict_author={}
	def __init__(self):
		self.CurrentData=""
		self.author=""
		self.title=""
		self.school=""


	def startElement(self,tag,attributes):
		global f 
#print i
		
		self.CurrentData=tag
		if tag=="phdthesis" or tag=="mastersthesis":
			self.author=""
			self.title=""
			self.school=""
			f=1
			#key=attributes["mdate"]
			
		

	def endElement(self,tag):
		global f
		global temp_author
		global temp_title
		if self.CurrentData=="author" and f==1:
			#temp_author=self.author
			temp_str1=self.author.encode("utf8").replace('\n','')
			self.author = ""
			temp_author=temp_str1.encode("utf8").strip(' ')
			#author_title[self.author]=""
		if self.CurrentData=="title" and f==1:
			#temp_title=self.title
			temp_str1=self.title.encode("utf8").replace('\n','')
			self.title = ""
			temp_title=temp_str1.encode("utf8").strip(' ')
			#author_title[self.author]=self.title
		if self.CurrentData=="school" and f==1:
			temp_str1=self.school.encode("utf8").replace('\n','')
			self.school = ""
			temp_str=temp_str1.encode("utf8").strip(' ')
			if temp_str not in school_author_title:
				school_author_title[temp_str]={}
				#if temp_author=='Daniel F. Lieuwen':
					#print "school is",self.school
			if temp_str in school_author_title:
				school_author_title[temp_str][author_id[temp_author]]=temp_title
				#if temp_author=='Daniel F. Lieuwen':
					#print 'school all',self.school
		if tag=="phdthesis"	or tag=="mastersthesis":
			f=0	
			self.author=""
			self.title=""
			self.school=""
			

	def characters(self,content):
		global f
		if self.CurrentData=="author" and f==1:
		#if self.properTagFound==1:
			self.author+=content
		if self.CurrentData=="title" and f==1:
			self.title+=content
		if self.CurrentData=="school" and f==1:
			self.school+=content



if ( __name__ == "__main__"):
	parser=xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	Handler=authors_handler()
	parser.setContentHandler(Handler)
	parser.parse("dblp.xml")

#print school_author_title
od = collections.OrderedDict(sorted(school_author_title.items()))
count=0
print "writting"
for school in od:
	if len(school)==0:
		continue;
	for auth in od[school]:
		target.write(school+" # "+ (auth)+" | "+ str(od[school][auth])+'\n')