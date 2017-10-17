from core.domain import Domain
from document.Document  import Document 
from util.util import _build_positional_output

main = Domain()
doc = Document()

docs = doc._registerInstances()._getInstance('XML').parse('data2.xml')

main_service =  main._add_documents_to_gl(docs)

_db = main_service._build_index()

pos_main = Domain()

domain_terms = pos_main._add_terms_to_gl(_db)

termInverted = domain_terms._build_positional_inverted_term()

_build_positional_output(termInverted,'Inverted')




