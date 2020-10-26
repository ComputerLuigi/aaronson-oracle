from oracle import Model
import TM
m = Model('10', 5)
a = TM.thue_morse_digits(1000)
inputstr = ''.join(str(e) for e in a)
b = []
for x in inputstr:
	m.feed(x)
	b.append(m.guess())
c = (zip(inputstr,b))

d = []
for y in c:
	if y[0] == y[1]:
		d.append(1)
	else:
		d.append(0)


print (zip (c,d))

print (d.count(1))
