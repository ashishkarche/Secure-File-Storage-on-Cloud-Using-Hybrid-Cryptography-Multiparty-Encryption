import os
from dataProcessing import *
from Threads import *

def EncryptInput():
	Segment()
	gatherInfo()
	HybridCrypt()
        
def main():
    EncryptInput()
    #DecryptMessage()
    
if __name__=="__main__":
    main()

