#!/usr/bin/python
import xml.sax
import sys
import collections
f=0
author_title={}
school_author_title={}
target=open("phd_masters1.txt",'w')
target1=open("temp.txt",'w')
target1.truncate()
temp_author=""
temp_title=""
target.truncate()

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
			f=1
			#key=attributes["mdate"]
			
		

	def endElement(self,tag):
		global f
		global temp_author
		global temp_title
		if self.CurrentData=="author" and f==1:
			temp_author=self.author
			#author_title[self.author]=""
		if self.CurrentData=="title" and f==1:
			temp_title=self.title
			#author_title[self.author]=self.title
		if self.CurrentData=="school" and f==1:
			if self.school not in school_author_title:
				school_author_title[self.school]={}
				#if temp_author=='Daniel F. Lieuwen':
					#print "school is",self.school
			if self.school in school_author_title:
				school_author_title[self.school][temp_author]=temp_title
				#if temp_author=='Daniel F. Lieuwen':
					#print 'school all',self.school
		if tag=="phdthesis"	or tag=="mastersthesis":
			f=0	
			

	def characters(self,content):
		if self.CurrentData=="author":
		#if self.properTagFound==1:
			self.author=content
		if self.CurrentData=="title":
			self.title=content
		if self.CurrentData=="school":
			self.school=content



if ( __name__ == "__main__"):
	parser=xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	Handler=authors_handler()
	parser.setContentHandler(Handler)
	parser.parse("dblp.xml")

#print school_author_title
od = collections.OrderedDict(sorted(school_author_title.items()))
count=0
for school in od:
		for auth in od[school]:
			if school=='\n':
				continue
			target1.write("school:::"+school)
			target.write(school+":"+ (auth)+":"+ str(od[school][auth])+'\n')