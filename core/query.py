from os import path
from nltk.stem import PorterStemmer as ps
import shlex


class Query(object):

    def __init__(self):
        self._stack = []

    def isEmpty(self):
        return (self._stack == [])

    def enqueue(self,item):
        self._stack.insert(0,item)

    def dequeue(self):
        return self._stack.pop()
   
    def size(self):
        return len(self._stack)
    
    def _print_queries(self):
        return self._stack

    def _get_location(self,fName):

        return path.realpath('./')+'/Input/'+fName+'.txt'
    
    def _throwErrIfNotFileExist(self,fName):

        try:

            fileName = self._get_location(fName)
            if(not path.isfile(fileName) or not path.exists(fileName)):
                raise IOError('### PLEASE PROVIDE A VALID FILE NAME')
            return True
        except Exception as err:
            print('### ERROR - %s.' % (err))
            return
   

    def _parse(self,fName):

        if(self._throwErrIfNotFileExist(fName)):
            
            _fName = self._get_location(fName)
            
            _queries = None

            with open(_fName,'r') as f:
                _queries = [line[2:] for line in f]

            self._process_query(_queries)

            return self

     
    def _process_query(self,queries):
        
        _queries = []
        
        if queries is not None:
            _queries = map(lambda x:x.rstrip('\r\n').strip(' '),queries)
        
        for query in _queries:
            self._make_query(query)

    def _is_query_NOT(self,)

        
    def _make_query(self,query):
        _ps = ps()
        sub_queries = shlex.split(query)
        if 'AND' in sub_queries:       
            fn = lambda word:word.lower()
            _query = map(fn,query.split('AND',1))
            self.enqueue({'lterm' :_query[0],'operator' :'AND','rterm' :_query[1]})
            #if 'NOT' in sub_queries:
            #    _query = map(fn,query.split('AND NOT',1))

            #    self.enqueue({'lterm' :_query[0],'operator' :'AND NOT','rterm' :_query[1]})
            #else:
        elif query[0] == '#' and 'AND' not in sub_queries:
            self.enqueue({'lterm' :'"'+sub_queries[0]+'"'})
        elif len(sub_queries) == 1:
            fn = lambda word:word.lower()
            sub_queries = map(fn,sub_queries)
            self.enqueue({'lterm' :'"'+sub_queries[0]+'"'})
            
