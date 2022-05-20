import functions as f
import brilhart as b

def alg(n, write_to_file=False):
    primes = b.get_primes()
    answ = f.count_solovei(n, 10)
    if answ == '    yes':
        if write_to_file:
            f.write_to_csv(write_to_file, (str(n)+ ' is prime by solovei method'))
        else:
            print(n, 'is prime by solovei method')
        return(n)
    else:
        if n in primes:
            if write_to_file:
                f.write_to_csv(write_to_file, (str(n) + ' is prime by table'))
            else:
                print(n)
            return('b is prime')
        result = f.try_divide(n)
        if result == 'plain':
            r = f.count_pollard_v1(n, 2)
            if r != 1 and r != 491:
                n = int(n/r)
                if write_to_file:
                    f.write_to_csv(write_to_file, (str(r) + ' by pollard v2'))
                else:
                    print(r, 'by pollard v2')
                alg(n,write_to_file)
            else:
                result = b.brilhart_moris(n)
                if result != 1:
                    n = int(n/result)
                    if write_to_file:
                        f.write_to_csv(write_to_file, (str(result) + ' by brilhart_moris'))
                    else:
                        print(result, ' by brilhart_moris')
                    alg(n,write_to_file)
                else:
                    print('didnt work')


        else:
            n = int(n/result)
            if write_to_file:
                f.write_to_csv(write_to_file, (str(result) + ' by пробні ділення'))
            else:
                print(result, ' by пробні ділення')
            alg(n,write_to_file)

def algorithm(n, write_to_file=False):
    if type(n) is list:
        for i in n:
            if write_to_file:
                f.write_to_csv(write_to_file, ('n = ' + str(i)))
                f.write_to_csv(write_to_file, ('\n'))
            alg(i, write_to_file)

                #
    else:
        alg(n, write_to_file)


n = input()
algorithm(n)