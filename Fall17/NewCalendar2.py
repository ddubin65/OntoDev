#!/usr/bin/python3
from rdflib import *
# import bibtexparser
import sys
import re

ttlfilename = str(sys.argv[1])

project = ""
newdefs = {}
regex1 = re.compile(r"([^.]+)\.ttl")
mymatch = re.search(regex1,ttlfilename)
if mymatch:
   project = mymatch.group(1)

if project:
   cldrfilename = project + ".cldr"
   cldrfile = open(cldrfilename,"w")
   defsfilename = project + ".defs"
   defsfile = open(defsfilename,"w")

onto = Namespace("http://courseweb.ischool.illinois.edu/lis/2017fa/is590od/")
event = Namespace("http://purl.org/NET/c4dm/event.owl#")
tl = Namespace("http://purl.org/NET/c4dm/timeline.owl#")
dc = Namespace("http://purl.org/dc/terms/")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")

mygraph = ConjunctiveGraph()
mygraph.parse(ttlfilename,format="n3")

wlist = []  # List of weeks
weekstart = {} # associate weeks with their starting date

for s in mygraph.subjects(RDF.type, onto.Week):
  for i in mygraph.objects(s,event.time):
    for a in mygraph.objects(i,tl.at):
       weekstart[str(a)] = s
deadlines = {}

for d in mygraph.subjects(RDF.type, onto.Deadline):
                            weekdue = duedate = adue = dlabel = alabel = ""
                            for o in mygraph.objects(d,RDFS.label):
                                    dlabel = str(o)
                            for o in mygraph.objects(d,onto.dueDuring):
                                    weekdue = o
                            for o in mygraph.objects(d,onto.dueDate):
                                    duedate = str(o)
                            for a in mygraph.subjects(onto.hasDeadline,d):
                                    for o in mygraph.objects(a,RDFS.label):
                                            alabel = str(o)
                                    for o in mygraph.objects(a,onto.dueDate):
                                            adue = str(o)
                            if (weekdue in deadlines.keys()):
                                    deadlines[weekdue] += "**Due:** " + dlabel + ", " + alabel + "\n\n"
                            else:
                                    deadlines[weekdue] = "**Due:** " + dlabel + ", " + alabel + "\n\n"
                            newdefs[adue] = duedate
                            
cldrfile.write("# Topic Schedule\n")

wlist = list(weekstart.keys())
wlist.sort()

for d in wlist:
   myweek = myconcept = required = background  = ''
   for o in mygraph.objects(weekstart[d], skos.prefLabel):
      myweek = str(o)
   for o in mygraph.objects(weekstart[d], onto.date):
      weekdate = str(o)
   cldrfile.write("\n")
   cldrfile.write("### " +  myweek + ": " + weekdate + "\n")
   for s in mygraph.objects(weekstart[d],dc.subject):
      for p in mygraph.objects(s,skos.prefLabel):
                      myconcept = str(p)
                      for q in mygraph.objects(s,onto.backgroundReading):
                              background = str(q)
                      for r in mygraph.objects(s,onto.reqReading):
                              required = str(r)
      cldrfile.write("- " + myconcept + "\n")  
      rstring = "    - **Required Readings:** "
      if required:
        cldrfile.write(rstring + " " + required + "\n")
        cldrfile.write("\n")
      dstring = ""
      if weekstart[d] in deadlines.keys():
        cldrfile.write(dstring + " " + deadlines[weekstart[d]] + "\n")
        cldrfile.write("\n")
      bstring = "    - **Further Background:** "
      if background:
        cldrfile.write(bstring + " " + background + "\n")
        cldrfile.write("\n")
      myconcept = background = required = ''

if newdefs:
        for k in newdefs.keys():
                defsfile.write("define(" + k + ", " + newdefs[k] + ")dnl\n")

          
cldrfile.close()
defsfile.close()
