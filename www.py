#!/usr/bin/python
import xml.sax
import sys
import collections
i=0
dict_author={}
target=open("om.txt",'w')
target.truncate()
f1=0
f2=0
class authors_handler(xml.sax.ContentHandler):
#target=open("a.txt",'w')
#target.truncate()
#	dict_author={}
	def __init__(self):
		self.CurrentData=""
		self.author=""


	def startElement(self,tag,attributes):
		global i 
#print i
		global f1
		global f2
		self.CurrentData=tag
		if tag=="www":
#			print "in www:"
#	print i
			#key=attributes["mdate"]
			key1="mdate"
			key2="key"
			if key1 and key2 in attributes:
				f1=1	
				#self.properTagFound=1
				i=i+1
				#print "inside"
				#print f1	
				#print "mdate:",attributes[key]
		if tag=="author":
				f2=1		

	def endElement(self,tag):
		global i
		global target
		global f1
		global f2 
		#print self.CurrentData,tag
		if self.CurrentData=="author":
#print "author:",self.author
			#print f1, f2
			if f1*f2==1:
				dict_author[self.author]=i
				
			f2=0
		elif tag=="www":
			f1=0	
			#print f1


	def characters(self,content):
		if self.CurrentData=="author":
		#if self.properTagFound==1:
			self.author=content



if ( __name__ == "__main__"):
	parser=xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	Handler=authors_handler()
	parser.setContentHandler(Handler)
	parser.parse("dblp.xml")

od = collections.OrderedDict(sorted(dict_author.items()))

for key in od:
		target.write(key+ " " + str(od[key])+"\n")
#print dict_author	
		
