import logging
import threading
from operaNoConm import addOne
from operaNoConm import addThree
from operaNoConm import divideTwo


addOne = threading.Thread(target = addOne,name = "T1")
addThree = threading.Thread(target = addThree,name= "T2")
divide1 = threading.Thread(target = divideTwo, name="T3")
divide2 = threading.Thread(target = divideTwo,name="T4")
threads = [addThree,divide1,addOne,divide2]

for i in threads:
    i.start()
