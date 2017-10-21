from core.domain import Domain
from core.queryexecuter import QueryExecuter
from document.Document  import Document 
from util.util import _build_positional_output,_pretty_print

main = Domain()


doc = Document()

docs = doc._registerInstances()._getInstance('XML').parse('data4.xml')

main_service =  main._add_documents_to_gl(docs)

_db = main_service._build_index()

pos_main = Domain()

pos_main._add_terms_to_gl(_db)

termInverted = pos_main._build_positional_inverted_term()

#_build_positional_output(termInverted,'Inverted')

#print pos_main._doc_search('middl','WD',1)


#print main._doc_details(3826)


qy = QueryExecuter('queries.boolean',pos_main)

queries = qy._parse_queries()

#print qy._get_queries()




