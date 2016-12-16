
class Alpha(object):
    #===================================== A L P H A B E T =====================================================
    alpha = ["•", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                 "t", "u", "v", "w", "x", "y", "z"]
    #===========================================================================================================
    @classmethod
    def index(cls,val):
        return cls.alpha.index(val)

    @classmethod
    def get(cls,pos):
        return cls.alpha[pos]

    @classmethod
    def len(cls):
        return len(cls.alpha)
