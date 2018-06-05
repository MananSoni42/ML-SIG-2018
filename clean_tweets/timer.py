"""
timer.py - decorator to time functions and lof them to prog_name.py
Author - Manan Soni (BITS ACM) (github: MananSoni42)
"""

import sys
import time
import logging

logging.basicConfig(filename=sys.argv[0].strip('.py')+'.log',level = logging.DEBUG,format='%(levelname)s: %(message)s')

def timer(orig_func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = orig_func(*args,**kwargs)
        t2 = time.time()
        logging.debug(f'{orig_func.__name__} ran in {round(t2-t1,2)}s')
        return result
    return wrapper

if __name__ == '__main__':
    #example use

    #no timer required
    def normal_func_1():
        print('no timer in this function')
        time.sleep(1)

    #to add timer add '@timer' before the function
    #check in timer.log file
    @timer
    def normal_func_2():
        print('added timer in this function')
        time.sleep(2)

    normal_func_1()
    normal_func_2()
