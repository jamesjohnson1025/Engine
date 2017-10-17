from preprocessing import Preprocessing
from service import Service
from collections import defaultdict


class Domain(object):

    def __init__(self):        
        self._service = Service()
	self._pre_processing = Preprocessing()
	self._cache_term = defaultdict(dict)	


    def _update_term(self,index,term,docId):
	if self._cache_term.get(term,False):
	    if self._cache_term[term].get(docId,False):
	        self._cache_term[term][docId].update([index])
	    else:
		self._cache_term[term][docId] = set([index]) 	
        else:
	    self._cache_term[term][docId] = set([index])

    def _add_documents_to_gl(self,docs):	
	self._service._insert_records(docs)
	return self 

    def _add_terms_to_gl(self,terms):
        terms = {'WORD':terms.keys(),'INFO':terms.values()}
	self._service._insert_records(terms)
	return self
	
    def _apply_preprocessing(self,column_name,fn):
	return self._service._apply_operation(column_name,fn)

    def _combine_SArray(self,larr,rarr):
	return zip(larr,rarr)

    def _fetch_details_by_word(self,word):
	return self._service._fetch_record_by_word(word)
   
    def _build_index(self):

	fn = lambda row:self._pre_processing._action(row)

	docs_tokenized = self._apply_preprocessing('TEXT',fn)
		
	doc_ids = self._service._fetch_column('DOCID')

	_cache = self._combine_SArray(doc_ids,docs_tokenized)
        	
   	fn = lambda term: self._update_term(term[0],term[1],docId)

	for docId,eWord in _cache:
	    map(fn,list(enumerate(eWord)))
	  	
	return self._cache_term

    def _build_positional_inverted_term(self):
	return self._service._get_sFrame_data()


		

