from xmlDocument import XmlDocument

class Document(object):

    def __init__(self,filename,instance = 'XML',):
        self._instances = None
        self._fileName = filename

    def _registerInstances(self):
        self._instances = dict(XML = XmlDocument()

    def parse(self,documentType='XML'):




