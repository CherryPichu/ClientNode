
import sqlite3


class NoConnectionError(Exception) : # Exception 을 상속받아 새로운 예외를 만듬
    """
    connection is fail 오류가 나올경우 다시 connection 연결.
    아직 이 오류가 발생한 적은 없지만, 혹시 발생할 경우를 대비해 만들어 놓고 테스트는 안함.
    """
    def __init__(self) :
        super().__init__("3의 배수가 아닙니다.")
    

class Database :
    # 싱글톤 처럼 작동.
    # https://wikidocs.net/69361

    def __new__(self, *args, **kwargs):
        
        # check_same_thread=False  다중 스레드 환경에서 DB연결을 허용.
        self.connection = sqlite3.connect("DB.db", check_same_thread=True)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __init__(self) :
        
        return self.cursor
    
    
        
   
