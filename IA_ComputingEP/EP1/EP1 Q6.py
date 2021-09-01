def numint(n, a, b, x, w):
    sum = 0
    for i in range(n):
        sum += (w[i]*((x[i])**3+(x[i])**2))
    result = sum*(b-a)
    return result


#trapezium rule

print(numint(2, 0, 10, [0, 10], [1/2, 1/2]))
    

#simpson's rule

print(numint(3, 0, 10, [0, 5, 10], [1/6, 2/3, 1/6]))

#Gauss quadrature
a = 0
b = 10
x0 = (1/2)*(a + b - (b-a)/(3**(1/2)))
x1 = (1/2)*(a + b + (b-a)/(3**(1/2)))
print(numint(2, a, b, [x0, x1], [1/2, 1/2]))
