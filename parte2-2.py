import logging
import threading
from operaNoConm import addOne
from operaNoConm import addThree
from operaNoConm import divideTwo


addOne = threading.Thread(target = addOne,name = "sumando 1")
addThree = threading.Thread(target = addThree,name = "sumando 3")
divideTwo = threading.Thread(target = divideTwo, name = "dividiendo 2")
threads = [addThree,divideTwo,addOne]

for i in threads:
    i.start()