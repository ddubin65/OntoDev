# Assignment 5: OWL Revision 1, restrictions and inference

This assignment is due ASGT5DUE. 

In the last assignment you defined individual instances as part of
your vocabulary to illustrate your property and class definitions. For
this assignment, propose an information management strategy for your
vocabulary that distinguishes between facts that should be asserted
and facts that should be deduced.  Prepare and submit a written
explanation of your strategy. It should be between one half page and
one page in length.

Revise your vocabulary and your instance illustrations so that when
facts are asserted in accordance with your strategy, the appropriate
deduced facts are entailed by your class and property
definitions. Confirm the deductions using the Hermit plugin that
accompanies our Protege installation.

At least one of your class definitions should employ either an
owl:allValuesFrom or an owl:someValuesFrom restriction. The remaining
deductions can be accomplished via as many or as few of the following
as you wish:

- owl:allValuesFrom
- owl:someValuesFrom
- owl:hasValue
- rdfs:subClassOf
- rdfs:subPropertyOf
- owl:inverseOf
- rdfs:range
- rdfs:domain

Post an announcement of your revision to the discussion
forum, and submit a copy of the revised vocabulary. The same validity
and linked data requirements apply as with Assignment 4: URIs for
entities in your schema should resolve to the URL for your
vocabulary's RDF, but you need not provide an html counterpart for
humans. One additional requirement is that in addition to being
syntactically valid, your vocabulary must be logically consistent.
That is to say, your declarations should not cause the reasoner
to report that your model is inconsistent.

