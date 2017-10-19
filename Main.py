from core.domain import Domain
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

_build_positional_output(termInverted,'Inverted')

#_pretty_print(pos_main._doc_search('scotland','WS'))

print pos_main._doc_search('edinburgh and scotland','BS')

#print main._doc_details(3826)




