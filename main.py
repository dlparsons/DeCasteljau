import matplotlib.pyplot as plt

cols = 2  # No matter the number of points, there is always just an x and y

# Retrieve nCr and fact code from GeeksforGeeks
def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))


def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


# Get r (x,y) points
def getpoints(r):
    p = [[0 for i in range(cols)] for j in range(r)]
    for n in range(r):
        p[n][0], p[n][1] = [float(x) for x in
                            input("Enter the values x and y for Point P" + str(n) + " separated by a space: ").split()]
    return p


# Append some set to separate the x's from the y's
def appendfunc(set):
    theX = []
    theY = []
    for n in range(len(set)):
        theX.append(set[n][0])
        theY.append(set[n][1])
    return theX, theY


# For any number of points, find "it" amount of between points to form the bezier curve
def decasteljau(p, it):
    b = [[0.0 for h in range(2)] for j in range(it)]
    n = len(p)
    for i in range(it):
        t = i / (it - 1)
        tempN = n
        for r in range(n):
            coeff = nCr(n-1, r)
            b[i][0] = b[i][0] + (coeff * ((1 - t) ** (tempN-1)) * (t ** r) * p[r][0])
            b[i][1] = b[i][1] + (coeff * ((1 - t) ** (tempN-1)) * (t ** r) * p[r][1])
            tempN -= 1
    return b


# Problem 1
rows = 3  # Determines how many points there are
iterations = 51  # Determines how many iterations are used

point = getpoints(rows)
# Finds the Bezier of the original order
px, py = appendfunc(point)  # Original Points for graphing
bezier = decasteljau(point, iterations)

# Reorders points from least to greatest of x axis, and finds bezier that way instead
point.sort()
opx, opy = appendfunc(point)  # Ordered Points for Graphing
orderedBezier = decasteljau(point, iterations)

x, y = appendfunc(bezier)
ox, oy = appendfunc(orderedBezier)

# Graphing two different plots, one for the original order of the points
# and another for the reordered points from least point of x to greatest point of x
fig, (sub1, sub2) = plt.subplots(1, 2)
fig.suptitle('Bezier Curves')
sub1.plot(x, y, marker='o', color='blue')
sub1.plot(px, py, 'ro-', marker='x', color='red')
sub1.set_title('Original Point Order')
sub2.plot(ox, oy, marker='o', color='blue')
sub2.plot(opx, opy, 'ro-', marker='x', color='red')
sub2.set_title('Ordered Point Order')
plt.show()

# Problem 2
rows = 4  # 4 rows with an X and Y column
iterations = 51
point = [[0 for i in range(cols)] for j in range(rows)]
point[0][0], point[0][1] = 1.0, 2.0
point[1][0], point[1][1] = 3.0, 7.0
point[2][0], point[2][1] = 5.0, 6.0
point[3][0], point[3][1] = 8.0, 3.0

px, py = appendfunc(point)
bezier = decasteljau(point, iterations)
x, y = appendfunc(bezier)

plt.plot(x, y, marker='o', color='blue')
plt.plot(px, py, 'ro', marker='x', color='red')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Bezier Curve of Four Predefined Points')
plt.show()

