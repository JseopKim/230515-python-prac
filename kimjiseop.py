import math

def exampleOne(a):
    if type(a) == int:
          if(a - int(a) != 0):
               raise ValueError("정수를 입력해야 합니다.")
    else:
        raise ValueError("정수를 입력해야 합니다.")  
    return a
           
           
try:
    print(exampleOne(23.4))
except ValueError as e:
     print(e)