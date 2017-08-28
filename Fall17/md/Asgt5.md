	<subtl>OWL Revision 1: Restrictions and inference</subtl>
      <p>This assignment is due &asgt5due;. 
<![ %HTML; [(<weblink url="&homework;&as5;">upload link</weblink>)]]>
</p> 
	<p>In the last assignment you defined individual instances as
part of your vocabulary to illustrate your property and class
definitions. For this assignment, propose an information management
strategy for your vocabulary that distinguishes between facts that
should be asserted and facts that should be deduced. For example, in
the current GSLIS ontology facts concerning job appointments are
asserted (appointee, appointing organization, job title), but status
as a GSLIS faculty member is deduced. Prepare and submit a written
explanation of your strategy. It should be between one half page and
one page in length.</p>
	<p>Revise your vocabulary and your instance illustrations so
that when facts are asserted in accordance with your strategy, the
appropriate deduced facts are entailed by your class and property
definitions (just as with the illustrations included in gslis.ttl). I
will confirm the deductions using the Hermit plugin that accompanies
our Protege installation.</p>

<p>At least one of your class definitions should employ either
an owl:allValuesFrom (&Text2;, page 227) or an owl:someValuesFrom
(&Text2;, page 225) restriction. The remaining deductions can be
accomplished via as many or as few of the following as you wish:</p>
	<itemize>
	  <item><tt>owl:allValuesFrom</tt></item>
	  <item><tt>owl:someValuesFrom</tt></item>
	  <item><tt>owl:hasValue</tt></item>
	  <item><tt>rdfs:subClassOf</tt></item>
	  <item><tt>rdfs:subPropertyOf</tt></item>
	  <item><tt>owl:inverseOf</tt></item>
	  <item><tt>rdfs:range</tt></item>
	  <item><tt>rdfs:domain</tt></item>
	</itemize>

Post an announcement of your revision to the discussion
forum, and submit a copy of the revised vocabulary. The same validity
and linked data requirements apply as with Assignment 4: URIs for
entities in your schema should resolve to the URL for your
vocabulary's RDF, but you need not provide an html counterpart for
humans. One additional requirement is that in addition to being
syntactically valid, your vocabulary must be logically consistent.
That is to say, your declarations should not cause the reasoner
to report that your model is inconsistent.
