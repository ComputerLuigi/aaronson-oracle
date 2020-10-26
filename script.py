import TM
import sys
import random

def do(a):

    from oracle import Model
    m = Model('10', 8)
    init = (TM.random_digits(20))
    initfeed = ''.join(str(e) for e in init)
    m.feed(initfeed)
    inputstr = ''.join(str(e) for e in a)
    b = []
    for x in inputstr:
        b.append(m.guess())
        m.feed(x)
    c = (zip(inputstr, b))

    d = []
    for y in c:
        if y[0] == y[1]:
            d.append(1)
        else:
            d.append(0)

##    print(zip(c, d))
    ##	print (d)
    print(d.count(1))


a = (TM.thue_morse_digits(int(sys.argv[1])))
do (a)
rs = random.sample (a, k=len(a)) 
do (rs)
do(TM.random_digits(int(sys.argv[1])))
do(TM.alternating_digits(int(sys.argv[1])))
