# ===================================== M A I N ========================================================================
import os
from comparandum import Comparandum
from analogy import Analogy
# ======================================================================================================================

first_string = input("Enter your first comparandum: ")
second_string = input("Enter your second comparandum: ")
third_string = input("Enter your third comparandum: ")
x = Comparandum(first_string)
y = Comparandum(second_string)
z = Comparandum(third_string)
# ===================================== C O R E ========================================================================
Analogy(x, y, z)
# ======================================================================================================================
