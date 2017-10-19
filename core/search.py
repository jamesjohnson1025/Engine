import shlex

class Search(object):

    #WS -- Word Search
    #PS -- Phrase Search 
    #BS -- Boolean Search
    #PYS -- Proximity Search  

    def __init__(self,_service):
        print('Initiating Search ....')
	self._service = _service
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
    	
    	word =  self._get_word(term)
    	if not word:
    	   print('No documents on this term %s'%(term))
           return
        return word
    
    def _boolean_search(self,lterm,operator,rterm):
	if not self._operators[operator]:
	   print ('### PLEASE PROVIDE VALID OPERATOR ###')
	   return

 	_lterm = shlex.split(lterm)
	_rterm = shlex.split(rterm)
	   
	_combine = _lterm + _rterm	    
	_records = self._service._fetch_records(_combine,'WORD')
        
	return _records


		
