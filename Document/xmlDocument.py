#from document import Document
from xml.etree.ElementTree import parse
from os import path


class XmlDocument(object):

    def __init__(self):
        self._fileName = None

    def _throwErrIfNotFileExist(self,fName):

        try:

            fileName = path.realpath('..')+'/Input/'+fName

            if(not path.isfile(fileName) or not path.exists(fileName)):
                raise IOError('### PLEASE PROVIDE A VALID FILE NAME')

            return True

        except Exception as err:

            print('### ERROR - %s.' % (err))
            return

    def parse(self,fName):

        if(self._throwErrIfNotFileExist(fName)):
            print('Reading File')



if __name__ == '__main__':
    XmlDocument().parse('data.xml')


