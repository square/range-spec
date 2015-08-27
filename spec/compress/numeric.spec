# No range
n1
n1

n1..3
n1
n2
n3

# Leading zeros
n01..3
n01
n02
n03

# Leading zeros across tens boundary
n09..11
n09
n10
n11

# Leading zeros fakeout
n003..4,n01..2
n01
n02
n003
n004

# Changing prefix
x1..2,y3..4
x1
y3
x2
y4

# Changing suffix
x1..2x,x3y
x1x
x2x
x3y

# Non-sequential range
x1..2,x4..5
x1
x5
x2
x4

# Maintain sort when we add digit columns
x98..100
x98
x99
x100
