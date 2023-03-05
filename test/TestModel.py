import sys, os
#https://freedata.tistory.com/70
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models import model


def debug():
    db = model.Database()    
    print( db.__dir__() )
    
    
    return 1

debug()


