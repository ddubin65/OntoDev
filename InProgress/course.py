from rdflib import *

def spaceOut(instring):               # function to replace spaces with underscores
  return(instring.replace(" ","_"))

def is_uri(thing):                    # Boolean test if rdf term is a URI ref
  foo = URIRef('')
  return(type(thing) == type(foo))

def is_literal(thing):                # Boolean test if rdf term is an rdf literal
  foo = Literal("foo")
  return(type(thing) == type(foo))

class Description:
   def __init__(self):
      self.attribute = {}
   def setAttrib(self, attrib, value):
      if attrib in self.attribute:
        (self.attribute[attrib]).append(value)
      else:
        self.attribute[attrib] = [value]
   def getAttrib(self,attrib):
      return(self.attribute[attrib])
   def display(self):
      for key in self.attribute:
         print(key, str(self.attribute[key]))
   def __getattr__(self,name):           # This is a default method handler
        def handlerFunction(*args):
            if name in self.attribute:
               if len(args) == 0:
                    return(self.attribute[name])
               else:
                    (self.attribute[name]).append(args[0])
            else: return(False)
        return handlerFunction

class Thing(Description):
   def __init__(*args):
      self = args[0]
      Description.__init__(self)
      if len(args) > 1:
        self.attribute['iri'] = args[1]
        myobjects[args[1]] = self

class Meeting(Thing):
   def __init__(*args):
      self = args[0]
      Thing.__init__(self,args[1:len(args)])

class Unit(Thing):
   def __init__(*args):
      self = args[0]
      Thing.__init__(self,args[1:len(args)])

class Activity(Thing):
   def __init__(*args):
      self = args[0]
      Thing.__init__(self,args[1:len(args)])

class Concept(Thing):
   def __init__(*args):
      self = args[0]
      Thing.__init__(self,args[1:len(args)])

class Assignment(Thing):
   def __init__(*args):
      self = args[0]
      Thing.__init__(self,args[1:len(args)])

class Deadline(Thing):
   def __init__(*args):
      self = args[0]
      Thing.__init__(self,args[1:len(args)])

# URI scheme 
isch = Namespace("http://courseweb.ischool.illinois.edu/")

# iri to object dictionary
myobjects = {}

