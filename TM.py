import sys


def thue_morse_digits(digits):
    return [bin(n).count('1') % 2 for n in range(digits)]


def alternating_digits(digits):
    return [n % 2 for n in range(digits)]


def ListXOR(l1, l2):
    x = []
    for n in range(len(l1)):
        x.append(int((l1[n] != l2[n])))
    return x


a = thue_morse_digits(int(sys.argv[1]))
