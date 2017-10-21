from query import Query
from operator import Operator 

class QueryExecuter(Query):

    def __init__(self,fName,domain):
        super(QueryExecuter,self).__init__()
        self._fName = fName
        self._domain = domain
        self._query = None

    def _identify_query(self,term):
        
        term = term.strip(' ')
        
        if term[0] == '"' :
            return 'PH'
        elif term[0] == '#' :
            return 'PX'
        else:
            return 'WD'
            
    def _parse_queries(self,wCollection=None):        
        self._query = super(QueryExecuter,self)._parse(self._fName)
        
        while not self._query.isEmpty():
            _query_dict =self._query.dequeue()        
            
            print 'Query -\t',_query_dict

            if len(_query_dict.keys()) == 1:
                _type = self._identify_query(_query_dict['lterm'])
                _search_results = self._execute_query(_query_dict['lterm'],_type)
                print _search_results
            else:
                lterm = _query_dict['lterm']
                rterm = _query_dict['rterm']

                _ltresults = self._execute_query(lterm,self._identify_query(lterm))
                _rtresults = self._execute_query(rterm,self._identify_query(rterm))
                

                operators = _query_dict['operator'].split(' ')
                
                op = Operator()

                if len(operators) == 1:
                    if 'AND' in operators:
                        return op._parse(_ltresults,_rtresults)._AND()
                    elif 'OR' in operators:
                        return op._parse(_ltresults,_rtresults)._OR()

                    

                    

                print '\n\tlt\t\n',_ltresults,'\n'
                print '\n\trt\t\n',_rtresults,'\n'
                
    def _get_queries(self):
        return self._query._print_queries()

    def _execute_query(self,term,qtype,distance=1):
        
        return self._domain._doc_search(term,qtype,distance)
     


            
           
                




