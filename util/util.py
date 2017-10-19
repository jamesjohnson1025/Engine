from os import path


def _get_location(_fName):
    return path.realpath('./')+'/Output/'+_fName+'.txt'
	        

def _save_to_file(_fName,_data):
    
    _fName = _get_location(_fName)
    
    with open(_fName,'wb') as f:
	for eRow in _data:
		pass



def _build_positional_output(_data,_fName):
    
    _fName = _get_location(_fName)
    
    _space = ' '*3

    with open(_fName,'wb') as f:
	
	for eRow in _data:
	    f.write(eRow['WORD']+_space+'(df:'+str(len(eRow['INFO'].keys()))+'):')
	    for eDoc,ePos in eRow['INFO'].iteritems():
                f.write('\n\t'+eDoc+':'+_space+'(tf:'+str(len(ePos))+')'+','.join(map(str,map(int,ePos))))
            f.write('\n')
		
def _pretty_print(_data):    
   
    print('\n Term \n \t'+_data['WORD'][0]+'\n')
    for (doc,positions) in _data['INFO'][0].iteritems():
        _positions = ','.join(map(str,map(int,positions)))
	print ('\tDocument #%s - %s'%(doc,_positions))

	
	


    






