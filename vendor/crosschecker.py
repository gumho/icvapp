import random

class CrossChecker():
    """The CrossChecker module is a temporary stub for the CodeRyte icd-cpt crosschecker module."""
    
    def checkPair(self, icd, cpt):
        """Takes an icd9 code and a cpt code and checks whether they are 'compatible'. Returns
        True if the code pair is correctly coded, False if not.
        
        In an attempt to simulate the behaviour of checking code pairs with the real CodeRyte 
        crosschecker, this method, on a basic level, checks whether a pair is correctly coded or 
        not. We are only interested in a boolean result. Here, we have hard-coded the checking 
        behaviour to report one incorrect code pair for every three pairs"""
        
        # supposed 1/10 fail rate
        # if random.randrange(1,11) % 10 == 0:
        #     return False
        
        # if icd contains a 0, fail it.
        # use this method for more stable control over
        # fail/pass outcomes. less chaos this way.
        if icd.find('0') != -1:
            return False
        else:
            return True

if __name__ == '__main__':
    t = 0
    f = 0
    
    for i in range(1,20):
        if CrossChecker().checkPair('a', 'k') is True:
            t += 1
        else:
            f += 1
            
    print "True: %d, False: %d" % (t,f)
            