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