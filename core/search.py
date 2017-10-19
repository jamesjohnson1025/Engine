from itertools import product
from collections import defaultdict
import shlex
import re

class Search(object):

    #WS -- Word Search
    #PS -- Phrase Search 
    #BS -- Boolean Search
    #PYS -- Proximity Search  

    def __init__(self,service):
                
        print('Initiating Search ....')
    	self._service = service
        self._operators = {'AND':True,'OR':True}
    
    def _parse(self,term,search_type):
        
        if search_type == 'WS':
            return self._word_search(term)
        
        elif search_type == 'BS':
            lterm,operator,rterm = shlex.split(term)	        
            return self._boolean_search(lterm,operator,rterm) 

    def _get_word(self,term):

        try:
            return self._service._fetch_record_by_word(term)
        except Exception as err:
            return False
    
    def _word_search(self,term,terminal=False):
    	
    	word = self._get_word(term)
    	if not word:
    	   print('No documents on this term %s'%(term))
           return
        return word
    
    def _boolean_search(self,lterm,operator,rterm):
     
        _tmp = lterm.split(' ') + rterm.split(' ')
        _combine = filter(re.compile(r'^\w+$').search,_tmp)
    	_records = self._service._fetch_records(_combine,'WORD')
        
        print _records

    	_bool_lphrase = self._set_status(lterm)
        _bool_rphrase = self._set_status(rterm)
        

        _phrase_ldocs = _phrase_rdocs = _lrecord = _rrecord = _result = None


        
        if _bool_lphrase and _bool_rphrase:
            _phrase_ldocs = self._phrase_search(lterm,_records) 
            _phrase_rdocs = self._phrase_search(rterm,_records)

            _result = self._common_documents(_phrase_ldocs,_phrase_rdocs)

        elif not _bool_lphrase and _bool_rphrase:
            _lrecord = self._word_search(lterm)
            _phrase_rdocs = self._phrase_search(rterm,_records)
           
            _result = self._common_documents(_lrecord[0]['INFO'],_phrase_rdocs)
        
        elif _bool_lphrase and not _bool_rphrase:

            _phrase_ldocs = self._phrase_search(lterm,_records)
            _rrecord = self._word_search(rterm)
           
            _result = self._common_documents(_phrase_ldocs,_rrecord[0]['INFO'])

        else:            
            _lrecord = self._word_search(lterm)
            _rrecord = self._word_search(rterm)

    	    _result = self._common_documents(_lrecord[0]['INFO'],_rrecord[0]['INFO'])
        
           	
    	return _result
    

    def _set_status(self,term):
        
        return True if len(term.split(' ')) > 1 else False
    

    def _phrase_search(self,phrase,records):
        
        _records = self._service._filter_custom_sframe(records,phrase.split(' '),'WORD')        
        return self._is_doc_with_phrase(_records[0],_records[1])
        
              
    def _common_documents(self,ldocs,rdocs):
       
        if type(ldocs) is dict and type(rdocs) is dict:
            _lterm = ldocs.keys()
            _rterm = rdocs.keys()           
        elif type(ldocs) is list and type(rdocs) is dict:
            _lterm = ldocs
            _rterm = rdocs.keys()
        elif type(ldocs) is dict and type(rdocs) is list:
    	    _lterm = ldocs.keys()
            _rterm = rdocs
        else:
            _lterm = ldocs
            _rterm = rdocs
        
        # Return the documents
        return set(_lterm).intersection(set(_rterm))
  
   
    def _is_doc_with_phrase(self,lrecord,rrecord,distance=1):
        
       _ldocs = lrecord['INFO']
       _rdocs = rrecord['INFO']

       _rsult_docs =  self._common_documents(_ldocs,_rdocs) 
       
       _rsult_phrase = []

       for _docIdx in _rsult_docs:
           _rsult_pharse.append(self._neighbor_terms(_ldocs[_docIdx],_rdocs[_docIdx],_docIdx,distance))          
       
       _phrase_rslt = map(lambda x: x[1],filter(lambda _match: _match[0] == True,_rsult_phrase))
       
       if len(_phrase_rslt) == 0:
           return None

       # [(True,#1),(False,#2),(False,#3)]
       return _phrase_rslt
    
    def _neighbor_terms(self,llist,rlist,docIdx,distance=1):
        
        _combinations = product(llist,rlist)

        _result = filter(lambda term: abs(term[0] - term[1]) == distance, _combinations)

        return (True if len(_result) > 0 else False,docIdx)  
    
   



