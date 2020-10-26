from oracle import Model
import TM
m = Model('10', 5)
a = TM.thue_morse_digits(100)
inputstr = ''.join(str(e) for e in a)
m.feed(inputstr)
print (m.guess())


