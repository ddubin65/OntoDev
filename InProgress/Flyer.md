# IS590-OD Ontology Development

## What will I learn in IS590-OD?

IS590-OD is an introduction to knowledge representation and
information management for distributed deductive information
systems. You'll learn analysis principles and metadata encoding
standards that allow linked application data to be distributed over
the Internet under the stewardship of cooperating stakeholders.

## Will the skills and knowledge covered in IS590-OD help me get a job? 

In ten years the IS590-OD course material will be mainstream
information systems design competencies that every information
professional will need to understand. For now job ads looking
for these skills use key words like "linked data" and "semantic web."
The two links below will show you recent examples of companies advertising
for people who know ontology development.

- <https://tinyurl.com/datalibrarian>
- <https://tinyurl.com/linkedDataScientist>

## What specific technologies are taught in IS590-OD?

1. The RDF-based OWL 2 DL Web Ontology Language including differences
   among the RL, QL, and EL profiles.
2. The Datalog declarative logic programming language. We'll use the
   [DES interpreter](http://des.sourceforge.net/) for our Datalog exercises.
3. The [Protégé ontology editor](https://protege.stanford.edu/) and
   the [HermiT](http://www.hermit-reasoner.com/) description logic
   reasoner.
4. One or more URL redirection methods appropriate to the current
   semester's project hosting requirements.

## How is ontology development different from relational database design?

Relational database management systems are suitable for applications
where all the data is under one organization's control and schemas can
be tightly coupled to that organization's specific needs. That was
true of most information management applications in the past, but
becomes less true every year. Looking forward, most digital
information management will be coordinated across institutional
boundaries, with responsibilities distributed among many cooperating
stakeholders. That calls for more powerful and more flexible data
definition and querying models than those offered by relational systems.

## How is ontology development different than other kinds of metadata encoding and taxonomy design?

Metadata descriptions have traditionally been assertions of facts
about resources in some kind of collection. They've typically been
expected to serve as "grist" for an information processing mill
controlled by programmers and software engineers. Ontology languages
like OWL let us encode the *meaning* of metadata and the rules
that govern its processing using robust and neutral forms of expression.
That enables information systems to be made more reliable and their data
kept under the control of users instead of programmers.


Students should see Ontology Development as followup or next step to
courses like Information Modeling, Metadata in Theory and Practice, or
Introduction to Databases. Any of those would be a good preparation,
and although no one of them is strictly necessary, I'd strongly
recommend having at least one of them first. IS561 would be the best
preparation, but I think students required to take that class may have
the least interest in going further.

I see inference and deduction as absolutely essential for very prosaic
information management problems like maintaining record consistency,
tracking data provenance, and coordinating cooperation among human
stakeholder communities:

- In the past information systems were driven by isolated data silos,
  but today's databases need to be distributed over very loosely
  coupled networks of machines and organizations.
- In the past it sufficed to conclude an answer of "no" if your system
  found no records that matched a query---no matching records meant no
  such records. But today we work under an Open World assumption: just
  because I can't retrieve a yes doesn't mean the answer is no.
- In the past I could design my database to meet very current and
  local requirements; if the schema works for our needs in 2009 I'll
  let some poor bastard (possibly my future self) inherit the problem
  of adapting it to our needs in 2019. These days cooperation across
  institutional boundaries demands that we consider data integration
  and synthesis from the very start, even if we lack the foresight to
  plan for our own uncertain futures.
- In the past we could be confident that the relational model was an
  adequate basis for data quality monitoring and data integrity
  enforcement. That confidence is no longer justified and we need more
  help keeping our records consistent and correct.
 