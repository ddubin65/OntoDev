An introduction to knowledge representation and information management
for distributed deductive information systems. Covers domain analysis,
the design of description logic based models, vocabulary integration,
and current standards for linked data encoding and communication.

<https://tinyurl.com/datalibrarian>
<https://tinyurl.com/linkedDataScientist>

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
 