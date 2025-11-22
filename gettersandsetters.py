class Obj:
    def __init__(self,value):
        self.value=value
    def show(self):
        print(f"Value is {self.value}")
    @property
    def ten_value(self):
        return 10* self.value
    @ten_value.setter
    def ten_value(self,new_value):
        self.value=new_value

object=Obj(20)
print(object.value)
object.ten_value=60
object.show()