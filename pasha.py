import sys, math

x=int(sys.argv[1])

a = x % 19
b = x % 4
c = x % 7
d = (19 * a + 15) % 30
e = (2 * b + 4 * c + 6 * d + 6) % 7
f = d + e

if x < 0:
	print("Что-то вы перепутали")
elif x < 1900 and f <= 9:
	print("Дата:" + str(22 + f) + " марта " + str(x) + "г.")
elif x < 1900 and f > 9:
	print("Дата:" + str(f - 9) + " апреля " + str(x) + "г.")
elif x >= 1900 and f <= 26:
	print("Дата:" + str(4 + f) + " апреля " + str(x) + "г.")
elif x >= 1900 and f > 26:
	print("Дата:" + str(f - 26) + " мая " + str(x) + "г.")
