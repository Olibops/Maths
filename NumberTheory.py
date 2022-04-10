def create_N_pythagorean_triples(N=1):
    
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
    
def inefficient_create_N_pythagorean_triples(N=1):
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

#GCD algorithms, EA, , , return GCD, EEA returns bezout identity as a list

def euclidean_algorithm(M=2,N=1,Show_Working="No"): #Returns GCD
    a_n,b_n=max(abs(M),abs(N)),min(abs(M),abs(N))
    
    while b_n>0:
        q_n = a_n // b_n
        r_n = a_n- q_n * b_n
        if Show_Working == "Yes":
            print(str(a_n)+"="+str(q_n)+"x"+str(b_n)+"+"+str(r_n))
        a_n = b_n
        b_n = r_n
    if Show_Working == "Yes":
        print("GCD(" + str(M) + "," + str(N) + ")=" + str(a_n))

    return a_n

def extended_euclidean_algorithm(N=1,M=2,Show_Working="No"):
   
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

        if Show_Working == "Yes":
            if step_counter == 0: 
                print( ( workings_length + 10 ) * " " + str(Bezout_a[0]) + ", " + str(Bezout_b[0]))
                print( ( workings_length + 10 ) * " " + str(Bezout_a[1]) + ", " + str(Bezout_b[1]))
            
            print(workings + ( workings_length - len(workings ) + 10 ) * " " + str(Bezout_a[-1]) + ", " + str(Bezout_b[-1]) )
        
        step_counter+=1
        a_n = b_n
        b_n = r_n

    if Show_Working == "Yes" and Bezout_a[0] >= 0:
        print("Therefore GCD(" + str(M) + "," + str(N) + ") = " + str(a_n) + " = " + str(Bezout_a[-2]) + "x" + str(min(abs(M),abs(N))) + " + " + str(Bezout_b[-2]) + "x" + str(max(abs(M),abs(N)))  )
    
    if Show_Working == "Yes" and Bezout_a[0] < 0:
        print("Therefore GCD(" + str(M) + "," + str(N) + ") = " + str(a_n) + " = " + str(Bezout_b[-2]) + "x" + str(min(abs(M),abs(N))) + " + " + str(Bezout_a[-2]) + "x" + str(max(abs(M),abs(N)))  )

    if N >= M:
        return [a_n,Bezout_a[-2],Bezout_b[-2]]
    if N < M:
        return [a_n,Bezout_b[-2],Bezout_a[-2]]

#Corollaries from GCDs

def least_common_multiple(N=1,M=2,Show_Working="No"):
    if Show_Working == "Yes":
        print("First we calculate GCD(" + str(M) + "," + str(N) + ") with the Euclidean Algorithm")
    GCD = euclidean_algorithm(N,M,Show_Working)
    LCM = int ( M * N / GCD )
    if Show_Working == "Yes":
        print("Therefore LCM(" + str(M) + "," + str(N) + ")" +  "=" + str(M) + "x" + str(N) + "/GCD(" + str(M) + "," + str(N) + ")=" + str(M) + "x" + str(N) + "/" + str(GCD) + "=" + str(M*N))
    else:
        print(LCM)
    return LCM




















































