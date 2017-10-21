from os import path
from preprocessing import Preprocessing as pw

class RankExecuter(object):

    def __init__(self,domain):
        self._fileName = None
        self._domain = domain
        self._preprocess = pw()
    
    def _throwErrIfNotFileExists(self,fName):

        try:
            fileName = self._getfLocation(fName)
            if(not path.isfile(fileName) or not path.exists(fileName)):
                raise IOError('### PLEASE PROVIDE A VALID FILE NAME')
                
            self._fileName = fileName
            
            return True
        
        except Exception as err:

            print('### ERROR - %s.'%(err))
            return 

    def _getfLocation(self,fName):
        return path.realpath('./')+'/Input/'+fName+'.txt'

    def _parse(self,fName):
        if(self._throwErrIfNotFileExists(fName)):
            
            fn = lambda x : x.strip('\r\n')
            with open(self._fileName,'r') as g:
                queries = map(fn,[line.split(' ',1)[1] for line in g])
        
            for query in queries:
                row = self._preprocess._action(query)
                self._execute_query(row)
            

    def _execute_query(self,query):

        query = map(str,query)
        
        records = self._domain._fetch_records(query,'WORD')

        docs  = set()

        records_size = len(records)

        [docs.update(records[i]['INFO'].keys()) for i in range(records_size)]

        print docs

     

'''
if __name__ == '__main__':

   

    print rk._parse('queries.ranked')
'''
