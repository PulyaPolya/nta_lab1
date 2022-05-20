import random
import math
import csv
def gcd(x, y):
    if x > 0:
        x = -x
    if y < 0:
        y = -y
    while (y):
        x, y = y, x % y

    return x
def func(x):
    return x**2+1
def count_pollard_v1(n,x_0=2, write_to_file=False):
    arr=[]
    arr.append(x_0)
    r = 1
    i=0
    while r==1 or r==n:
        for x_i in arr:
            r=gcd(arr[-1]-x_i,n)
            i += 1
            if r!=1 and r!=n:
                break
        x=func(arr[-1])%n
        arr.append(x)
    if write_to_file:
        write_to_csv(write_to_file, str(r))
    return r
def count_pollard_v2(n,x_0=2, write_to_file=False):
    arr = []
    arr.append(x_0)
    r = 1
    i=0
    while r == 1 or r == n:
        k=arr.index(arr[-1])
        if k%2==0:
            j=k//2
            r = gcd(arr[k] - arr[j], n)
            i += 1
        x = func(arr[-1])%n
        arr.append(x)
    if write_to_file:
        write_to_csv(write_to_file, str(r))
    return r
def count_k(j):
    h=0
    while 1==1:
        if 2**h<=j and 2**(h+1)>j:
            return 2**h-1
        else:
            h=h+1
def count_pollard_v3(n,x_0=2,write_to_file=False ):
    arr = []
    arr.append(x_0)
    r = 1
    i = 0
    while r == 1 or r == n:
        j=arr.index(arr[-1])
        if j!=0:
            k=count_k(j)
            r = gcd(arr[j] - arr[k], n)
            i += 1
        x = func(arr[-1]) % n
        arr.append(x)
    if write_to_file:
        write_to_csv(write_to_file, str(r))
    return (r, i, arr)

def jacobi_symbol(a,n):
    if gcd(a,n) != 1:
        return 0
    res = 1
    while a != 1:
        if a < 0:
            a = -a
            res = res * (-1)** ((n-1)/2)
        while a % 2 == 0:
            a = a / 2
            res = res * (-1) ** ((n**2 - 1) / 8)
        if a == 1 :
            break

        if a < n:
           temp = a
           a = n
           n = temp
           res = res * (-1) ** ((n - 1) / 2 * ((a-1)/ 2))
        if a > n:
            a = a % n
    if a == 1:
        return 1 * res
def pseudo_simple(a,p):
    if gcd(a,p) != 1:
        return 'no'
    else:
        jac = jacobi_symbol(a, p)
        if jac == -1:
            jac = p - 1
        deg = int((p - 1) / 2)
        pow = FastPow(a, deg, p)
        #pow = a ** deg
        if jac == pow % p:
            return 'yes'
        else:
            return 'no'
def count_solovei(p, k):
    i = 0
    while i < k:
        x= random.randint(2,p-1)
        if gcd(x,p) == 1:
           if pseudo_simple(a = x, p = p) == 'no':
               return 'no'
           else:
               i += 1
        else:
            return 'no'
    if i == k:
        return 'yes'

def count_r(m, t):
    r = []
    r_prev = 1
    r.append(r_prev)
    for i in range (1, t):
        r_i = (r_prev * 10)
        r_i = r_i % m
        r.append(r_i)
        r_prev = r_i
    return r
def try_divide(n,  write_to_file=False):
    t = len(str(n))
    #top_verge = int(math.sqrt(n))
    top_verge = 47
    for m in range (2, top_verge):
        sum = 0
        r = count_r(m, t)
        n_rev= str(n)[::-1]
        for i in range (t):
            sum += int(n_rev[i]) * r[i]
        if sum % m == 0 :
            if write_to_file:
                write_to_csv(write_to_file, str(m))
            return m
    if write_to_file:
        write_to_csv(write_to_file, 'plain')
    return 'plain'



def count_row(arr, n):
    b=1
    b_prev = 0
    b_arr=[]
    b_arr.append(b)
    b_sq = []
    b_sq.append(b)
    for a in arr:
        temp = b
        b = b * a + b_prev
        b = b % n

        b_arr.append(b)
        b_prev = temp
        b_square = (b ** 2) % n
        if b_square > n/2:
            b_square = b_square - n
        b_sq.append(b_square)
    return (b_arr, b_sq)


def FastPow(t, k, mod):
    res = 1
    while k:
        if (k & 1):
            res *= t
            res = res% mod
        k = k >> 1
        if k == 0:
            break
        t *= t
        t = t% mod
    res = res% mod
    return res

'''
arr = [9172639163, 8627969789, 8937716743, 278874899, 99400891, 116381389, 4252083239, 6633776623, 227349247,3568572617]
for i in arr:
    with open('inf', 'a',encoding = 'utf-8') as f:
        #f.read()
        start = time.time()
        d = count_pollard_v1(i, 2)
        end = time.time()
        #print(end - start, 's')
        print('n = '+str(i), end =' ')
        print(' d = '+str(d),end =' ')
        #f.write('\n')
        print(' time ='+str(end - start) + ' s')
        #print('\n')
        f.close()
        
'''
def read_from_csv(filename):
    arr_numb = []
    with open(filename, newline='') as csvfile:
        inf = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in inf:
            if (row != ['n']):
                arr_numb.append(int(row[0]))
    return arr_numb
def write_to_csv(filename, result):
    with open(filename, 'a', newline='') as csvfile:
        inf = csv.writer(csvfile, delimiter=' ',  quoting=csv.QUOTE_MINIMAL)
        if type(result) is list:
            for i in result:
                inf.writerow([str(i)])
        elif type(result) is str:
            inf.writerow([result])
        else:
            inf.writerow([str(result)])

    csvfile.close()
def evklid(a,n):
    arr_r = []
    arr_r.append(a)
    arr_r.append(n)
    arr_q = []
    arr_s = []
    arr_t = []
    arr_s.append(1)
    arr_s.append(0)
    arr_t.append(0)
    arr_t.append(1)
    r = -10
    while r != 1 or r !=0:
       r = arr_r[-2]%arr_r[-1]
       q = arr_r[-2] // arr_r[-1]
       arr_r.append(r)
       arr_q.append(q)
       s = arr_s[-2] - arr_q[-1] *arr_s[-1]
       t = arr_t[-2] - arr_q[-1] * arr_t[-1]
       arr_s.append(s)
       arr_t.append(t)
       #print(q,r,s,t)
       if r == 0:
           break
    return (arr_r[-2], arr_s[-2], arr_t [-2])

def get_minus(a , n):
    a = a %n
    d = math.gcd(a, n)
    if d == 1:
        r, s, t = evklid(a, n)

        a_minus = s
        return a_minus%n
    else:
        return ':('


