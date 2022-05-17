import math
import random

import functions as f
from math import exp, sqrt, log, log2
from vectors import add_one
import numpy as np


def get_primes():
    file_name= 'prime'
    res=[]
    with open(file_name, 'r') as file:
        content=file.read()
        numbers= content.split()
    for number in numbers:
        res.append(int(number))
    return res
def get_B(n,k = False):
    B = []
    #B.append(-1)
    primes = get_primes()
    a = 1 / (sqrt(2))

    L=exp((log2(n) * log2(log2(n)))** 0.5)

    limit = (L ** a)
    if k :
        for number in primes:

            if f.jacobi_symbol(n, number) == 1:
                B.append(number)
            elif f.jacobi_symbol(n, number) == 0:
                pass
            if len(B)>= k+ 1:
                break
    else:
        for number in primes:
            if number < limit:
                if f.jacobi_symbol(n, number) == 1:
                    B.append(number)
                elif f.jacobi_symbol(n, number) == 0:
                        pass
                    #raise Exception
            else:
                break
    #B.pop(-2)
    random.shuffle(B)
    c = [-1]
    c+= B
    return c
def get_zepnaya_fraction_a(n, k):
    v = 1
    alpha_0=math.sqrt(n)
    alpha = alpha_0
    a=int(alpha)
    u=a
    arr_a=[]
    arr_a.append(a)
    i = 0
    while i < k:
        v = (n - u ** 2) / v
        alpha = (alpha_0 + u) / v
        a = int(alpha)
        u = a * v -u
        arr_a.append(a)
        i += 1
    return arr_a
def get_mod(k,n):
    k = k%n
    if k > n/2:
        k = k - n
    return k

def rozklastu_po_B(k,n, B):
    arr_degs = []
    if k <0:
        arr_degs.append(1)
    else:
        arr_degs.append(0)
    k = abs(k)
    for elem in B:
        deg = 0
        if abs(elem) != 1:
            while k%elem == 0:
                k /= elem
                deg += 1
            arr_degs.append(deg)
        if abs(k) ==1:
            break
    if k != 1:
        return 'no'
    else:
        if len(arr_degs) < len(B):
            for i in range( len(B)-len(arr_degs)):
                arr_degs.append(0)
        return arr_degs
def get_row_b_bsq(arr, n, B, k):
    b=1
    b_prev = 0
    b_arr=[]
    vect = {}
    #b_arr.append(b)
    b_sq = []
    #b_sq.append(b)
    for a in arr:
        temp = b
        b = b * a + b_prev
        #b = b % n
        b = get_mod(b,n)
        #b_arr.append(b)
        b_prev = temp
        b_square = get_mod(b**2, n)
        arr = rozklastu_po_B(b_square, n, B)
        if arr!= 'no':

            '''
            if b_square > n/2:
                b_square = b_square - n
            '''
            if b_square in b_sq:
                pass
            else:
                vect[b_square] = arr
                b_arr.append(b)
                b_sq.append(b_square)
        if len(b_arr) == k:
            break


    return (b_arr, b_sq, vect)

def get_coef(vectors, zero):
    vect_bin = {}
    for elem in vectors:
        vect_bin[elem] = vectors[elem].copy()
        for i in range(len(vect_bin[elem])):
            vect_bin[elem][i] = vect_bin[elem][i]%2
    max = 0

    arr_vect = []
    for elem in vect_bin:
        arr_vect.append(vect_bin[elem])
    zero_arr=[]
    keys = list(vect_bin.keys())
    length = len(vect_bin[keys[0]])
    for t in range (length):
        zero_arr.append(0)
    #zero_arr = result[:]
    result = zero_arr[:]
    zero_arr = np.array(zero_arr)
    start = 0
    numb_it = 0
    arr = zero[:]
    while start != 1 or not (result == zero_arr).all():
        arr = add_one(arr)
        #result = zero_arr[:]
        start = 1
        '''
        for k in range (length):
            i = 0
            for number in keys:
                result[k] += vectors[number][k] * arr[i]
                result[k] = result[k] % 2
                i += 1
        '''
        vect = np.array(arr_vect)
        v = np.array(arr)
        v = np.reshape(v, (len(arr_vect), 1))
        result = np.multiply(vect, v)
        result = np.sum(result, axis=0, keepdims=False)
        result = result % 2
        #print(result)
        #print(arr, '\n')
        numb_it+=1
        #print(numb_it)
    return arr
def get_X_Y(arr_coef, b_arr, b_sq, n):
    x = 1
    for i in range (len(b_sq)):
        x = (x * (b_arr[i] ** arr_coef[i])) % n

    y = 1

    '''
    for j in range(length):
        deg_p = 0
        for number in keys:
            deg_p += vectors[number][j] * arr_x[j]
        y = y * (b[j] ** deg_p) % n
    '''
    #i = 0
    #while i < n:
    y = 1
    #arr_k = list(vect.keys())
    minus = 0
    for j in range (len(arr_coef)):
        if arr_coef[j] !=0:
            if b_sq[j] < 0:
                minus  +=1
            y = y*b_sq[j]

                #y = y*  b_sq[j+1]


    #y = y%n
    y =int(sqrt(y))
    if minus % 4 !=0:
        y= y*(-1)
    '''
    for j in range(length):
        deg_p = 0
        i = 0
        for number in keys:
            deg_p += vectors[number][j] * arr_x[i]
            i += 1
        y = y * (B[j] ** deg_p) % n

    y = int(sqrt(y))
    '''
    #y = y%n
    return (x,y)

def get_gcd(x, y, n):
    sum = (x+y)%n
    dif =(x-y)%n
    print('{ ',sum , ' and ',dif, '}')
    if f.gcd(sum, n) != 1:
        return f.gcd(sum, n)
    else:
        return f.gcd(dif, n)

def make_square(arr):
     z  =np.array(arr)

     if np.shape(z)[0] < np.shape(z)[1]:
            t= np.shape(z)[1]- np.shape(z)[0]
            for i in range (t):
                a = [0]*len(arr[0])
                arr.append(a)
     if np.shape(z)[0] >= np.shape(z)[1]:
         for elem in arr:
             for i in range (np.shape(z)[0]- np.shape(z)[1]+1):
                 elem.append(0)
     z = np.array(arr)
     print(np.shape(z)[0], np.shape(z)[1])
     return arr
def brilhart_moris(n):
    result = 1
    t = False
    time = 1
    arr_coef = []
    while result == 1 or result == n:
        B = get_B(n, t)
        k = len(B)-1


        arr_a = get_zepnaya_fraction_a(n,2*k+1)
        arr_b, arr_b_sq, vect = get_row_b_bsq(arr_a, n, B, k)
        if time == 1:
            for t in range(len(vect)):
                arr_coef.append(0)
            time += 1
        arr_eq = []
        for elem in vect:
            arr_eq.append(vect[elem])
        if len(arr_coef) < len(vect):
            for i in range(len(vect)-len(arr_coef)):
                arr_coef.append(0)
        arr_coef=get_coef(vect, arr_coef)
        X, Y = get_X_Y(arr_coef, arr_b, arr_b_sq, n)
        result = get_gcd(X, Y, n)
        print( get_mod(X,n),get_mod(Y,n))
    return result


