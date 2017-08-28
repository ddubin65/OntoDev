#!/usr/bin/python
from rdflib import *
import bibtexparser
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

wlist = []  # List of sessions
sessionstart = {} # associate sessions with their starting date

for s in mygraph.subjects(RDF.type, onto.Session):
	for i in mygraph.objects(s,onto.date):
	    sessionstart[str(i)] = s
deadlines = {}
activities = {}

for d in mygraph.subjects(RDF.type, onto.Deadline):
                            sessiondue = sessiondate = duedate = dlabel = ""
                            for o in mygraph.objects(d,RDFS.label):
                                    dlabel = str(o)
                            for o in mygraph.objects(d,onto.during):
                                    sessiondue = o
                                    for p in mygraph.objects(o,onto.date):
                                        sessiondate = p
                            for o in mygraph.objects(d,onto.date):
                                    duedate = str(o)
                            if (sessiondue in deadlines.keys()):
                                deadlines[sessiondue] += ("\n- " + dlabel)
                            else:
                                deadlines[sessiondue] = ("\n- " + dlabel)
                            newdefs[duedate] = sessiondate 

for d in mygraph.subjects(RDF.type, onto.Activity):
                            sessiondue = sessiondate = duedate = dlabel = ""
                            for o in mygraph.objects(d,RDFS.label):
                                    dlabel = str(o)
                            for o in mygraph.objects(d,onto.during):
                                    sessiondue = o
                                    for p in mygraph.objects(o,onto.date):
                                        sessiondate = p
                            for o in mygraph.objects(d,onto.date):
                                    duedate = str(o)
                            if (sessiondue in activities.keys()):
                                activities[sessiondue] += ("\n- " + dlabel)
                            else:
                                activities[sessiondue] = ("\n- " + dlabel)
                            newdefs[duedate] = sessiondate 


                            
cldrfile.write("# Topic Schedule\n")

wlist = sessionstart.keys()
wlist.sort()
for d in wlist:
        myweek = weekdate = myconcept = required = background  = ''
        topics = {}
	for o in mygraph.objects(sessionstart[d], RDFS.label):
	      myweek = str(o)
	for o in mygraph.objects(sessionstart[d], onto.date):
	      weekdate = str(o)
	for s in mygraph.objects(sessionstart[d],dc.subject):
	      for p in mygraph.objects(s,skos.prefLabel):
                      myconcept = str(p)
              for q in mygraph.objects(s,onto.backgroundReading):
                      background = str(q)
              for r in mygraph.objects(s,onto.reqReading):
                      required = str(r)
              topics[myconcept] = required  
        cldrfile.write("\n")
        cldrfile.write("### " +  myweek + ": " + weekdate + ": \n")

        dstring = "#### Due today: "
        if sessionstart[d] in deadlines.keys():
                cldrfile.write(dstring + " " + deadlines[sessionstart[d]] + "\n")
                cldrfile.write("\n")
        astring = "#### In class: "
        if sessionstart[d] in activities.keys():
                cldrfile.write(astring + " " + activities[sessionstart[d]] + "\n")
                cldrfile.write("\n")
        bstring = "**Further Background:** "
        if background:
          cldrfile.write(bstring + " " + background + "\n")
          cldrfile.write("\n")

        
        for t in topics.keys():
            cldrfile.write("### " + t + "\n")
            rstring = "\n"
            if required:
              cldrfile.write(rstring)
              cldrfile.write("\n")
              bibfile = topics[t][5:] + '.md'
              with open(bibfile, 'r') as md_file:
                  md_str = md_file.read()
                  cldrfile.write(md_str)

if newdefs:
        for k in newdefs.keys():
                defsfile.write("define(" + k + ", " + newdefs[k] + ")dnl\n")

          
cldrfile.close()
defsfile.close()
