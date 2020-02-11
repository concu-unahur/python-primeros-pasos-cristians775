import requests
import time
import logging
import threading
from operaNoConm import addOne
from operaNoConm import addThree
from operaNoConm import divideTwo


addOne = threading.Thread(target=addOne)
addThree = threading.Thread(target=addThree)

threads = [addThree, addOne]

for i in threads:
    i.start()