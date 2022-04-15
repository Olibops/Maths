#general maths functions that really shouldn't be missing

def sign(X):
    if X == 0:
        Sign=0
    else:
        Sign = int(abs(X)//X)
    return Sign

#Algorithms for finding "special numbers"

def N_pythagorean_triples(N=1):
    
    for i in range(N + 1):
        if (1 + i) * i /2 >= N:
            x=i
            break

    Storage_List=[]
    for i in range(1,x+2):
        for j in range(i,x+2):
            a=abs(i ** 2 - j ** 2)
            if a == 0:
                continue
            b = 2 * i * j
            c=i ** 2 + j ** 2
            Storage_List=Storage_List+[[a,b,c]]
            if len(Storage_List) > N:
                break
    
    for i in range(N):
        Storage_List[i].sort()
    Storage_List.sort()
    print("Here are the first " + str(N) + " Pythagorean Triples")
    for i in range(N):
        print(Storage_List[i])

def brute_force_N_pythagorean_triples(N=1):
    def pythagorean_triple_search(N=1):
        Storage_List=[]
        for i in range(1,N):
            for j in range(1,N):
                for k in range(1,N):
                    if i ** 2 + j ** 2 == k ** 2:
                        Storage_List = Storage_List + [( i, j, k )]
        
        for i in range(len(Storage_List)):
            Storage_List[i]=list(Storage_List[i])
            Storage_List[i].sort()
            Storage_List[i]=tuple(Storage_List[i])

        Storage_List=list(set(Storage_List))
        Storage_List.sort()
        return Storage_List
    i=0
    while len(pythagorean_triple_search(i)) < N:
        i += 1
        triples=pythagorean_triple_search(i)
    print("Here are the first " + str(N) + " Pythagorean Triples")
    for i in range(N):
        print(triples[i])

def N_fibonacchi(N,estimate_G_ratio=True):
    list=[1,1]
    G_list=[]
    for i in range(N):
        list = list + [ list[-1] + list[-2] ]
    print(list)
    if estimate_G_ratio == True:
        for i in range(1,N):
            G_list=G_list+[ list[i] / list[i-1] ]
        print(G_list)


#GCD algorithms, EA, EEA, , return GCD, EEA also returns bezout identity as a list

def brute_force_GCD(X,Y,Show_working=True):

    x=0

    test_range=range(1, int(min(X,Y)) +1 )

    for i in test_range:
        if X % i == 0 and Y % i == 0:
            x=i
    print(x)

def euclidean_algorithm(M=2,N=1,Show_Working=False): #Returns GCD
    a_n,b_n=max(abs(M),abs(N)),min(abs(M),abs(N))
    
    while b_n>0:
        q_n = a_n // b_n
        r_n = a_n- q_n * b_n
        if Show_Working == True:
            print(str(a_n)+"="+str(q_n)+"x"+str(b_n)+"+"+str(r_n))
        a_n = b_n
        b_n = r_n
    if Show_Working == True:
        print("GCD(" + str(M) + "," + str(N) + ")=" + str(a_n))

    return a_n


def extended_euclidean_algorithm(N=1,M=2,Show_Working=False):

    N_sign = sign(N)
    M_sign = sign(M)

    a_n,b_n=max(abs(M),abs(N)),min(abs(M),abs(N))

    Bezout_a = [1,0]
    Bezout_b = [0,1]

    step_counter=0
    workings_length=0

    while b_n>0:
        q_n = a_n // b_n
        r_n = a_n- q_n * b_n

        Bezout_a = Bezout_a + [Bezout_a[-2] - q_n * Bezout_a[-1]]
        Bezout_b = Bezout_b + [ Bezout_b[-2] - q_n * Bezout_b[-1]]

        workings=str(a_n)+"="+str(q_n)+"x"+str(b_n)+"+"+str(r_n)
        workings_length = max(workings_length,len(workings))

        if Show_Working == True:
            if step_counter == 0: 
                print( ( workings_length + 10 ) * " " + str(Bezout_a[0]) + ", " + str(Bezout_b[0]))
                print( ( workings_length + 10 ) * " " + str(Bezout_a[1]) + ", " + str(Bezout_b[1]))
            
            print(workings + ( workings_length - len(workings ) + 10 ) * " " + str(Bezout_a[-1]) + ", " + str(Bezout_b[-1]) )
        
        step_counter+=1
        a_n = b_n
        b_n = r_n

    if abs(N) >= abs(M):
        
        if Show_Working == True:
            print("Therefore GCD(" + str(N) + "," + str(M) + ") = " + str(a_n) + " = " + str( N_sign * Bezout_a[-2]) + "x" + str(N) + " + " + str( M_sign * Bezout_b[-2]) + "x" + str(M) )
       
        return [a_n, N_sign * Bezout_a[-2], M_sign * Bezout_b[-2]]

    else:

        if Show_Working == True:
            print("Therefore GCD(" + str(N) + "," + str(M) + ") = " + str(a_n) + " = " + str( M_sign * Bezout_a[-2]) + "x" + str(M) + " + " + str( N_sign * Bezout_b[-2]) + "x" + str(N) )

        return [a_n, N_sign * Bezout_b[-2], M_sign * Bezout_a[-2]]

def dijkstras_GCD(X,Y,Show_Working=False):
    while X != Y:
        X, Y = max(abs(X - Y),Y), min(abs(X - Y),Y)
        if Show_Working == True:
            print(X,Y)
    print(X)

#Corollaries from GCDs

def least_common_multiple(N=1,M=2,Show_Working=False):
    if Show_Working == True:
        print("First we calculate GCD(" + str(M) + "," + str(N) + ") with the Euclidean Algorithm")
    GCD = euclidean_algorithm(N,M,Show_Working)
    LCM = int ( M * N / GCD )
    if Show_Working == True:
        print("Therefore LCM(" + str(M) + "," + str(N) + ")" +  "=" + str(M) + "x" + str(N) + "/GCD(" + str(M) + "," + str(N) + ")=" + str(M) + "x" + str(N) + "/" + str(GCD) + "=" + str(M*N))
    else:
        print(LCM)
    return LCM

def linear_diophantine(a=1,b=1,c=1,Show_Working=False): #Not finished
    #Find x,y such that ax+by=c
    if Show_Working==True:
        print("First we calculate the GCD, and Bezout Identities of " + str(abs(a)) + " and " + str(abs(b)) + " with the Euclidean Algorithm")
        GCD_Bezout= extended_euclidean_algorithm(a,b,Show_Working)
    else:
        GCD_Bezout = extended_euclidean_algorithm(a,b)
    GCD=GCD_Bezout[0]
    Solveable = c % GCD
    if Solveable == 0:

        multiplier=c // GCD
        X_Y=[ multiplier * GCD_Bezout[1], multiplier * GCD_Bezout[2]]

        if Show_Working==True:
            print("Thus " + str(a) + "x" + "+" + str(b) + "y=" + str(c) + " is solveable because " + str(GCD) + "|" + str(c) )
            print("As " + str(c) + " = " + str(multiplier) + "x" + str(GCD) +" = " + str(multiplier * GCD_Bezout[1]) + "x" + str(a) + " + " + str(multiplier * GCD_Bezout[2]) + "x" + str(b) + " we have the particular solution (x,y)" + " = (" + str(X_Y[0]) + ", " + str(X_Y[1]) + ")" )        

        return X_Y
    else:
        return False
        if Show_Working==True:
            print("Thus " + str(a) + "x" + "+" + str(b) + "y=" + str(c) + " is not solveable because " + str(GCD) + "∤" + str(c) )
        else:
            print(str(a) + "x" + "+" + str(b) + "y=" + str(c) + " is not solveable because " + str(GCD) + "∤" + str(c) )

def solve_linear_congruence(a=1,c=1,n=1,Show_Working=True): #aX=c mod n
    if Show_Working==True:
        print("To solve an modular congruence of the form " + str(a) + "X = " + str(c) + " mod " + str(n) + " note it can be rephrased as the linear Diophantine equation:")
        print(str(a) + "X + " + str(-n) + "Y = " + str(c) )
        print("which can be solved with the following method:")
    
    X=linear_diophantine(a,-n,c,Show_Working)
    if X==False:
        print("Therefore "+ str(a) + "X = " + str(c) + " mod " + str(n) + " is not solveable")




















































