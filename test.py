from threading import Thread
import time

class ConstantPrint(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while 1:
            print "PRINT"
            
def main():
    cp = ConstantPrint()
    cp.start()
    while 1:
        print "ok"
        
main()

            
