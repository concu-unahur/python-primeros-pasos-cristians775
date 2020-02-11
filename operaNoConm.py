import threading
from threading import Lock
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
lock = Lock()
num = 0

def addOne():
    global num
    lock.acquire()
    logging.info(f'num vale = {num}')
    logging.info('Sumando uno')
    num+= 1
    logging.info(f'num vale = {num}')
    lock.release()

def addThree():
    global num
    lock.acquire()
    logging.info(f'num vale = {num}')
    logging.info('Sumando 3')
    num+= 3
    logging.info(f'num vale = {num}')
    lock.release()

def divideTwo():
    global num
    lock.acquire()
    logging.info(f'num vale = {num}')
    logging.info('Dividiendo por dos')
    num /= 2
    logging.info(f'num vale = {num}')
    lock.release()

