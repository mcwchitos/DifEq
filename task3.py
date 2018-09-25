import math


def first(x, y):
    try:
        return 2 * x ** 2 + 3 * y ** 2 - 2
    except OverflowError:
        return float('inf')


def second(x, y):
    try:
        return y + math.sqrt(x ** 2 + y ** 2)
    except OverflowError:
        return float('inf')


def third(x, y):
    try:
        return x ** 2 - 3 * x * y + y ** 2 - 3 * y
    except OverflowError:
        float('inf')

def forth(x, y):
    try:
        return (1 + x) / (1 - y ** 2)
    except OverflowError:
        float('inf')


h = 0.05
x = []
y = []
x.append(2)
y.append(1)
x.append(0)
y.append(1)
x.append(0)
y.append(2)
x.append(2)
y.append(3)


x1Arr = []
y1Arr = []
x2Arr = []
y2Arr = []
x3Arr = []
y3Arr = []
x4Arr = []
y4Arr = []

for i in range(int(1 / h + 1)):
    x1Arr.append(x[0] + i * h)
    x2Arr.append(x[1] + i * h)
    x3Arr.append(x[2] + i * h)
    x4Arr.append(x[3] + i * h)
    if i == 0:
        y1Arr.append(y[0])
        y2Arr.append(y[1])
        y3Arr.append(y[2])
        y4Arr.append(y[3])
    else:
        y1Arr.append(y1Arr[i - 1] + h * first(x1Arr[i - 1], y1Arr[i - 1]))
        y2Arr.append(y2Arr[i - 1] + h * second(x2Arr[i - 1], y2Arr[i - 1]))
        y3Arr.append(y3Arr[i - 1] + h * third(x3Arr[i - 1], y3Arr[i - 1]))
        y4Arr.append(y4Arr[i - 1] + h * forth(x4Arr[i - 1], y4Arr[i - 1]))
print("First equation")
for i in range(len(x1Arr)):
    print(str(i + 1) + "th try: " + str(round(x1Arr[i], 2)) + " " + str(round(y1Arr[i], 6)))
print("Second equation")
for i in range(len(x2Arr)):
    print(str(i + 1) + "th try: " + str(round(x2Arr[i], 2)) + " " + str(round(y2Arr[i], 6)))
print("Third equation")
for i in range(len(x3Arr)):
    print(str(i + 1) + "th try: " + str(round(x3Arr[i], 2)) + " " + str(round(y3Arr[i], 6)))
print("Forth equation")
for i in range(len(x4Arr)):
    print(str(i + 1) + "th try: " + str(round(x4Arr[i], 2)) + " " + str(round(y4Arr[i], 6)))