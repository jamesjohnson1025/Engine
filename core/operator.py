

class Operator(object):


    def __init__(self):
        self._lcollection = None
        self._rcollection = None

    def _parse(self,lcollection,rcollection):

        if type(lcollection) is list and type(rcollection) is dict:
            
            self._lcollection = lcollection
            self._rcollection = rcollection[0]['INFO'].keys()

        elif type(lcollection) is dict and type(rcollection) is list:

           self._lcollection = lcollection[0]['INFO'].keys()
           self._rcollection = rcollection
            
        elif type(lcollection) is list and type(rcollection) is list:

            self._lcollection = lcollection
            self._rcollection = rcollection
        
        elif type(lcollection) is dict and type(lcollection) is dict:
            
            self._lcollection = lcollection[0]['INFO'].keys()
            self._rcollection = rcollection[0]['INFO'].keys()
        
        return self

    
    def _AND(self):

        return set(self._lcollection).intersection(set(self._rcollection))

    def _OR(self):

        return set(self._lcollection) | set(self._rcollection)

    def _NOT(self):

        return set(self._lcollection) - set(self._rcollection)










