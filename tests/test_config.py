import pytest

class NotInRange(Exception):
    def __init__(self,message="Val not in range"):
        self.message=message
        super().__init__(self.message)




def test_generic():
   a=5
   with pytest.raises(NotInRange):
       if a not in range(10,20):
           raise NotInRange
       
def test_function():
    a=10/10
    with pytest.raises(ZeroDivisionError):
        if a in range(10):
            raise ZeroDivisionError