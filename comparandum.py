from alpha import Alpha
#===================================== C L A S S 1/2 ==================================================================
class Comparandum():
    print("Hello and welcome to kaPYcat")
    print("I will ask for three string comparanda and will try to meow the fourth one, such that x : y :: z : [meow]")
    def __init__(self, char):
        # fin = len(char) - 1
        # ifin = alpha.index(char[fin])
        self.char = char
        if len(char) == 1:
            self.i1 = Alpha.index(char[0])
        elif len(char) == 2:
            self.i1 = Alpha.index(char[0])
            self.i2 = Alpha.index(char[1])
        elif len(char) == 3:
            self.i1 = Alpha.index(char[0])
            self.i2 = Alpha.index(char[1])
            self.i3 = Alpha.index(char[2])
        else:
            KeyError
            print("Error.")

    def __len__(self):
        return len(self.char)
#======================================================================================================================
