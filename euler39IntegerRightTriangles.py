#if p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p ≤ 1000, is the number of solutions maximised?

def PerfectSquare(n):
    result = False
    root = n**0.5
    if int(root + 0.5)**2 == n:
        result = True
    return result

def IntegerRightTriangles(n):
    count_max = 0
    p_max = 0
    for p in range (n//4*2, n+1,2): #p can be only even for this to be true and if p got n solutions, then 2p will either get n ones or more.
        count = 0
        for a in range(2, int(p/(2 + 2**0.5))+1): # from a+b>c
            if p*(p-2*a) % (2*(p-a)) ==0:# from the condition a+b+c = p and pythogoras condition
                count += 1
        if count > count_max:
            count_max, p_max = count, p
    return p_max


final = IntegerRightTriangles(1000)
#final = PerfectSquare(8)
print(final)